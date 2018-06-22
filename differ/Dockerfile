FROM python:3.6 as dev
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN mkdir src logs repo static

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn==19.8.1

COPY . /app/src

COPY docker-entrypoint.sh /app
EXPOSE 8000
WORKDIR /app/src
ENTRYPOINT ["/app/docker-entrypoint.sh"]
