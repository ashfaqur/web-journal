import { serverAddress } from '$lib/constants';
import { last30DaysStub } from '$lib/stubs/lastThirtyDays';
import type { DayPoints, FetchLastDaysResult } from '$lib/types/response';


export async function fetchLastThirtyDays(): Promise<FetchLastDaysResult> {
    try {
        console.log('Fetching last 30 days from server:', serverAddress);
        const response = await fetch(`${serverAddress}/last30days`);

        if (!response.ok) {
            console.warn('Response not OK, falling back to stub data');
            return { data: last30DaysStub, isFallback: true };
        }

        const data = await response.json();
        if (!isDayPoints(data)) {
            console.warn('Data format invalid, falling back to stub');
            return { data: last30DaysStub, isFallback: true };
        }
        return { data: data, isFallback: false };
    } catch (error) {
        console.error('Network error fetching last 30 days:', error);
        console.log('Falling back to stub data after fetch error');
        return { data: last30DaysStub, isFallback: true };
    }
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

function isDayPoints(data: unknown): data is DayPoints[] {
    return Array.isArray(data) && data.every(item =>
        typeof item.date === 'string' &&
        typeof item.state === 'string' &&
        typeof item.points === 'number'
    );
}

export async function serverHealthCheck(): Promise<boolean> {
    return fetch(`${serverAddress}/health`)
        .then(response => response.ok)
        .catch(() => false);
}

