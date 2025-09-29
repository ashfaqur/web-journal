<script lang="ts">
	import Warning from '$lib/components/Warning.svelte';
	import PlotBar from '$lib/components/plot/PlotBar.svelte';
	import PieChart from '$lib/components/plot/PieChart.svelte';
	import { processLastDaysData, datesToDays } from '$lib/util';

	interface LastDaysProps {
		days: number;
		displayXAxisGap?: number;
	}

	let { days, displayXAxisGap = 1 }: LastDaysProps = $props();

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

	async function fetchData() {
		const result = await processLastDaysData(days);
		console.log('Last days data loaded:', result);
		dates = result.dates;
		points = result.points;
		states = result.states;
		stateCounts = result.stateCounts;
		fallback = result.fallback;
	}

	$effect(() => {
		// Calculate time taken to fetch data
		const start = performance.now();
		fetchData();
		const end = performance.now();
		console.debug(`Time to fetch last days data: ${end - start} ms`);
	});
</script>

{#if fallback}
	<Warning text="Showing mock data due to fetch error" />
{/if}

<PlotBar
	title={`Points earned over the last ${days} Days`}
	xaxis="Date"
	yaxis="Points"
	x={dates}
	y={points}
	{states}
	{stateColors}
/>

<PieChart
	title={`Percentage of days having entries`}
	chart={stateCounts}
	{stateColors}
	{fallback}
/>
