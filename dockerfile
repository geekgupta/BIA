FROM python:alpine3.10

RUN apk update && apk upgrade

# Install necessary packages
RUN apk add --no-cache \
    wget \
    ca-certificates \
    curl \
    git \
    gnupg \
    gcc \
    musl-dev \
    libffi-dev \
    libressl-dev \
    libldap \
    libsasl \
    postgresql-dev \
    sudo

RUN  apk install imagemagick


# Clean up package cache
RUN rm -rf /var/cache/apk/*

WORKDIR /backend
COPY requirements.txt /backend/


RUN chmod +x entrypoint.sh && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install tzdata

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install -r requirements.txt && pip install tzdata
COPY . /backend/

EXPOSE 8000

# ENTRYPOINT  ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
