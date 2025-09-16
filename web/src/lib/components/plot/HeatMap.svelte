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
		[0.5, 'rgb(235, 242, 237)'],
		[1, 'rgb(15, 163, 2)'] // green for positive values
	];

	const ROW_HEIGHT_LG = 100; // pixels per row
	const ROW_HEIGHT_SM = 55;
	const MARGIN_HEIGHT = 100;

	const zMin = -10;
	const zMax = 10;

	let rowHeight = $derived(xValues.length > 10 ? ROW_HEIGHT_SM : ROW_HEIGHT_LG);

	let data: any = $derived([
		{
			x: xValues,
			y: yValues,
			z: zValues,
			type: 'heatmap',
			colorscale: colorscaleValue,
			zmin: zMin,
			zmax: zMax,
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
		// width: 600,
		height: yValues.length * rowHeight + MARGIN_HEIGHT,
		autosize: false,
		plot_bgcolor: '#000000' // black border color
	});

	const config = { responsive: true };

	$effect(() => {
		Plotly.newPlot(plotId, data, layout, config);
	});
</script>

<div id={plotId}></div>
