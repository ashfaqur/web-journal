<script lang="ts">
	import { onMount } from 'svelte';
	import { fetchProgressData } from '$lib/api';
	import type { ProgressObj, FetchProgressResult } from '$lib/types/response';
	import Progress from '$lib/components/Progress.svelte';

	const title = 'Progress';

	let progressObjs: ProgressObj[] = [];
	let isFallback = false;

	onMount(async () => {
		const result: FetchProgressResult = await fetchProgressData();
		progressObjs = result.data;
		isFallback = result.isFallback;
		console.log('Progress data loaded:', progressObjs, 'Is fallback:', isFallback);
	});
</script>

<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>

{#if isFallback}
	<div class="rounded bg-yellow-200 px-4 py-2 text-center">
		<p class="text-yellow-900">Displaying fallback data due to fetch error.</p>
	</div>
{/if}

<section>
	<!-- Loop over all the progress objects in the progress data array -->
	{#each progressObjs as progress}
		<Progress {progress} />
	{/each}
</section>
