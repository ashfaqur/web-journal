<script lang="ts">
	import 'tailwindcss/tailwind.css';
	let { children } = $props();
</script>

<!-- Header -->
<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-2">
		<h2 class="text-3xl font-bold">Journal</h2>
	</div>
</section>
{@render children()}
