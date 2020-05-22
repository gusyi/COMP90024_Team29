# Parent image
FROM python:3.7.3

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
        build-essential \
        git \
        curl \
        vim \
        nginx \
        nodejs \
        npm \
        wget \
        ca-certificates \
        python3-pip \
        python3-dev \
        libpq-dev
        
RUN mkdir /app
WORKDIR /app
ADD . /app

# pip install required packages listed in dependencies.txt
RUN pip install --trusted-host pypi.python.org -r dependencies.txt

EXPOSE 8080
CMD [ "python","manage.py","runserver","0.0.0.0:8080" ]