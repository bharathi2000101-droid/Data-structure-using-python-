# Student Registration System using Hashing
# Collision Resolution: Linear Probing

size = 10
hash_table = [None] * size


def insert():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    index = roll % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            hash_table[pos] = (roll, name)
            print("Student record inserted successfully")
            return

        if hash_table[pos][0] == roll:
            print("Roll Number already exists")
            return

    print("Hash Table is full")


def search():
    roll = int(input("Enter Roll Number to search: "))
    index = roll % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            print("Student not found")
            return

        if hash_table[pos][0] == roll:
            print("Student Found")
            print("Roll Number:", hash_table[pos][0])
            print("Student Name:", hash_table[pos][1])
            return

    print("Student not found")


def delete():
    roll = int(input("Enter Roll Number to delete: "))
    index = roll % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            print("Student not found")
            return

        if hash_table[pos][0] == roll:
            hash_table[pos] = "DELETED"
            print("Student record deleted successfully")
            return

    print("Student not found")


def display():
    print("\nIndex\tRoll Number\tStudent Name")

    for i in range(size):
        record = hash_table[i]

        if record is None:
            print(i, "\tEmpty")
        elif record == "DELETED":
            print(i, "\tDeleted")
        else:
            print(i, "\t", record[0], "\t\t", record[1])


while True:
    print("\n--- Student Registration System ---")
    print("1. Insert Student Record")
    print("2. Search Student")
    print("3. Delete Student Record")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
