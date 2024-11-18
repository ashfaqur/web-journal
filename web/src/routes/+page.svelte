<script lang="ts">
	async function buttonAction() {
		console.log('buttonAction');
		try {
			const response = await fetch('http://localhost:8181/items');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const data = await response.json();
			console.log('Data:', data);
		} catch (error) {
			console.error('Fetch error:', error);
		}
	}
</script>

<h2 class="card-title">Hello World</h2>

<button class="btn btn-primary" onclick={buttonAction}>Button</button>
