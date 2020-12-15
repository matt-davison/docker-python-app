FROM python:alpine
WORKDIR /app
#COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
RUN apk add curl
ENV FLASK_APP /app/app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=15s --timeout=2s --retries=2 --start-period=15s CMD curl -f http://localhost:5000/blabs?createdSince=0 || exit 1