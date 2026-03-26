events = []

while True:
    print("\n1. Add Event")
    print("2. View Events")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event_name = input("Event Name: ")
        event_date = input("Event Date (YYYY-MM-DD): ")
        start_time = input("Start Time (HH:MM): ")
        end_time = input("End Time (HH:MM): ")
        department = input("Department: ")
        event_type = input("Event Type: ")

        event = [
            event_name,
            event_date,
            start_time,
            end_time,
            department,
            event_type
        ]

        events.append(event)
        print("Event added successfully")

    elif choice == "2":
        if len(events) == 0:
            print("No events scheduled")
        else:
            for i in range(len(events)):
                print("\nEvent", i + 1)
                print("Event Name:", events[i][0])
                print("Date:", events[i][1])
                print("Time:", events[i][2], "-", events[i][3])
                print("Department:", events[i][4])
                print("Event Type:", events[i][5])

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice, try again")
