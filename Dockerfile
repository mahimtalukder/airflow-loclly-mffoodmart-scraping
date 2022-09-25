FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt install python3-pip -y
RUN pip install apache-airflow[celery]==2.3.4 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.4/constraints-3.7.txt"
RUN export AIRFLOW_HOME=$(pwd) 
RUN echo AIRFLOW_HOME is set as $AIRFLOW_HOME 
RUN airflow db init
COPY . ./
#RUN ./create_user.sh

EXPOSE 3000
CMD ["/bin/bash", "-c", "airflow scheduler;airflow webserver --port 3000"]
