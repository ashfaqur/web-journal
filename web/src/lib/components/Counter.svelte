<script lang="ts">
	import type { DayCounts } from '$lib/types/response';
	import PlotBar from '$lib/components/PlotBar.svelte';
	import LineChart from './LineChart.svelte';
	import { onMount } from 'svelte';
	import { fetchCounterCumulativeData } from '$lib/api';
	import type { FetchCounterCumulativeResult } from '$lib/types/response';

	let { counterName, counts }: { counterName: string; counts: DayCounts[] } = $props();

	let cumulativeCounts: [date: string, count: number][] = $state([]);

	onMount(async () => {
		const result: FetchCounterCumulativeResult = await fetchCounterCumulativeData(counterName, 180);
		if (!result.isFallback) {
			// convert date to DD/MM format from YYYY-MM-DD
			cumulativeCounts = result.data.map(([date, , count]) => [date, count]);
		}
	});
</script>

<!-- Plot -->
<PlotBar
	title={`"${counterName}" over last 30 days`}
	xaxis="Date"
	yaxis="Count"
	x={counts.map((c) => c.date)}
	y={counts.map((c) => c.count)}
/>

<!-- {#if cumulativeCounts.length > 0} -->
<LineChart
	title={`"${counterName}" (Cumulative) over last 180 days`}
	xaxis="Date"
	yaxis="Cumulative Count"
	displayXAxisGap={2}
	x={cumulativeCounts.map(([date]) => date)}
	y={cumulativeCounts.map(([, count]) => count)}
/>
<!-- {/if} -->
