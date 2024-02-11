from lib.todo import *
import pytest

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

def test_instanciation_of_ToDo_task_given_task_changes_when_marked_complete():
    todo_1 = Todo("Walk the dog")
    todo_1.mark_complete()
    assert todo_1.complete == True

'''
given an invalid entry (empty string) as a task, raise an exception

'''

def test_invalid_entry_exception_raised():
    
    with pytest.raises(Exception) as e:
        todo_1 = Todo("")
    error_message = str(e.value)
    assert error_message == "Input valid task as string that is not empty!"