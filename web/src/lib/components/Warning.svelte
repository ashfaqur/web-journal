<script lang="ts">
	interface Props {
		text: string;
	}
	let { text }: Props = $props();
</script>

<div class="mb-1 mt-1 min-w-full rounded bg-yellow-200 px-4 py-2 text-center">
	<p class="text-yellow-900">{text}</p>
</div>
