import type Counter from '$lib/components/Counter.svelte';

export type FetchHabitResult = {
	data: HabitObj[];
	isFallback: boolean;
};

export type HabitObj = {
	name: string;
	data: Record<string, number>; // key = date, value = intensity
};

export type FetchProgressResult = {
	data: ProgressObj[];
	isFallback: boolean;
};

type RawProgressData = Record<string, [string, number, number][]>;

export type ProgressObj = {
	title: string;
	data: ProgressData[];
};

export type ProgressData = {
	date: string;
	totalProgress: number;
	dailyProgress: number;
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
