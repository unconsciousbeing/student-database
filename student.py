import csv
import sys

def add():    
    name = input("Name: ").title()
    roll = input("Roll number: ")

    with open("students.csv", "r") as i:
        check = csv.DictReader(i)
        for row in check:
            if row["roll"] == roll:
                sys.exit("Roll number already exists. ")

    
    marks = input("Marks: ")

    with open("students.csv", "a", newline="") as _:
        file = csv.DictWriter(_, fieldnames=["name", "roll", "marks"])
        file.writerow({"name": name, "roll": roll, "marks": marks})

def search():
    parameter = input("Search with Name or Roll? ").lower()
    if parameter == "name":
        name_search()
    elif parameter == "roll":
        roll_search()
    else:
        sys.exit("Please type a valid parameter. ")

def name_search():
    name = input("Name: ").title()
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        found = False
        for row in file:
            if row["name"] == name:
                found = True
                print("Found! \n")
                print(f'Name: {row["name"]} \nRoll number: {row["roll"]} \nMarks: {row["marks"]}') 
        if found == False:
            sys.exit("Not found. ")

def roll_search():
    roll = input("Roll number: ")
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        found = False
        for row in file:
            if row["roll"] == roll:
                found = True
                print("Found!")
                print(f"Name: {row['name']} \nRoll number: {row['roll']} \nMarks: {row['marks']}")
        if found == False:
            sys.exit("Not found. ")

def remove():
    roll = input("Roll number: ")
    rows = []
    removed = False
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        for row in file:
            if row["roll"] == roll:
                removed = True
            if row["roll"] != roll:
                rows.append(row)
    with open("students.csv", "w", newline="") as i:
        new = csv.DictWriter(i, fieldnames=["name", "roll", "marks"])
        new.writeheader()
        for k in rows:
            new.writerow(k)
    if removed == True:
        print("Removed! ")
    if removed == False:
        sys.exit("Student not found. ")

def update_marks():
    roll = input("Roll number: ")
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        found = False
        for row in file:
            if row["roll"] == roll:
                found = True
                print(f"Name: {row['name']} \nOld Marks: {row['marks']} \n")
        if found == False:
            sys.exit("Not found. ")

    new_marks = input("New Marks: ")
    rows = []
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        for row in file:
            if row["roll"] == roll:
                row["marks"] = new_marks
                rows.append(row)
            if row["roll"] != roll:
                rows.append(row)
    with open("students.csv", "w", newline="") as i:
        new = csv.DictWriter(i, fieldnames=["name", "roll", "marks"])
        new.writeheader()
        for k in rows:
            new.writerow(k)

def sort():
    action = input("Sort by Names or Marks? ").lower()
    if action == "name" or action == "names":
        sort_names()
    if action == "marks":
        sort_marks()

def sort_names():
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        sort = sorted(file, key=lambda student: student["name"])
        for row in sort:
            print(f"Name: {row['name']}, Roll number: {row['roll']}, Marks: {row['marks']} ")

def sort_marks():
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        sort = sorted(file, key=lambda student: int(student["marks"]), reverse=True)
        for row in sort:
            print(f"Name: {row['name']}, Roll number: {row['roll']}, Marks: {row['marks']} ")

def topper():
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        sort = sorted(file, key=lambda student: int(student["marks"]), reverse=True)
        row = sort[0]
        print(f"Name: {row['name']}, Roll number: {row['roll']}, Marks: {row['marks']} \n")

def average_marks():
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        total = 0
        rows = 0
        for row in file:
            total += int(row["marks"])
            rows += 1
        average = total / rows
        print(f"Average Marks: {round(average, 2)}")

def show_all():
    with open("students.csv", "r") as _:
        file = csv.DictReader(_)
        for row in file:
            print(f"Name: {row['name']}, Roll number: {row['roll']}, Marks: {row['marks']}")