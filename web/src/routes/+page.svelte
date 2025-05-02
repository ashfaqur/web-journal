<script lang="ts">
	import { onMount } from 'svelte';
	import { serverAddress } from '$lib/constants';

	let isServerRunning = $state(true);

	onMount(() => {
		fetch(`${serverAddress}/health`)
			.then((response) => {
				if (response.ok) {
					console.log('Server is running');
				} else {
					console.error('Server is not running');
					isServerRunning = false;
				}
			})
			.catch((error) => {
				console.error('Server not reachable. Network error');
				isServerRunning = false;
			});
	});
	const options = {};
</script>

<div class="w-full">
	{#if !isServerRunning}
		<!-- Warning panel saying the data is mock -->
		<div class="mb-4 rounded bg-yellow-200 px-4 py-2 text-center">
			<p class="text-yellow-900">Server not reachable. Data is mock</p>
		</div>
	{/if}
</div>

<div class="m-4 grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
	<!-- Link buttons for different website's pages -->
	<a href="/last7days" class="btn border-green-400 bg-green-300 hover:bg-green-500">Last 7 Days</a>
	<a href="/last30days" class="btn border-green-400 bg-green-300 hover:bg-green-500">Last 30 Days</a
	>
</div>
