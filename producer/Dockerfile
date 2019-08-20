FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY Producer.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./Producer.py" ]