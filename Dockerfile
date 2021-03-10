FROM python:3.6

COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY dummy_webhook_server.py .
CMD [ "python3", "dummy_webhook_server.py" ]