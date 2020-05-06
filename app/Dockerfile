FROM python:alpine
WORKDIR /app
COPY requirements.txt .
COPY . /app
RUN pip install -r requirements.txt
ENV FLASK_APP /app/app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=15s --timeout=2s --retries=2 --start-period=15s CMD curl -f http://localhost/api/blabs || exit 1