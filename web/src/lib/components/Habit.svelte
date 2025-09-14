<script lang="ts">
	import HeatMap from '$lib/components/plot/HeatMap.svelte';

	import { fetchHabitData } from '$lib/api';
	import type { FetchHabitResult, HabitObj } from '$lib/types/response';

	interface Props {
		days: number;
	}
	let { days }: Props = $props();
	let xValues: string[] = $state([]);
	let yValues: string[] = $state([]);
	let zValues: number[][] = $state([]);

	async function fetchData() {
		const habitData: FetchHabitResult = await fetchHabitData(days);
		console.log('Habit data loaded:', habitData);
		const habitObjs: HabitObj[] = habitData.data;
		yValues = habitObjs.map((obj) => obj.name);
		xValues = habitObjs[0].data.map((item) => item.date);
		zValues = habitObjs.map((obj) => obj.data.map((item) => item.value));
	}

	$effect(() => {
		fetchData();
	});
</script>

<HeatMap title="Habit" {xValues} {yValues} {zValues} />
