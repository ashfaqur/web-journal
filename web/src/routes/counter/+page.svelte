<script lang="ts">
	import { onMount } from 'svelte';

	const title = 'Counter';

	onMount(async () => {
		// const result = await processLastDaysData(days);
	});
</script>

<!-- Title -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>
