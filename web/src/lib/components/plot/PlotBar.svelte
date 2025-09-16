<script lang="ts">
	import Plotly from 'plotly.js-dist-min';
	import { isValidPlotlyColor, dateToDDMM } from '$lib/util';
	import { defaultColorValue } from '$lib/constants';

	interface PlotlyProps {
		title: string;
		xaxis: string;
		yaxis: string;
		x: string[];
		y: number[];
		states?: string[];
		stateColors?: { [key: string]: string };
		defaultColor?: string;
		plotId?: string;
	}

	let {
		title,
		xaxis,
		yaxis,
		x,
		y,
		states = [],
		stateColors = {},
		defaultColor = defaultColorValue,
		plotId = 'barplot'
	}: PlotlyProps = $props();

	interface PlotlyData {
		x: string[];
		y: number[];
		type: 'bar' | 'pie';
		marker: { color: string[] };
	}

	if (!isValidPlotlyColor(defaultColor)) {
		defaultColor = defaultColorValue;
	}

	let data: PlotlyData[] = $derived([
		{
			x,
			y,
			type: 'bar',
			marker: {
				color:
					states.length > 0
						? states.map((s) => stateColors[s] || defaultColor)
						: x.map(() => defaultColor)
			}
		}
	]);

	let tickFormat = $derived(x.length <= 7 ? '%a' : '%b %d');

	let layout: any = $derived({
		title: title,
		xaxis: {
			title: xaxis,
			type: 'date', // <-- important
			tickformat: tickFormat, // optional: format ticks as DD/MM
			automargin: true
		},
		yaxis: {
			title: yaxis
		}
	});
	const config = { responsive: true };

	$effect(() => {
		Plotly.newPlot(plotId, data, layout, config);
	});
</script>

<div class="w-full">
	<div id={plotId}></div>
</div>
