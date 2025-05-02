<script lang="ts">
	import { onMount } from 'svelte';
	import { serverHealthCheck } from '$lib/api';

	let isServerRunning: boolean = $state(true);

	onMount(async () => {
		isServerRunning = await serverHealthCheck();
	});
</script>

<!-- Infomation panel saying the data is mock when server inactive -->
{#if !isServerRunning}
	<div class="mb-4 rounded bg-yellow-200 px-4 py-2 text-center">
		<p class="text-yellow-900">Server is not reachable. Showing mock data.</p>
	</div>
{/if}
