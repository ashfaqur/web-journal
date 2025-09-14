<script lang="ts">
	interface Props {
		title: string;
	}
	let { title }: Props = $props();
</script>

<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
	<h3 class="text-2xl">{title}</h3>
</div>
