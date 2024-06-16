FROM python:3.11-slim
ENV PYTHONBUFFERED True
ENV APP_HOME /app 
WORKDIR $APP_HOME
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ['/app/bucket_clean.py']
