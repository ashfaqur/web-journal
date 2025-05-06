
import type { DayPoints, FetchLastDaysResult } from '$lib/types/response';
import { fetchLastDays } from '$lib/api';

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