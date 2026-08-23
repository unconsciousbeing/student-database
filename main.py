import sys
import student

print("\nWelcome to the Student Database Programme.\n")

while True:
        action = input("What do you wish to perform? \n" \
        "1. Add a student. \n" \
        "2. Search for a student information. \n" \
        "3. Show all students' information. \n" \
        "4. Remove a student's information. \n" \
        "5. Update a student's marks. \n" \
        "6. Sort all students' information. \n" \
        "7. Find the topper of the class. \n" \
        "8. Find Average marks. \n" \
        "9. Quit the program. \n" \
        "Action: ").lower()
        print()
        if action == "1" or action == "add":
                student.add()
        elif action == "2" or action == "search":
                student.search()
        elif action == "3" or action == "show":
                student.show_all()
        elif action == "4" or action == "delete" or action == "remove":
                student.remove()
        elif action == "5" or action == "update":
                student.update_marks()
        elif action == "6" or action == "sort":
                student.sort()
        elif action == "7" or action == "topper":
                student.topper()
        elif action == "8" or action == "average":
                student.average_marks()
        elif action == "9" or action == "quit" or action == "exit":
                sys.exit("Thank you for using this program.")
        else:
                print("Invalid action. ")
        print("\n\n")