import type Counter from '$lib/components/Counter.svelte';

export type FetchProgressResult = {
	data: ProgressObj[];
	isFallback: boolean;
};

export type ProgressObj = {
	title: string;
	count: number;
	progress: number;
	data: ProgressData[];
	color?: string = cssColorNames[Math.floor(Math.random() * cssColorNames.length)];
};

export type ProgressData = {
	date: string;
	progress: number;
};

export type DayPoints = {
	date: string;
	state: 'Complete' | 'Incomplete' | 'None';
	points: number;
};

export type FetchLastDaysResult = {
	data: DayPoints[];
	isFallback: boolean;
};

export type FetchCounterDataResult = {
	data: CounterDataDict;
	isFallback: boolean;
};

export type CounterDataDict = {
	[name: string]: DayCounts[];
};

export type DayCounts = {
	date: string;
	count: number;
};

export type FetchCounterCumulativeResult = {
	data: CounterCumulativeTuple[];
	isFallback: boolean;
};

export type CounterCumulativeTuple = [string, string, number];
