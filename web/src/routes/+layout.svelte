<script lang="ts">
	import '../app.css';
	import WarnServerInactive from '$lib/components/WarnServerInactive.svelte';
	let { children } = $props();
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-2">
		<a href="/" class="text-3xl font-bold">Journal</a>
	</div>
</section>

<section>
	<WarnServerInactive />
</section>
{@render children()}
