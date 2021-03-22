# Dockerfile, Image, Container
FROM python:3.8.3

ADD main.py . 
ADD settings.py .

RUN pip install twitchio python-dotenv

CMD [ "python", " ./main.py" ]
