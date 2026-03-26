from event import Event
from room import Room

events = []
rooms = []

def add_event():
    title = input("Enter Event Title: ")
    date = input("Enter Event Date (YYYY-MM-DD): ")
    start = input("Enter Start Time: ")
    end = input("Enter End Time: ")
    dept = input("Enter Department: ")
    event_type = input("Enter Event Type: ")

    event = Event(title, date, start, end, dept, event_type)

    if event.validate_event():
        events.append(event)
        print("Event added successfully")

def view_events():
    if not events:
        print("No events available")
    else:
        for e in events:
            e.display_event()

def add_room():
    room_id = input("Enter Room ID: ")
    capacity = int(input("Enter Room Capacity: "))
    features = input("Enter Room Features: ")

    room = Room(room_id, capacity, features)

    if room.validate_room():
        rooms.append(room)
        print("Room added successfully")

def view_rooms():
    if not rooms:
        print("No rooms available")
    else:
        for r in rooms:
            r.display_room()


while True:

    print("""
SMART EVENT & SPACE SCHEDULER
1. Add Event
2. View Events
3. Add Room
4. View Rooms
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_event()

    elif choice == "2":
        view_events()

    elif choice == "3":
        add_room()

    elif choice == "4":
        view_rooms()

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")