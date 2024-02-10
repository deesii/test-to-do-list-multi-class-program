from lib.todo_list import *

'''
todo_list instanciates an empty todo_list object with empty entries and empty complete 

'''

def test_instanciation_of_ToDoList():
    todo_list = TodoList()
    assert todo_list._all_entries == []
