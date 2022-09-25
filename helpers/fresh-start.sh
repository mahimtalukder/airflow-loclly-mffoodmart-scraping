echo AIRFLOW_HOME is set as $AIRFLOW_HOME 
airflow db init

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org