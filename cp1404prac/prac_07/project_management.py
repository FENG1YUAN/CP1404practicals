"""
CP1404/CP5632 Practical
Author: FENG YUAN
Time: 30 minutes
"""


import os
from datetime import datetime
from project import Project


def display_menu():
    menu = """
- (L)Load projects  
- (S)Save projects  
- (D)Display projects  
- (F)Filter projects by date
- (A)Add new project  
- (U)Update project
- (Q)Quit
"""
    print(menu)


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\
                t{project.cost_estimate}"
                f"\t{project.completion_percentage}\n")


def main():
    projects = []
    while True:
        display_menu()
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            if os.path.exists(filename):
                projects = load_projects(filename)
                print("Projects loaded successfully.")
            else:
                print(f"File {filename} not found.")
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved successfully.")
        elif choice == "d":
            incomplete = [project for project in projects if not project.is_complete()]
            complete = [project for project in projects if project.is_complete()]

            print("Incomplete projects: ")
            for project in sorted(incomplete):
                print("  " + str(project))

            print("Completed projects: ")
            for project in sorted(complete):
                print("  " + str(project))
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
            for project in sorted(projects, key=lambda x: x.start_date):
                if project.start_date > date_obj:
                    print("  " + str(project))
        elif choice == "a":
            name = input("Let's add a new project\nName: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = input("Priority: ")
            cost_estimate = input("Cost estimate: ")
            completion_percentage = input("Percent complete: ")
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "u":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            selected_project = projects[project_choice]
            print(selected_project)
            completion_percentage = input("New Percentage: ")
            priority = input("New Priority: ")
            selected_project.update(completion_percentage if completion_percentage else None,
                                    priority if priority else None)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
