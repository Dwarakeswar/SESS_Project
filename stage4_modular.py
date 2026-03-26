# WEEK 4 – Modular Function-Based System

events = []

def add_event():
    name = input("Enter Event Name: ").strip()
    dept = input("Enter Department: ").strip()
    date = input("Enter Date (YYYY-MM-DD): ").strip()

    event = {
        "name": name,
        "department": dept,
        "date": date
    }

    events.append(event)
    print("Event Added Successfully!")

def view_events():
    if not events:
        print("No Events Available.")
    else:
        print("\n--- Event List ---")
        for e in events:
            print(e)

def search_event():
    search_name = input("Enter Event Name to Search: ").strip().lower()
    found = False

    for e in events:
        if e["name"].lower() == search_name:
            print("Event Found:", e)
            found = True

    if not found:
        print("Event Not Found.")

def main_menu():
    while True:
        print("\nSMART EVENT & SPACE SCHEDULER")
        print("1. Add Event")
        print("2. View Events")
        print("3. Search Event")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            search_event()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")

main_menu()