<script lang="ts">
	import type { ProgressObj, ProgressData } from '$lib/types/response';
	import LineChart from '$lib/components/LineChart.svelte';

	let { progress }: { progress: ProgressObj } = $props();
	let progressData: ProgressData[] = progress.data;
	console.log('Progress component received data:', progressData);
	// Generate a plot ID based on progress obj title to ensure uniqueness
	const progressPlotId = `progress-plot-${progress.title.replace(/[\s-]+/g, '').toLowerCase()}`;

	const latestProgress = progressData[progressData.length - 1]?.totalProgress || 0;
	console.log(
		`Rendering progress component for "${progress.title}" with latest progress: ${latestProgress}%`
	);

	// Last 3 months of data
	const longTermProgressData = progressData.slice(-90);

	// Get the last 30 days of progress data
	const shortTermProgressData = progressData.slice(-30);

	let shortTermProgressAverage = 0;
	let daysToComplete = Infinity;

	if (shortTermProgressData.length > 0) {
		const latestProgress = shortTermProgressData.at(-1)!.totalProgress;

		// Start from most recent, move backwards until we see a drop
		let minValue = latestProgress;
		let daysUsed = 1; // At least 1 day (latest)

		for (let i = shortTermProgressData.length - 2; i >= 0; i--) {
			const value = shortTermProgressData[i].totalProgress;
			if (value <= minValue) {
				minValue = value;
				daysUsed = shortTermProgressData.length - i;
			} else {
				break;
			}
		}

		// Average daily increase
		shortTermProgressAverage = (latestProgress - minValue) / daysUsed;

		// Days to complete the progress at the current rate
		daysToComplete =
			shortTermProgressAverage > 0
				? Math.ceil((100 - latestProgress) / shortTermProgressAverage)
				: Infinity;
	} else {
		console.log('No progress data available');
	}
</script>

<div class="flex flex-col items-center pb-5 pt-5 text-center">
	<h1 class="mb-4 text-3xl font-bold">{progress.title}</h1>
	<div class="mb-4 flex flex-row items-center gap-2">
		<progress class="progress progress-primary h-9 w-72" value={latestProgress} max={100}
		></progress>
		<div class="text-sm font-bold text-black">{latestProgress}%</div>
	</div>
	<LineChart
		title={'Progress over days'}
		plotId={progressPlotId}
		xaxis="Date"
		yaxis="Progression (%)"
		displayXAxisGap={5}
		x={longTermProgressData.map((data) => data.date)}
		y={longTermProgressData.map((data) => data.totalProgress)}
		yRange={[0, 100]}
	/>
	<div class="mt-2 text-lg text-gray-600">
		<p>Current Rate: {shortTermProgressAverage.toFixed(2)}%</p>
		<p>Days to Complete: {Math.ceil(daysToComplete)}</p>
	</div>
</div>
