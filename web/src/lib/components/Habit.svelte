<script lang="ts">
	import HeatMap from '$lib/components/plot/HeatMap.svelte';
	import Warning from '$lib/components/Warning.svelte';

	import { fetchHabitData } from '$lib/api';
	import { datesToDays } from '$lib/util';
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
		const habitObjs: HabitObj[] = habitData.data.reverse(); // show first ones at the top
		fallback = habitData.isFallback;
		// Capitalize the first letter
		yValues = habitObjs.map((habit: HabitObj) =>
			habit.name
				.split(' ')
				.map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
				.join(' ')
		);

		if (habitObjs.length > 0) {
			// Get sorted dates from the first habit
			const dates = Object.keys(habitObjs[0].data).sort((a, b) => a.localeCompare(b));

			// Show day for week and dates for month visualization
			if (dates.length > 7) {
				xValues = dates;
			} else {
				// Compute day-of-week labels (short, e.g., Mon, Tue)
				xValues = datesToDays(dates);
			}

			// Map each habit to its values in the same order
			zValues = habitObjs.map(
				(obj) => dates.map((date) => obj.data[date] ?? 0) // fallback 0 if missing
			);
		}
	}

	$effect(() => {
		// Calculate time taken to fetch data
		const start = performance.now();
		fetchData();
		const end = performance.now();
		console.debug(`Time to fetch habit data: ${end - start} ms`);
	});
</script>

{#if fallback}
	<Warning text="Showing mock data due to fetch error" />
{/if}

<HeatMap title="Habits" {xValues} {yValues} {zValues} />
