FROM python:3.10

WORKDIR /app

COPY requirements/app.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src /app

EXPOSE 8000

CMD ["python", "main.py"]