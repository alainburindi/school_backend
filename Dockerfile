  
# specify a base image
FROM ubuntu:latest


LABEL version="1.0"
LABEL maintainer="olumide ogundele <alainburindi62@gmail.com>"
LABEL project.name="school"

# set environment variables
ENV PYTHONUNBUFFERED 1


# set the current directory to build the app
WORKDIR /usr/school

# install the dependencies required to run the app
RUN apt-get update  -y && apt-get install -y \
    libpq-dev \
    python3-pip -y

RUN pip3 install psycopg2 gunicorn

# copy the file containing the app dependencies
COPY ./requirements.txt ./

# install all the dependencies
RUN pip3 install -r requirements.txt

# copy the remaining project
COPY ./ ./