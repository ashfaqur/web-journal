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
		fallback?: boolean;
		defaultColor?: string;
		displayXAxisGap?: number;
		plotId?: string;
		yRange?: [number, number];
	}

	let {
		title,
		xaxis,
		yaxis,
		x,
		y,
		states = [],
		stateColors = {},
		fallback = false,
		displayXAxisGap = 30,
		defaultColor = defaultColorValue,
		plotId = 'lineplot',
		yRange
	}: PlotlyProps = $props();

	if (!isValidPlotlyColor(defaultColor)) {
		defaultColor = defaultColorValue;
	}

	interface PlotlyData {
		x: string[];
		y: number[];
		mode: 'lines';
		line: { color: string };
	}

	let data: PlotlyData[] = $derived([
		{
			x,
			y,
			mode: 'lines',
			line: { color: defaultColor }
		}
	]);
	let layout = $derived({
		title: title,
		xaxis: {
			title: xaxis,
			tickvals: x, // Ensure all x values are plotted
			ticktext: x.map((label, index) => (index % displayXAxisGap === 0 ? dateToDDMM(label) : '')) // Hide labels
		},
		yaxis: {
			title: yaxis,
			...(yRange ? { range: yRange } : {})
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
