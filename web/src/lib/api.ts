import { serverAddress } from '$lib/constants';
import { last30DaysStub } from '$lib/stubs/lastThirtyDays';
import type {
	DayPoints,
	FetchLastDaysResult,
	FetchCounterDataResult,
	FetchCounterCumulativeResult
} from '$lib/types/response';
import { isDayPoints, isCounterData, isCounterCumulativeData } from '$lib/util';

export async function fetchCounterData(days: number): Promise<FetchCounterDataResult> {
	console.log(`Fetching last ${days} days counter data from server:`, serverAddress);
	const response = await fetch(`${serverAddress}/count/${days}`);
	const data = await response.json();
	if (!isCounterData(data)) {
		console.warn('Data format invalid, falling back to stub');
		return { data: {}, isFallback: true };
	}
	return { data: data, isFallback: false };
}

export async function fetchCounterCumulativeData(
	counter_name: string,
	days: number
): Promise<FetchCounterCumulativeResult> {
	console.log(`Fetching last ${days} days counter data from server:`, serverAddress);
	const response = await fetch(
		`${serverAddress}/counter_total/${encodeURIComponent(counter_name)}/${days}`
	);
	const data = await response.json();
	if (!isCounterCumulativeData(data)) {
		console.warn('Data format invalid, falling back to stub');
		return { data: [], isFallback: true };
	}
	return { data: data, isFallback: false };
}

export async function fetchLastDays(days: number): Promise<FetchLastDaysResult> {
	const stub_data: DayPoints[] = last30DaysStub.slice(0, days);
	try {
		console.log(`Fetching last ${days} days from server:`, serverAddress);
		const response = await fetch(`${serverAddress}/lastdays/${days}`);

		if (!response.ok) {
			console.warn('Response not OK, falling back to stub data');
			return { data: stub_data, isFallback: true };
		}

		const data = await response.json();
		if (!isDayPoints(data)) {
			console.warn('Data format invalid, falling back to stub');
			return { data: stub_data, isFallback: true };
		}
		return { data: data, isFallback: false };
	} catch (error) {
		console.error('Network error fetching last 30 days:', error);
		console.log('Falling back to stub data after fetch error');
		return { data: stub_data, isFallback: true };
	}
}

export async function serverHealthCheck(): Promise<boolean> {
	return fetch(`${serverAddress}/health`)
		.then((response) => response.ok)
		.catch(() => false);
}
