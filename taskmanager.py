class Task:
  def __init__(self, id, title, description, priority, status):
    self.id = id
    self.title = title
    self.description = description
    self.priority = priority
    self.status = status

class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)
    print("Task added successfully.")
  
  def filter_tasks(self):
    priority = input("Enter priority needed:\t")
    for task in self.tasks:
      if priority == task.priority:
        print(f" {task.id}, {task.title}, {task.description}, {task.priority}, {task.status}")


  def delete_task(self):
    if not self.tasks:
      print("No tasks to delete")
    else:
      print("delete operation")
      del_id = input("please enter your id to delete:\t")
      for task in self.tasks:
        if del_id == task.id:
          self.tasks.pop()
          print(f" {task.id} is deleted")
  
  def edit_task(self):
    if not self.tasks:
      print("No tasks to view")
    else:
      edit_id = input("please enter your id to edit:\t")
      for task in self.tasks:
        if edit_id == task.id:
          edited_title = input('enter your title (leave blank to keep existing):\t')
          edited_description = input('enter your description (leave blank to keep existing):\t')
          edited_priority = input('enter your priority (leave blank to keep existing):\t')
          edited_status = input('enter your status (leave blank to keep existing):\t')

          if edited_title == '':
            pass
          else:
            task.title = edited_title

          if edited_description == '':
            pass
          else:
            task.description = edited_description

          if edited_priority == '':
            pass
          else:
            task.title = edited_priority
          if edited_status == '':
            pass
          else:
            task.status = edited_status

          
         
      print(f" {task.id}, {task.title}, {task.description}, {task.priority}, {task.status}")
          
      
  def view_tasks(self):
    if not self.tasks:
      print("No tasks to view")
    else:
      print("Tasks:")
      for task in self.tasks:
        print(f" {task.id}, {task.title}, {task.description}, {task.priority}, {task.status}")

def main():
  task_manager = TaskManager()

  while True:
    print("\nOptions:\n")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View Task")
    print('5. Filter Task')
    print("6. Exit")
    
    

    choice = input("Enter your choice: ")

    if choice == "1":
      id = input("Enter task id: ")
      title = input("Enter task title: ")
      description = input("Enter task description: ")
      priority = input("Enter task priority: ")
      status = input("Enter task status: ")
      task = Task(id, title, description, priority, status)
      task_manager.add_task(task)

    elif choice == "2":
      task_manager.edit_task()

    elif choice == "3":
      task_manager.delete_task()

    elif choice == "4":
      task_manager.view_tasks()

    elif choice == "5":
      task_manager.filter_tasks()
        
    elif choice == "6":
      print("Exit...")
      break
 
      
    else:
      print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
