<script lang="ts">
	import PlotBar from '$lib/components/PlotBar.svelte';
	import PieChart from '$lib/components/PieChart.svelte';
	import { onMount } from 'svelte';
	import { fetchLastThirtyDays } from '$lib/api';
	import type { DayPoints, FetchLastDaysResult } from '$lib/types/response';

	const title = 'Points in last 30 Days';
	const xaxis = 'Date';
	const yaxis = 'Points';
	let xValues: string[] = $state([]);
	let yValues: number[] = $state([]);
	let stateValues: string[] = $state([]);
	let stateCounts: Map<string, number> = $state(new Map());
	let fallback: boolean = $state(false);
	// $inspect(xValues);
	// $inspect(yValues);
	$inspect(stateCounts);
	// Fetch data when the component is mounted
	onMount(async () => {
		try {
			const result: FetchLastDaysResult = await fetchLastThirtyDays();
			const data: DayPoints[] = result.data;
			fallback = result.isFallback;
			xValues = data.map((entry: DayPoints) => entry.date);
			yValues = data.map((entry: DayPoints) => entry.points);
			stateValues = data.map((entry: DayPoints) => entry.state);
			let stateMap = new Map<string, number>();
			stateValues.forEach((state) => {
				stateMap.set(state, (stateMap.get(state) || 0) + 1);
			});
			stateMap.forEach((value, key) => {
				if (value !== 0) {
					stateMap.set(key, Math.round((value * 100) / stateValues.length));
				}
			});
			stateCounts = stateMap;
			console.log('State Counts:', stateCounts);
		} catch (error) {
			console.error('Error fetching data:', error);
		}
	});
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-600 px-6 py-1">
		<h3 class="text-2xl">Last Month</h3>
	</div>
</section>

<!-- Graph -->
<section>
	<PlotBar {title} {xaxis} {yaxis} x={xValues} y={yValues} s={stateValues} {fallback} />
</section>

<section>
	<PieChart title={'Last 30 Days entry'} chart={stateCounts} {fallback} />
</section>
