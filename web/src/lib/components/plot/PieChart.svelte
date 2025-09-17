<script lang="ts">
	import { onMount } from 'svelte';
	import Plotly from 'plotly.js-dist-min';

	interface PieChartProps {
		title: string;
		chart: Map<string, number>;
		stateColors: { [key: string]: string };
		fallback: boolean;
	}

	let { title, chart, stateColors, fallback }: PieChartProps = $props();

	interface PlotlyData {
		labels: string[];
		values: number[];
		type: 'pie';
		marker: { colors: string[] };
	}

	let data: PlotlyData[] = $derived([
		{
			labels: Array.from(chart.keys()),
			values: Array.from(chart.values()),
			type: 'pie',
			marker: {
				// Map stateColors to the corresponding labels
				colors: Array.from(chart.keys()).map((state) => stateColors[state] || 'black')
			}
		}
	]);

	let layout = $derived({
		title: title
	});

	const config = { responsive: true };

	onMount(() => {
		Plotly.newPlot('pie-chart', data, layout, config);
	});

	$effect(() => {
		Plotly.newPlot('pie-chart', data, layout, config);
	});
</script>

<div class="w-full">
	<div id="pie-chart"></div>
</div>
