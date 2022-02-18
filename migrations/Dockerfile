FROM python:3.9-slim
ENV DB_ADAPTER=mysql+mysqlconnector
ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_USERNAME=user
ENV DB_PASSWORD=password
ENV DB_NAME=mysql
WORKDIR /migrations
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["alembic", "upgrade", "head"]