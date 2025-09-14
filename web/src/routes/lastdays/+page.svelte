<script lang="ts">
	const title = 'Last Days';

	const dayOptions = [7, 30, 90];
	let selectedDays = 7;
</script>

<section>
	<div class="container flex min-w-full items-center justify-center bg-green-400 px-6 py-1">
		<h3 class="text-2xl">{title}</h3>
	</div>
</section>

<!-- Button Group to choose range of day options -->

<div class="container my-4 flex justify-center">
	<div class="btn-group space-x-1">
		{#each dayOptions as option}
			<button
				class="btn btn-outline btn-primary {selectedDays === option ? 'btn-active' : ''}"
				onclick={() => (selectedDays = option)}
			>
				{option} Days
			</button>
		{/each}
	</div>
</div>
<!-- Last days bar plot showing points earned -->

<!-- Last days pie chart showing percentage of days with activity -->

<!-- Habits heat map over days and activitites -->
