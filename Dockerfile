FROM python:3.8

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
# RUN pip install -U pip setuptools

RUN apt-get install python3.8-dev
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]