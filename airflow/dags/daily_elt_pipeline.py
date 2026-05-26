from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

default_args = {
    "owner": "data-team",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["data-oncall@company.com"],
}

with DAG(
    dag_id="daily_elt_pipeline",
    default_args=default_args,
    schedule_interval="0 17 * * *",  # UTC 17:00 = KST 02:00
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["elt", "production"],
) as dag:
    extract = PythonOperator(task_id="extract_from_rds", python_callable=extract_fn)
    transform = PythonOperator(task_id="transform_upload_s3", python_callable=transform_fn)
    load = PythonOperator(task_id="load_to_redshift", python_callable=load_fn)
    notify = SlackWebhookOperator(
        task_id="notify_success",
        slack_webhook_conn_id="slack_webhook",
        message="✅ 일 배치 ELT 완료",
    )
    extract >> transform >> load >> notify
