# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._all_entries = []
        
    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._all_entries.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        self._incomplete_entries = []
        for todo in self._all_entries:
            if todo.complete == False:
                print(f"the task that is completed and is to be removed from the incompleted list:{todo.task}")
                self._incomplete_entries.append(todo)
                

        return self._incomplete_entries

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        self._complete = []
        for todo in self._all_entries:
            if todo.complete == True:
                print(f"the task that is completed and to be added to the completed list is:{todo.task}")
                self._complete.append(todo)
    
        return self._complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._all_entries: # iterate across the to do entries 
            todo.mark_complete() # and make sure each entry is marked as complete using the Todo class!
            print(f"the task that is completed: {todo.task}")
            print(todo.complete) # mark each to do item as complete, which sets the individual property as complete.
            
        

# class Todo:
#     # Public Properties:
#     #   task: a string representing the task to be done
#     #   complete: a boolean representing whether the task is complete

#     def __init__(self, task):
#         # Parameters:
#         #   task: a string representing the task to be done
#         # Side-effects:
#         #   Sets the task property
#         #   Sets the complete property to False
#         self.task = task
#         self.complete = False

#     def mark_complete(self):
#         # Returns:
#         #   Nothing
#         # Side-effects:
#         #   Sets the complete property to True
    
#         self.complete = True


# todo_list = TodoList()
# todo_1 = Todo("Walk the dog")
# todo_2 = Todo("Do homework")
# todo_list.add(todo_1)
# todo_list.add(todo_2)
# todo_2.mark_complete()
# print(f"printing incomplete after completing todo list 2 {todo_list.incomplete()}")
# print(f"printing compelted list after completeing  to do2 {todo_list.complete()}")
# todo_3 = Todo("Make dinner")
# todo_list.add(todo_3)
# print(f"printing incomplete after adding todo_3 {todo_list.incomplete()}")
# print(f"printing compelted list after adding todo_3  {todo_list.complete()}")
# todo_list.give_up()
# print(f"printing the incomplete list after giving up {todo_list.incomplete()}")# == []
# print(f"printing the complete list after giving up  {todo_list.complete()}") # ==[todo_2, todo_1, todo_3]