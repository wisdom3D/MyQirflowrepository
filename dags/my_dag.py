from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utilst.helpers import chain
def print_a():
    print('hi from task a')
def print_b():
    print('hi from task a')

with DAG('my_dag',
         start_date = datetime(2023, 1, 1),
         schedule = '@daily',
         description = 'A simple tutorial DAG',
         tags = ['data_science'],
         catchup = False):
    taskA = PythonOperator(
	python_callable=print_a,
	op_args="None",
	op_kwargs="None",
	templates_dict="None",
	templates_exts="None",
	show_return_value_in_logs="True",
    task_id = 'task_a')
    taskB = PythonOperator(
	python_callable=print_b,
	op_args="None",
	op_kwargs="None",
	templates_dict="None",
	templates_exts="None",
	show_return_value_in_logs="True",
    task_id = 'task_b')
    chain(taskA, taskB)