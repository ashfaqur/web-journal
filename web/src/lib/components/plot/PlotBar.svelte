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
		title: { text: title }, // chart title
		xaxis: {
			title: { text: xaxis },
			type: 'date',
			tickformat: tickFormat,
			automargin: true,
			...(x.length <= 7
				? {
						tickmode: 'array',
						tickvals: x,
						ticktext: x.map((d) => new Date(d).toLocaleDateString('en-US', { weekday: 'short' }))
					}
				: {
						tickformat: '%b %d' // fallback default for longer ranges
					})
		},
		yaxis: {
			title: { text: yaxis }
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
