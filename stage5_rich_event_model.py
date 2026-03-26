# WEEK 5 – Dictionaries, Sets, Tuples Implementation

events = {}              # dictionary to store events
departments = set()      # set to store unique departments
event_types = set()      # set to store unique event types
event_logs = []          # list of tuples for logs

event_id_counter = 1


def add_event():
    global event_id_counter

    name = input("Enter Event Name: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    start = input("Enter Start Time: ")
    end = input("Enter End Time: ")
    department = input("Enter Department: ")
    event_type = input("Enter Event Type: ")

    event = {
        "name": name,
        "date": date,
        "start_time": start,
        "end_time": end,
        "department": department,
        "type": event_type
    }

    events[event_id_counter] = event

    departments.add(department)
    event_types.add(event_type)

    event_logs.append((name, "ADDED"))

    print("Event Added Successfully with ID:", event_id_counter)

    event_id_counter += 1


def view_events():
    if not events:
        print("No events available.")
        return

    print("\n--- Event List ---")
    for event_id, event in events.items():
        print("ID:", event_id, "|", event)


def search_event():
    search_name = input("Enter Event Name to Search: ").lower()

    for event_id, event in events.items():
        if event["name"].lower() == search_name:
            print("Event Found:", event)
            return

    print("Event not found.")


def show_departments():
    print("Departments conducting events:")
    for d in departments:
        print(d)


def show_logs():
    print("\nEvent Logs:")
    for log in event_logs:
        print(log)


def menu():
    while True:
        print("\nSMART EVENT & SPACE SCHEDULER")
        print("1. Add Event")
        print("2. View Events")
        print("3. Search Event")
        print("4. Show Departments")
        print("5. Show Logs")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_event()

        elif choice == "2":
            view_events()

        elif choice == "3":
            search_event()

        elif choice == "4":
            show_departments()

        elif choice == "5":
            show_logs()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


menu()