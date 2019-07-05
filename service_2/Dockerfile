FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app
ENV FLASK_APP=app.py
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5002
RUN chmod 644 app.py
CMD gunicorn -b 0.0.0.0:5002 app:app