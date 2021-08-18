FROM python:3.8
LABEL maintainer="Sam Gabrail"
WORKDIR /app
COPY . /app
RUN apt-get update && pip install -r requirements.txt
CMD [ "python", "-u", "main.py" ]