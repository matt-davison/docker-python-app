FROM python:alpine

COPY requirements.txt .
COPY . /app
RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py
WORKDIR /app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]