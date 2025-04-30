<script lang="ts">
	import PlotBar from '$lib/components/PlotBar.svelte';
	import { onMount } from 'svelte';
	import { fetchLastThirtyDays } from '$lib/api';
	import type { DayPoints, FetchLastDaysResult } from '$lib/types/response';

	const title = 'Points in last 30 Days';
	const xaxis = 'Date';
	const yaxis = 'Points';
	let xValues: string[] = $state([]);
	let yValues: number[] = $state([]);
	let stateValues: string[] = $state([]);
	let fallback: boolean = $state(false);
	$inspect(xValues);
	$inspect(yValues);

	// Fetch data when the component is mounted
	onMount(async () => {
		try {
			const result: FetchLastDaysResult = await fetchLastThirtyDays();
			const data: DayPoints[] = result.data;
			fallback = result.isFallback;
			console.log('Data:', data);
			xValues = data.map((entry: { date: string }) => entry.date);
			yValues = data.map((entry: { points: number }) => entry.points);
			stateValues = data.map((entry: { state: string }) => entry.state);
		} catch (error) {
			console.error('Error fetching data:', error);
		}
	});
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-600 px-6 py-1">
		<h3 class="text-2xl">Last Days</h3>
	</div>
</section>

<!-- Graph -->
<section>
	<PlotBar {title} {xaxis} {yaxis} x={xValues} y={yValues} s={stateValues} {fallback} />
</section>
