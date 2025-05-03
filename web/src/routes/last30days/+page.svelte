<script lang="ts">
	import LastDays from '$lib/components/LastDays.svelte';

	const days = 30;
</script>

<LastDays title={`Last ${days} Days`} {days} />
