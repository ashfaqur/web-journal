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
		dates = result.dates;
		points = result.points;
		states = result.states;
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
