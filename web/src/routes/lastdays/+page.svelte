<script lang="ts">
	import PlotBar from '$lib/components/PlotBar.svelte';

	const title = 'Points in last 30 Days';
	const xaxis = 'Date';
	const yaxis = 'Points';
	const x = ['1/12', '2/12'];
	const y = [10, 12];
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-600 px-6 py-2">
		<h2 class="text-3xl font-bold">Last 30 Days</h2>
	</div>
</section>

<!-- Graph -->
<section><PlotBar {title} {xaxis} {yaxis} {x} {y} /></section>
