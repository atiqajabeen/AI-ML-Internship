import os
DATA_FILE = "intern_records.txt"
class Intern:
    def __init__(self, intern_id, full_name, email):
        self.intern_id = intern_id
        self.full_name = full_name
        self.email = email
        self.tasks = []
    def add_task(self, title):
        self.tasks.append({"title": title, "status": "Pending"})
    def calculate_score(self):
        score = 0
        completed_count = 0
        for task in self.tasks:
            if task["status"] == "Completed":
                score += 12
                completed_count += 1
            elif task["status"] == "In Progress":
                score += 6
        if completed_count >= 3:
            score += 5
        return score
    def get_rank(self):
        score = self.calculate_score()
        if score >= 45:
            return "Star Performer"
        elif score >= 25:
            return "Rising Talent"
        elif score >= 10:
            return "On Track"
        else:
            return "Just Started"
class InternshipManager:
    def __init__(self):
        self.interns = []
        self.batch_year = 2026
        self.load_data()
    def generate_unique_id(self):
        serial_number = len(self.interns) + 1
        new_id = f"INT-{self.batch_year}-{serial_number:03d}"
        while self.id_exists(new_id):
            serial_number += 1
            new_id = f"INT-{self.batch_year}-{serial_number:03d}"
        return new_id
    def id_exists(self, intern_id):
        for intern in self.interns:
            if intern.intern_id == intern_id:
                return True
        return False
    def is_duplicate(self, full_name, email):
        for intern in self.interns:
            if intern.full_name.strip().lower() == full_name.strip().lower() and intern.email.strip().lower() == email.strip().lower():
                return True
        return False
    def find_intern(self, search_value):
        search_value = search_value.strip().lower()
        for intern in self.interns:
            if intern.intern_id.lower() == search_value or intern.full_name.lower() == search_value:
                return intern
        return None
    def register_intern(self):
        try:
            full_name = input("Enter full name: ").strip()
            email = input("Enter email address: ").strip()
            if not full_name or not email:
                print("Error: Name and email cannot be empty.")
                return
            if self.is_duplicate(full_name, email):
                print("Error: An intern with this name and email is already registered.")
                return
            new_id = self.generate_unique_id()
            new_intern = Intern(new_id, full_name, email)
            self.interns.append(new_intern)
            print(f"Success: Intern registered with ID {new_id}")
            self.save_data()
        except Exception as error:
            print(f"An error occurred during registration: {error}")
    def assign_task(self):
        try:
            search_value = input("Enter Intern ID or Name: ").strip()
            intern = self.find_intern(search_value)
            if intern is None:
                print("Error: Intern not found.")
                return
            task_title = input("Enter task title: ").strip()
            if not task_title:
                print("Error: Task title cannot be empty.")
                return
            intern.add_task(task_title)
            print(f"Success: Task '{task_title}' assigned to {intern.full_name}.")
            self.save_data()
        except Exception as error:
            print(f"An error occurred while assigning the task: {error}")
    def update_task_status(self):
        try:
            search_value = input("Enter Intern ID or Name: ").strip()
            intern = self.find_intern(search_value)
            if intern is None:
                print("Error: Intern not found.")
                return
            if not intern.tasks:
                print("This intern has no tasks assigned yet.")
                return
            print(f"\nTasks assigned to {intern.full_name}:")
            for index, task in enumerate(intern.tasks, start=1):
                print(f"  {index}. {task['title']}  [{task['status']}]")
            task_number = int(input("Enter task number to update: "))
            if task_number < 1 or task_number > len(intern.tasks):
                print("Error: Invalid task number.")
                return
            print("1. Pending\n2. In Progress\n3. Completed")
            status_choice = input("Select new status (1/2/3): ").strip()
            status_map = {"1": "Pending", "2": "In Progress", "3": "Completed"}
            if status_choice not in status_map:
                print("Error: Invalid status selection.")
                return
            intern.tasks[task_number - 1]["status"] = status_map[status_choice]
            print("Success: Task status updated.")
            self.save_data()
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as error:
            print(f"An error occurred while updating task status: {error}")
    def search_intern(self):
        search_value = input("Enter Intern ID or Name to search: ").strip()
        intern = self.find_intern(search_value)
        if intern is None:
            print("No matching intern found.")
            return
        print("\n" + "=" * 40)
        print(f"Intern ID : {intern.intern_id}")
        print(f"Name      : {intern.full_name}")
        print(f"Email     : {intern.email}")
        print(f"Score     : {intern.calculate_score()}")
        print(f"Rank      : {intern.get_rank()}")
        print("Tasks     :")
        if not intern.tasks:
            print("   No tasks assigned yet.")
        else:
            for task in intern.tasks:
                print(f"   - {task['title']}  ->  {task['status']}")
        print("=" * 40)
    def display_pending_tasks(self):
        print("\n---- Pending Tasks ----")
        found_any = False
        for intern in self.interns:
            for task in intern.tasks:
                if task["status"] == "Pending":
                    print(f"{intern.full_name}: {task['title']}")
                    found_any = True
        if not found_any:
            print("No pending tasks at the moment.")
    def display_completed_tasks(self):
        print("\n---- Completed Tasks ----")
        found_any = False
        for intern in self.interns:
            for task in intern.tasks:
                if task["status"] == "Completed":
                    print(f"{intern.full_name}: {task['title']}")
                    found_any = True
        if not found_any:
            print("No completed tasks yet.")
    def display_rankings(self):
        if not self.interns:
            print("No interns registered yet.")
            return
        ranked_interns = sorted(self.interns, key=lambda i: i.calculate_score(), reverse=True)
        print("\n---- Intern Rankings ----")
        for position, intern in enumerate(ranked_interns, start=1):
            print(f"{position}. {intern.full_name} ({intern.intern_id}) - {intern.calculate_score()} pts - {intern.get_rank()}")

    def display_top_performer(self):
        if not self.interns:
            print("No interns registered yet.")
            return
        top_intern = max(self.interns, key=lambda i: i.calculate_score())
        print(f"Top Performing Intern: {top_intern.full_name} ({top_intern.calculate_score()} pts, {top_intern.get_rank()})")

    def generate_report(self):
        print("\n========== SUMMARY REPORT ==========")
        if not self.interns:
            print("No data available to report.")
            return
        total_score = 0
        for intern in self.interns:
            print(f"\n{intern.intern_id} | {intern.full_name} | {intern.calculate_score()} pts | {intern.get_rank()}")
            total_score += intern.calculate_score()
            if not intern.tasks:
                print("   No tasks assigned.")
            else:
                for task in intern.tasks:
                    print(f"   - {task['title']}: {task['status']}")
        average_score = round(total_score / len(self.interns), 2)
        print(f"\nAverage Team Score: {average_score}")
        self.display_top_performer()
    def display_all_interns(self):
        if not self.interns:
            print("No interns registered yet.")
            return
        print("\n---- All Registered Interns ----")
        for intern in self.interns:
            print(f"{intern.intern_id} - {intern.full_name} - {intern.get_rank()}")
    def save_data(self):
        try:
            file = open(DATA_FILE, "w", encoding="utf-8")
            for intern in self.interns:
                task_data = ""
                for task in intern.tasks:
                    task_data += f"{task['title']}::{task['status']};;"
                line = f"{intern.intern_id}|{intern.full_name}|{intern.email}|{task_data}"
                file.write(line + "\n")
            file.close()
        except Exception as error:
            print(f"Error: Could not save data. {error}")

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            file = open(DATA_FILE, "r", encoding="utf-8")
        except Exception as error:
            print(f"Error: Could not load data. {error}")
            return
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 4:
                continue
            intern_id, full_name, email, task_data = parts[0], parts[1], parts[2], parts[3]
            intern = Intern(intern_id, full_name, email)
            if task_data.strip():
                for task_entry in task_data.split(";;"):
                    if not task_entry.strip():
                        continue
                    if "::" in task_entry:
                        title, status = task_entry.split("::")
                        intern.tasks.append({"title": title, "status": status})
            self.interns.append(intern)
        file.close()
        print(f"Loaded {len(self.interns)} existing intern record(s) from file.\n")
def display_menu():
    print("\n---------- AI Internship Dashboard ----------")
    print("1. Register Intern")
    print("2. Assign Task")
    print("3. Update Task Status")
    print("4. Search Intern")
    print("5. View Pending Tasks")
    print("6. View Completed Tasks")
    print("7. View Rankings")
    print("8. Generate Report")
    print("9. View All Interns")
    print("10. Exit")
def main():
    manager = InternshipManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manager.register_intern()
        elif choice == "2":
            manager.assign_task()
        elif choice == "3":
            manager.update_task_status()
        elif choice == "4":
            manager.search_intern()
        elif choice == "5":
            manager.display_pending_tasks()
        elif choice == "6":
            manager.display_completed_tasks()
        elif choice == "7":
            manager.display_rankings()
        elif choice == "8":
            manager.generate_report()
        elif choice == "9":
            manager.display_all_interns()
        elif choice == "10":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 10.")


if __name__ == "__main__":
    main()