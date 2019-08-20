FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY Consumer.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./Consumer.py" ]