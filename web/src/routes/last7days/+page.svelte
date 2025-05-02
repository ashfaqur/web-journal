<script lang="ts">
	import LastDays from '$lib/components/LastDays.svelte';

	const days = 7;
</script>

<LastDays title={`Last ${days} Days`} {days} />
