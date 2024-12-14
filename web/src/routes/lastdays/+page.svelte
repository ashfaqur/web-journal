<script lang="ts">
	import PlotBar from '$lib/components/PlotBar.svelte';
	import { onMount } from 'svelte';

	const title = 'Points in last 30 Days';
	const xaxis = 'Date';
	const yaxis = 'Points';
	let x: string[] = $state([]);
	let y: number[] = $state([]);
	$inspect(x);
	$inspect(y);

	// Fetch data when the component is mounted
	onMount(async () => {
		try {
			const response = await fetch('http://localhost:8181/last30days');
			if (!response.ok) {
				throw new Error('Failed to fetch data');
			}
			const data = await response.json();
			console.log('Data:', data);
			x = data.map((entry: { date: string }) => entry.date);
			y = data.map((entry: { points: number }) => entry.points);
		} catch (error) {
			console.error('Error fetching data:', error);
		}
	});
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-600 px-6 py-2">
		<h2 class="text-3xl font-bold">Last 30 Days</h2>
	</div>
</section>

<!-- Graph -->
<section><PlotBar {title} {xaxis} {yaxis} {x} {y} /></section>
