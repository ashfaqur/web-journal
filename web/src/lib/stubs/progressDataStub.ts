import type { ProgressObj } from '$lib/types/response';

export const progressStub: ProgressObj[] = [
	{
		title: 'Exercise',
		count: 3,
		progress: 80,
		color: 'green',
		data: [
			{ date: '2025-09-01', progress: 70 },
			{ date: '2025-09-02', progress: 90 },
			{ date: '2025-09-03', progress: 80 }
		]
	},
	{
		title: 'Meditation',
		count: 3,
		progress: 60,
		color: 'blue',
		data: [
			{ date: '2025-09-01', progress: 50 },
			{ date: '2025-09-02', progress: 70 },
			{ date: '2025-09-03', progress: 60 }
		]
	},
	{
		title: 'Reading',
		count: 3,
		progress: 100,
		color: 'orange',
		data: [
			{ date: '2025-09-01', progress: 100 },
			{ date: '2025-09-02', progress: 100 },
			{ date: '2025-09-03', progress: 100 }
		]
	}
];
