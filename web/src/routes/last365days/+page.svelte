<script lang="ts">
	import { onMount } from 'svelte';
	import PieChart from '$lib/components/PieChart.svelte';
	import LineChart from '$lib/components/LineChart.svelte';
	import { processLastDaysData } from '$lib/util';

	const days = 365;
	const title = 'Last 365 Days';

	let fallback: boolean = $state(false);
	let dates: string[] = $state([]);
	let points: number[] = $state([]);
	let states: string[] = $state([]);
	let stateCounts: Map<string, number> = $state(new Map<string, number>());

	// Define colors for each state
	const stateColors: { [key: string]: string } = {
		None: 'gray',
		Complete: 'green',
		Incomplete: 'orange'
	};

	onMount(async () => {
		const result = await processLastDaysData(days);
		// Filter the data to include only items with the state "Complete"
		const filteredData = result.states
			.map((state, index) => ({
				date: result.dates[index],
				point: result.points[index],
				state
			}))
			.filter((item) => item.state === 'Complete' && item.point > 0);

		// Extract the filtered dates, points, and states
		dates = filteredData.map((item) => item.date);
		points = filteredData.map((item) => item.point);
		states = filteredData.map((item) => item.state);
		stateCounts = result.stateCounts;
		fallback = result.fallback;
	});
</script>

<!-- Title -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>

<LineChart
	title={`Points earned daily`}
	xaxis="Date"
	yaxis="Points"
	x={dates}
	y={points}
	{states}
	{stateColors}
	{fallback}
/>

<PieChart
	title={`Percentage of days having entries`}
	chart={stateCounts}
	{stateColors}
	{fallback}
/>
