import type Counter from '$lib/components/Counter.svelte';
import type { an } from 'vitest/dist/chunks/reporters.D7Jzd9GS.js';

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
