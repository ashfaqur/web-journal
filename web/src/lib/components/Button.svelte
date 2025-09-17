<script lang="ts">
	interface Props {
		text: string;
		selected: boolean;
		onclick: () => void;
	}

	let { text, selected, onclick }: Props = $props();
</script>

<button
	class="btn border-green-400 hover:bg-green-500 {selected ? 'bg-green-500' : 'bg-green-300'} "
	{onclick}
>
	{text} Days
</button>
