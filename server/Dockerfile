FROM python:latest
WORKDIR /server
COPY requirements.txt /server
RUN pip3 install -r requirements.txt --no-cache-dir
COPY server.py /server
COPY data.csv /server
ENTRYPOINT ["python3"]
CMD ["server.py"]
