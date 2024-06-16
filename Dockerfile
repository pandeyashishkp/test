FROM python:3.11-slim
ENV PYTHONBUFFERED 1
ENV APP_HOME /app 
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt
CMD ['python', 'bucket_clean.py']
