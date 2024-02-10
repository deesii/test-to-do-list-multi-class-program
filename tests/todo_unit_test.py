from lib.todo import *


'''
given a task, during instanciates with the task itself.

'''

def test_instanciation_of_ToDo_task_given_task():
    todo_1 = Todo("Walk the dog")
    assert todo_1.task == "Walk the dog"
    assert todo_1.complete == False


'''
given a task that is now completed task is marked as complete
and boolean set to True

'''

def test_instanciation_of_ToDo_task_given_task():
    todo_1 = Todo("Walk the dog")
    todo_1.mark_complete()
    assert todo_1.complete == True

