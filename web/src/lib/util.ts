import type { DayPoints, FetchLastDaysResult, ProgressObj } from '$lib/types/response';
import { fetchLastDays } from '$lib/api';
import { cssColorNames } from '$lib/constants';
import type { CounterCumulativeTuple, CounterDataDict } from '$lib/types/response';

export async function processLastDaysData(days: number): Promise<{
	dates: string[];
	points: number[];
	states: string[];
	stateCounts: Map<string, number>;
	fallback: boolean;
}> {
	const result: FetchLastDaysResult = await fetchLastDays(days);
	const data: DayPoints[] = result.data;
	const fallback = result.isFallback;

	const dates = data.map((entry: DayPoints) => entry.date);
	const points = data.map((entry: DayPoints) => entry.points);
	const states = data.map((entry: DayPoints) => entry.state);

	let stateCounts = new Map<string, number>();
	states.forEach((state) => {
		stateCounts.set(state, (stateCounts.get(state) || 0) + 1);
	});
	stateCounts.forEach((value, key) => {
		if (value !== 0) {
			stateCounts.set(key, Math.round((value * 100) / states.length));
		}
	});

	return {
		dates,
		points,
		states,
		stateCounts,
		fallback
	};
}

export function isValidPlotlyColor(color: string): boolean {
	// Check for named color
	if (cssColorNames.includes(color.toLowerCase())) return true;
	// Check for hex code
	if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(color)) return true;
	// Check for rgb/rgba/hsl/hsla
	if (/^rgb(a)?\((\s*\d+\s*,){2,3}\s*\d+\s*\)$/.test(color)) return true;
	if (/^hsl(a)?\(\s*\d+\s*,\s*\d+%?,\s*\d+%?\s*(,\s*\d+(\.\d+)?\s*)?\)$/.test(color)) return true;
	return false;
}

export function dateToDDMM(date: string): string {
	// Check if the date is in YYYY-MM-DD format
	if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) {
		return date;
	}
	const [year, month, day] = date.split('-');
	return `${day}/${month}`;
}

export function isCounterData(data: unknown): data is CounterDataDict {
	return (
		data !== null &&
		typeof data === 'object' &&
		!Array.isArray(data) &&
		Object.values(data).every(
			(array) =>
				Array.isArray(array) &&
				array.every(
					(item) =>
						typeof item === 'object' &&
						item !== null &&
						'date' in item &&
						typeof item.date === 'string' &&
						'count' in item &&
						typeof item.count === 'number'
				)
		)
	);
}

export function isCounterCumulativeData(data: unknown): data is CounterCumulativeTuple[] {
	return (
		Array.isArray(data) &&
		data.every(
			(item) =>
				Array.isArray(item) &&
				item.length === 3 &&
				typeof item[0] === 'string' &&
				typeof item[1] === 'string' &&
				typeof item[2] === 'number'
		)
	);
}

export function isDayPoints(data: unknown): data is DayPoints[] {
	return (
		Array.isArray(data) &&
		data.every(
			(item) =>
				typeof item.date === 'string' &&
				typeof item.state === 'string' &&
				typeof item.points === 'number'
		)
	);
}

export function isProgressObj(data: unknown): data is ProgressObj[] {
	return (
		Array.isArray(data) &&
		data.every(
			(item) =>
				typeof item.title === 'string' &&
				typeof item.count === 'number' &&
				typeof item.progress === 'number' &&
				Array.isArray(item.data) &&
				item.data.every(
					(subItem) => typeof subItem.date === 'string' && typeof subItem.progress === 'number'
				)
		)
	);
}
