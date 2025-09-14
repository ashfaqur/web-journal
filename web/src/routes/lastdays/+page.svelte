<script lang="ts">
	import PageTitle from '$lib/components/PageTitle.svelte';
	import Button from '$lib/components/Button.svelte';
	import Habit from '$lib/components/Habit.svelte';

	const title: string = 'Last Days';

	const dayOptions: number[] = [7, 30];
	let selectedDayOption: number = $state(dayOptions[0]);
</script>

<div class="container flex min-w-full flex-col items-center">
	<PageTitle {title} />

	<!-- Button Group to choose range of day options -->
	<div class="btn-group mt-1 space-x-1">
		{#each dayOptions as option}
			<Button
				text={option.toString()}
				selected={selectedDayOption === option}
				onclick={() => (selectedDayOption = option)}
			/>
		{/each}
	</div>

	<!-- Habits heat map over days and activitites -->
	<Habit days={selectedDayOption} />
</div>
