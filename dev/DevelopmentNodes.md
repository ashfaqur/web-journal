# Dev Notes

Set the path to the sqlite database:

    export JOURNAL_DATABASE_PATH=/home/ash/journal.db

Run the sever:

    uvicorn main:app --host 0.0.0.0 --port 8181 --reload

Run the front end

    npm run dev

## Deployment

PI has a hard time building the web frontend,
so build it on PC then upload the build artifacts to the repository,
then deploy it to the PI.

Note to change the server address to the PI address before building:

    export const serverAddress = 'http://0.0.0.0:8181';

Nginx setup script:

    /etc/nginx/sites-available/default


All these issues can easily be solved by Docker...
