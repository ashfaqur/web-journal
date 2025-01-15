<script lang="ts">
	import { onMount } from 'svelte';
	import Plotly from 'plotly.js-dist-min';
	import type { PlotlyData } from '$lib/types/plots';

	interface PlotlyProps {
		title: string;
		xaxis: string;
		yaxis: string;
		x: string[];
		y: number[];
		s: string[];
	}

	let { title, xaxis, yaxis, x, y, s }: PlotlyProps = $props();

	// Define colors for each state
	const stateColors: { [key: string]: string } = {
		None: 'gray',
		Complete: 'green',
		Incomplete: 'orange'
	};

	let data: PlotlyData[] = $derived([
		{
			x,
			y,
			type: 'bar',
			marker: { color: s.map((s) => stateColors[s] || 'black') }
		}
	]);
	let layout = $derived({
		title: title,
		xaxis: {
			title: xaxis,
			tickvals: x, // Ensure all x values are plotted
			ticktext: x.map((label, index) => (index % 2 === 0 ? label : '')) // Hide alternate labels
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
		console.log('updating');
		console.log(data);
		Plotly.newPlot('plot', data, layout, config);
	});
</script>

<div class="w-full"><div id="plot"></div></div>
