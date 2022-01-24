from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

# The DummyOperator is a task and does nothing
accurate = DummyOperator(task_id="accurate")
# The BashOperator is a task to execute a bash command
commands = BashOperator(task_id="commands", bash_command="sleep 5")
