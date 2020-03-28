FROM python:alpine
WORKDIR /app
COPY requirements.txt .
COPY . /app
RUN pip install -r requirements.txt
ENV FLASK_APP /app/app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]