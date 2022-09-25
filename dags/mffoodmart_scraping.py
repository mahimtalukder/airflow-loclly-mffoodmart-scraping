from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from random import randint
from datetime import datetime

from subprocess import check_output

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


def _training_model():
    return randint(1, 10)

with DAG("scaping_task", start_date=datetime(2021, 1, 1),
    schedule_interval="@daily", catchup=False) as dag:

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