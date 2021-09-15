# docker build -t custom_exporter .
FROM alpine:3.14
WORKDIR /app
COPY ./custom_exporter.py /app
RUN apk update; apk add py-pip; pip install prometheus_client
EXPOSE 8080
CMD python3 ./custom_exporter.py
