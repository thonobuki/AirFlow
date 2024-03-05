from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define os argumentos padrão do DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define o nome do DAG e os argumentos
dag = DAG(
    'download_and_process_file',
    default_args=default_args,
    description='Baixa um arquivo da internet e o processa',
    schedule_interval=timedelta(days=1),
)

# Tarefa para baixar o arquivo
download_task = BashOperator(
    task_id='download_file',
    bash_command='wget -O /tmp/data.csv http://example.com/data.csv',
    dag=dag,
)

# Tarefa para processar o arquivo baixado
def process_file():
    # Código para processar o arquivo baixado
    pass

process_task = PythonOperator(
    task_id='process_file',
    python_callable=process_file,
    dag=dag,
)

# Define a ordem de execução das tarefas
download_task >> process_task
