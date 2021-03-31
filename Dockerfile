# Dockerfile, Image, Container
FROM python:3.8.3

ADD main.py . 
ADD settings.py .
ADD .env .

RUN pip install twitchio python-dotenv

CMD [ "python3", "main.py" ]
