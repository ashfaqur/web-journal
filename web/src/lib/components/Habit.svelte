<script lang="ts">
	import HeatMap from '$lib/components/plot/HeatMap.svelte';
	import Warning from '$lib/components/Warning.svelte';

	import { fetchHabitData } from '$lib/api';
	import type { FetchHabitResult, HabitObj } from '$lib/types/response';

	interface Props {
		days: number;
	}
	let { days }: Props = $props();
	let fallback: boolean = $state(false);
	let xValues: string[] = $state([]);
	let yValues: string[] = $state([]);
	let zValues: number[][] = $state([]);

	async function fetchData() {
		const habitData: FetchHabitResult = await fetchHabitData(days);
		console.log('Habit data loaded:', habitData);
		const habitObjs: HabitObj[] = habitData.data;
		fallback = habitData.isFallback;
		yValues = habitObjs.map(
			(obj) => obj.name.charAt(0).toUpperCase() + obj.name.slice(1).toLowerCase()
		);
		if (habitObjs.length > 0) {
			// Get sorted dates from the first habit
			xValues = Object.keys(habitObjs[0].data).sort((a, b) => a.localeCompare(b));

			// Map each habit to its values in the same order
			zValues = habitObjs.map(
				(obj) => xValues.map((date) => obj.data[date] ?? 0) // fallback 0 if missing
			);
		}
	}

	$effect(() => {
		fetchData();
	});
</script>

{#if fallback}
	<Warning text="Showing mock data due to fetch error" />
{/if}

<HeatMap title="Habit" {xValues} {yValues} {zValues} />
