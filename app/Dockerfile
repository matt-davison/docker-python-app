FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]