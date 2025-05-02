<script lang="ts">
	import { onMount } from 'svelte';
	import WarnServerInactive from './WarnServerInactive.svelte';
	import PlotBar from './PlotBar.svelte';
	import PieChart from './PieChart.svelte';
	import type { DayPoints, FetchLastDaysResult } from '$lib/types/response';
	import { fetchLastDays } from '$lib/api';

	interface LastDaysProps {
		title: string;
		days: number;
	}

	let { title, days }: LastDaysProps = $props();

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
		const result: FetchLastDaysResult = await fetchLastDays(days);
		const data: DayPoints[] = result.data;
		fallback = result.isFallback;
		dates = data.map((entry: DayPoints) => entry.date);
		points = data.map((entry: DayPoints) => entry.points);
		states = data.map((entry: DayPoints) => entry.state);
		let stateMap = new Map<string, number>();
		states.forEach((state) => {
			stateMap.set(state, (stateMap.get(state) || 0) + 1);
		});
		stateMap.forEach((value, key) => {
			if (value !== 0) {
				stateMap.set(key, Math.round((value * 100) / states.length));
			}
		});
		stateCounts = stateMap;
		console.log('State Counts:', stateCounts);
	});
</script>

<!-- Title -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>

<WarnServerInactive />

<PlotBar
	title={`Points earned daily in the last ${days} Days`}
	xaxis="Date"
	yaxis="Points"
	x={dates}
	y={points}
	{states}
	{stateColors}
	{fallback}
/>

<PieChart
	title={`Percentage of days having entries in the last ${days} days`}
	chart={stateCounts}
	{stateColors}
	{fallback}
/>
