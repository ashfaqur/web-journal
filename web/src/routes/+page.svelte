<script lang="ts">
	import { onMount } from 'svelte';
	import { flip } from 'svelte/animate';
	import { serverAddress } from '$lib/constants';

	onMount(() => {
		fetch(`${serverAddress}/ping`)
			.then((response) => {
				if (response.ok) {
					console.log('Server is running');
				} else {
					console.error('Server is not running');
				}
			})
			.catch((error) => {
				console.error('Server not reachable. Network error');
			});
	});
	const options = {};
</script>

<div class="m-4 grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
	<!-- Link buttons for different website's pages -->
	<a href="/lastdays" class="btn border-green-400 bg-green-300 hover:bg-green-500">Last Days</a>
	<a href="/lastweeks" class="btn border-green-400 bg-green-300 hover:bg-green-500">Last Weeks</a>
</div>
