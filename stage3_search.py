# WEEK 3 – Event Search System

events = []

while True:
    print("\nSMART EVENT & SPACE SCHEDULER")
    print("1. Add Event")
    print("2. View Events")
    print("3. Search Event")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Event Name: ").strip()
        dept = input("Enter Department: ").strip()

        event = {
            "name": name,
            "department": dept
        }

        events.append(event)
        print("Event Added!")

    elif choice == "2":
        print("\nAll Events:")
        for e in events:
            print(e)

    elif choice == "3":
        search_name = input("Enter Event Name to Search: ").strip().lower()
        found = False

        for e in events:
            if e["name"].lower() == search_name:
                print("Event Found:", e)
                found = True

        if not found:
            print("No Event Found!")

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")