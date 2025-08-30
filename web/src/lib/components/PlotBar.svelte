<script lang="ts">
	import { onMount } from 'svelte';
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
		displayXAxisGap?: number;
		fallback?: boolean;
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
		displayXAxisGap = 1,
		fallback = false,
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
	let layout = $derived({
		title: title,
		xaxis: {
			title: xaxis,
			tickvals: x, // Ensure all x values are plotted
			ticktext: x.map((label, index) => (index % displayXAxisGap === 0 ? dateToDDMM(label) : ''))
		},
		yaxis: {
			title: yaxis
		}
	});
	const config = { responsive: true };

	onMount(() => {
		Plotly.newPlot(plotId, data, layout, config);
	});

	$effect(() => {
		Plotly.newPlot(plotId, data, layout, config);
	});
</script>

<div class="w-full">
	<div id={plotId}></div>
</div>
