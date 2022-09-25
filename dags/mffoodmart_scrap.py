from datetime import datetime, timedelta
import time
from airflow import DAG
from airflow.operators.python import PythonOperator

from subprocess import check_output



default_args = {
    'owner': 'clickSpikes',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def scrap():
    scrap_mess = check_output(['npm', 'start'])
    print (scrap_mess)

def update_category_dims():
    db_push_message = check_output(['npm', 'run','updateCategoryDim'])
    print (db_push_message)


def upload_product_dims():
    db_push_message = check_output(['npm', 'run','updateProductDim'])
    print (db_push_message)

def upload_product_categories_dims():
    db_push_message = check_output(['npm', 'run','updateProductCategoriesDim'])
    print (db_push_message)

def upload_fatcs():
    db_push_message = check_output(['npm', 'run','uploadProductFact'])
    print (db_push_message)

 
with DAG(
    dag_id = "mffoodmart_scrap_v2",
    default_args = default_args,
    description = "Scraping task of mffoodmart.com",
    start_date = datetime(2022, 9, 16, 1),
    schedule_interval = "@daily"
) as dag:

    mffoodmart_scrap = PythonOperator(
        task_id='mffoodmart_scrap',
        python_callable=scrap
    )


    mffoodmart_category_dim_upgrade = PythonOperator(
        task_id='mffoodmart_category_dim_upgrade',
        python_callable=update_category_dims
    )


    mffoodmart_product_dim_upgrade = PythonOperator(
        task_id='mffoodmart_product_dim_upgrade',
        python_callable=upload_product_dims
    )


    mffoodmart_product_categories_dim_upgrade = PythonOperator(
        task_id='mffoodmart_product_categories_dim_upgrade',
        python_callable=upload_product_categories_dims
    )

    mffoodmart_fact_upload = PythonOperator(
        task_id='mffoodmart_fact_upload',
        python_callable=upload_fatcs
    )


    mffoodmart_scrap >> [mffoodmart_category_dim_upgrade, mffoodmart_product_dim_upgrade] >> mffoodmart_product_categories_dim_upgrade >> mffoodmart_fact_upload
