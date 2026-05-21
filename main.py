from crud.create_table import create_table
from crud.insert_into_table import insert_data
from crud.read_table import read_data
from crud.update_table import update_data
from crud.delete_table import delete_data

while True:
    print("\n===== USER MANAGEMENT SYSTEM =====")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_table()

    elif choice == '2':
        insert_data()

    elif choice == '3':
        read_data()

    elif choice == '4':
        update_data()

    elif choice == '5':
        delete_data()

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice")