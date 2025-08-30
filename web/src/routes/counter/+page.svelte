<script lang="ts">
	import { onMount } from 'svelte';
	import { fetchCounterData } from '$lib/api';
	import Counter from '$lib/components/Counter.svelte';
	import type { FetchCounterDataResult, CounterDataDict } from '$lib/types/response';

	const title = 'Counter';
	let counterData: CounterDataDict = $state({});

	onMount(async () => {
		const result: FetchCounterDataResult = await fetchCounterData(30);
		counterData = result.data;
	});
</script>

<!-- Title -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>

<section>
	<!-- Loop over all the counters in the counter data dict -->
	{#each Object.entries(counterData) as [counterName, counts]}
		<Counter {counterName} {counts} />
	{/each}
</section>
