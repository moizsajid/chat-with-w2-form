FROM python:3.11-slim

RUN apt-get -y update
# RUN apt-get install -y libpoppler-dev
RUN apt-get install -y poppler-utils

# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# set working directory
WORKDIR /usr/src/app

RUN echo $(ls -1)

# disables lag in stdout/stderr output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN ls

COPY ./ /usr/src/app

# Run streamlit
CMD streamlit run app.py
