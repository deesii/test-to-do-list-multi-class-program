from lib.todo import *
from lib.todo_list import *
import pytest

'''
Integrated Given a todo item as a string, want to put it in the todo list.
It will automatically be set as incomplete (therefore boolean = False)
This will appear on the todo list, it will add to an empty todolist
'''

def test_to_add_the_to_do_item_to_list():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]

'''
Integrated Given a todo item as a string, want to put it in the todo list.
It will automatically be set as incomplete (therefore boolean = False)
This will appear on the todo list, it will add to an existing list. Both incomplete.
'''

def test_to_add_the_to_do_item_to_an_existing_incompelte_list():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Do homework")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]


'''
Integrated Given a todo task added and then completed, the incompleted list reduces by that amount
and the completed list increase by that object
'''

def test_to_completing_a_task_and_seeing_incomplete_complete_list():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Do homework")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.incomplete() == [todo_2]
    assert todo_list.complete() ==[todo_1]


'''
Integrated Given a todo task added and then completed, the incompleted list reduces by that amount
and the completed list increase by that object, adding an additional task adds to the incomplete list
'''

def test_to_adding_after_completing_tasks():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Do homework")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    todo_3 = Todo("Make dinner")
    todo_list.add(todo_3)
    assert todo_list.incomplete() == [todo_2, todo_3]
    assert todo_list.complete() ==[todo_1]


'''
Integrated : makes all complete, so all the list from the incomplete disappears 
and the complete task list is set to all the tasks, listed in order of added.
'''

def test_for_give_up_after_adding_and_completing_task():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Do homework")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()
    todo_3 = Todo("Make dinner")
    todo_list.add(todo_3)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() ==[todo_1, todo_2, todo_3]

    '''
    Additional ones that could be done: Exceptions for when there isnt 
    a task that is not a string or that is empty
    
    '''