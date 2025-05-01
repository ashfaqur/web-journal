<script lang="ts">
	import { onMount } from 'svelte';
	import Plotly from 'plotly.js-dist-min';

	interface PieChartProps {
		title: string;
		chart: Map<string, number>;
		fallback: boolean;
	}

	let { title, chart, fallback }: PieChartProps = $props();

	$inspect(chart);

	// let labels = ['Category A', 'Category B', 'Category C'];
	// let values = [30, 50, 20];

	// interface PieData {
	// 	labels: string[];
	// 	values: number[];
	// 	type: string;
	// 	marker: { color: string[] };
	// }

	// Define colors for each state
	const stateColors: { [key: string]: string } = {
		None: 'gray',
		Complete: 'green',
		Incomplete: 'orange'
	};

	let data: any[] = $derived([
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

	// let data: any = [
	// 	{
	// 		labels: labels,
	// 		values: values,
	// 		type: 'pie'
	// 	}
	// ];

	let layout = $derived({
		title: 'Percentage of Day Entries in Last 30 Days'
	});

	const config = { responsive: true };

	onMount(() => {
		Plotly.newPlot('pie-chart', data, layout, config);
	});

	$effect(() => {
		console.log('updating pie chart');
		console.log(data);
		Plotly.newPlot('pie-chart', data, layout, config);
	});
</script>

<div id="pie-chart"></div>
