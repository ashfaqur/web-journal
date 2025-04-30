export type DayPoints = {
    date: string;
    state: 'Complete' | 'Incomplete' | 'None';
    points: number;
};

export type FetchLastDaysResult = {
    data: DayPoints[];
    isFallback: boolean;
};
