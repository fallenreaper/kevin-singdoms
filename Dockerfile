
# Python Flask App
from centos:latest
COPY python/ /home/python/.
RUN yum update -y
RUN yum install -y python3 postgresql-devel python3-devel gcc 
RUN pip3 install -r /home/python/requirements.txt
WORKDIR /home/python
CMD python3 app.py

# Postgres DB Docker Image.  Just need to expose port 5432 to host:  `-p 5432:5432`
#FROM postgres:latest
#ENV POSTGRES_PASSWORD moondbpassword 
#COPY python/db.sql /docker-entrypoint-initdb.d/db.sql
