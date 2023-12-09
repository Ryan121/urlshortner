FROM python:3.10-slim-bookworm

WORKDIR /app

COPY ./urlshortner .

COPY ./requirements.txt requirements.txt

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
