FROM python:3.11
ENV PYTHONBUFFERED 1
ENV APP_HOME /app 
WORKDIR $APP_HOME
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./
CMD ["python", "bucket_clean.py"]
