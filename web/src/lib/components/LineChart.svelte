<script lang="ts">
	import { onMount } from 'svelte';
	import Plotly from 'plotly.js-dist-min';

	interface PlotlyProps {
		title: string;
		xaxis: string;
		yaxis: string;
		x: string[];
		y: number[];
		states: string[];
		stateColors: { [key: string]: string };
		fallback: boolean;
	}

	let { title, xaxis, yaxis, x, y, states, stateColors, fallback }: PlotlyProps = $props();

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
			line: { color: 'green' }
		}
	]);
	let layout = $derived({
		title: title,
		xaxis: {
			title: xaxis,
			tickvals: x, // Ensure all x values are plotted
			ticktext: x.map((label, index) => (index % 30 === 0 ? label : '')) // Hide alternate labels
		},
		yaxis: {
			title: yaxis
		}
	});
	const config = { responsive: true };

	onMount(() => {
		Plotly.newPlot('plot', data, layout, config);
	});

	$effect(() => {
		Plotly.newPlot('plot', data, layout, config);
	});
</script>

<div class="w-full">
	<div id="plot"></div>
</div>
