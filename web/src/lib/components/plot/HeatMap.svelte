<script lang="ts">
	import Plotly from 'plotly.js-dist-min';

	interface Props {
		title: string;
		xValues: string[];
		yValues: string[];
		zValues: number[][];
		plotId?: string;
	}

	let { title, xValues, yValues, zValues, plotId = 'heatmap' }: Props = $props();

	const colorscaleValue = [
		[0, 'rgb(148, 7, 7)'], // red for negative values
		[0.5, 'rgb(255,255,255)'], // white for zero
		[1, 'rgb(4, 102, 21)'] // green for positive values
	];

	const ROW_HEIGHT = 100; // pixels per row
	const MARGIN_HEIGHT = 100; // for title, labels, padding etc.

	let data: any = $derived([
		{
			x: xValues,
			y: yValues,
			z: zValues,
			type: 'heatmap',
			colorscale: colorscaleValue,
			showscale: false
		}
	]);

	let layout: any = $derived({
		title: { text: title, font: { size: 20 } },
		annotations: [],
		xaxis: { ticks: '', side: 'top' },
		yaxis: {
			ticks: '',
			ticksuffix: ' '
		},
		width: 600,
		height: yValues.length * ROW_HEIGHT + MARGIN_HEIGHT,
		autosize: false,
		plot_bgcolor: '#000000' // black border color
	});

	const config = { responsive: true };

	$effect(() => {
		Plotly.newPlot(plotId, data, layout, config);
	});
</script>

<div id={plotId}></div>
