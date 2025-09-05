<script lang="ts">
	import type { ProgressObj, ProgressData } from '$lib/types/response';
	import LineChart from '$lib/components/LineChart.svelte';

	let { progress }: { progress: ProgressObj } = $props();
	let progressData: ProgressData[] = progress.data;
	// Generate a random plot ID for each Progress component instance
	const plotId = `progress-plot-${Math.random().toString(36).substr(2, 9)}`;
</script>

<div class="m-4 flex flex-col items-center text-center">
	<h1 class="mb-4 text-2xl font-bold">{progress.title}</h1>
	<div class="mb-4 flex flex-row items-center gap-2">
		<progress class="progress progress-primary h-8 w-56" value={progress.progress} max={100}
		></progress>
		<div class="text-sm font-bold text-black">{progress.progress}%</div>
	</div>
	<LineChart
		title={'Progress over last days'}
		{plotId}
		xaxis="Date"
		yaxis="Progression (%)"
		displayXAxisGap={1}
		x={progressData.map((data) => data.date)}
		y={progressData.map((data) => data.progress)}
		yRange={[0, 100]}
	/>
</div>
