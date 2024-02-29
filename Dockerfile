FROM python:3.10-slim

COPY requirements.txt main.py .

RUN pip install -r requirements.txt

CMD ["python", "/main.py"]