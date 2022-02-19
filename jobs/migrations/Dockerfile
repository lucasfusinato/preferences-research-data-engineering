FROM python:3.9-slim
WORKDIR /migrations
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["alembic", "upgrade", "head"]