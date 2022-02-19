FROM python:3.9-slim
WORKDIR /etl
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "start.py"]