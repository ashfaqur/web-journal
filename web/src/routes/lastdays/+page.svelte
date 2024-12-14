<script lang="ts">
	import { onMount } from 'svelte';
	import Plotly from 'plotly.js-dist-min';

	// Generate the data for the bar plot
	const daysInMonth = 31;
	const yValues = Array.from({ length: daysInMonth }, (_, i) => i + 1);

	interface PlotlyData {
		x: number[];
		y: number[];
		type: 'bar';
	}

	let data: PlotlyData[] = [
		{
			x: Array.from({ length: daysInMonth }, (_, i) => i + 1),
			y: yValues,
			type: 'bar'
		}
	];

	let layout = {
		title: 'Bar Plot with Days of the Month',
		xaxis: {
			title: 'Day of the Month'
		},
		yaxis: {
			title: 'Value'
		}
	};

	let config = { responsive: true };

	onMount(() => {
		// Create the plot
		Plotly.newPlot('myDiv', data, layout, config);
	});
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-600 px-6 py-2">
		<h2 class="text-3xl font-bold">Last Days</h2>
	</div>
</section>

<!-- Graph -->
<section></section>

<div class="w-full"><div id="myDiv"></div></div>
