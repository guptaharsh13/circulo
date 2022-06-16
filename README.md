# círculo

Backend Assignment | FamPay

## About the Backend

To provide an API to retrieve the most recent videos from YouTube, arranged in reverse chronological order of their posting date-time, in a paginated response for a particular tag/search query.

## Tech Stack

- Python3.8
- Django
- Django Rest Framework
- Celery
- PostgreSQL
- Docker

## Getting Started

To get started:

- Clone the repo.

```shell
git clone https://github.com/guptaharsh13/circulo
```

- Change into the directory.

```shell
cd circulo
```

### Run

#### Environment Variables

```shell
touch .env
```

**For running this project successfully you'll need to create a `.env` file and store your firebase credentials there like [`.env.sample`](https://github.com/guptaharsh13/circulo/tree/master/.env.sample).**

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

Open a new temminal and start the celery worker

```shell
celery -A circulo.celery worker -l INFO
```

Open another temminal and start the celery beat scheduler

```shell
celery -A circulo beat -l INFO
```

### Docker Run

#### Environment Variables

```shell
touch .env
```

**For running this project successfully you'll need to create a `.env` file and store your firebase credentials there like [`.env.sample.docker`](https://github.com/guptaharsh13/circulo/tree/master/.env.sample.docker).**

```shell
docker-compose up --build
```

## API Documentation

- [Swagger](http://localhost:8000/swagger/)
- [Redoc](http://localhost:8000/redoc/)

## Inspirations

- [Why did I use BRIN index for published_on and made_on?](https://medium.com/geekculture/postgres-brin-index-large-data-performance-with-minimal-storage-4db6b9f64ca4)
- [Why did I use Cursor Pagination?](https://uxdesign.cc/why-facebook-says-cursor-pagination-is-the-greatest-d6b98d86b6c0)

## Future Scope

- Build a TUI
- [Implement Elasticsearch](https://github.com/guptaharsh13/circulo/tree/feat-%2322)

<p align="center">Made with ❤ by Harsh Gupta</p>
