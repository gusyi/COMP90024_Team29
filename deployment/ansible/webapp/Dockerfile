# Use an official Python runtime as a parent image
FROM python:3.7.3

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000

RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
        build-essential \
        cmake \
        git \
        curl \
        vim \
        wget \
        ca-certificates \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Set working directory
WORKDIR /home/ubuntu/

# Copy the current directory contents into the container
COPY ./backend /home/ubuntu/
COPY ./startserver.sh /home/ubuntu/startserver.sh


# Expose port 8080
EXPOSE 8080

# Run manage.py when the container launches
CMD [ "python","manage.py","runserver","0.0.0.0:8080" ]