from models.event import Event
from models.room import Room
from models.booking import Booking
from utils.file_handler import save_events, load_events, save_rooms, load_rooms

events = load_events()
rooms = load_rooms()
bookings = []


def add_event():
    title = input("Enter Event Title: ")
    date = input("Enter Date: ")
    start = input("Enter Start Time: ")
    end = input("Enter End Time: ")
    dept = input("Enter Department: ")
    event_type = input("Enter Event Type: ")

    event = Event(title, date, start, end, dept, event_type)

    if event.validate_event():
        events.append(event)
        print("Event added successfully")


def add_room():
    room_id = input("Enter Room ID: ")
    capacity = int(input("Enter Capacity: "))
    features = input("Enter Features: ")

    room = Room(room_id, capacity, features)

    if room.validate_room():
        rooms.append(room)
        print("Room added successfully")


def create_booking():
    if not events or not rooms:
        print("Add events and rooms first")
        return

    print("\nSelect Event:")
    for i, e in enumerate(events):
        print(i, e.title)

    e_index = int(input("Enter event index: "))
    event = events[e_index]

    print("\nSelect Room:")
    for i, r in enumerate(rooms):
        print(i, r.room_id)

    r_index = int(input("Enter room index: "))
    room = rooms[r_index]

    booking = Booking(event, room)
    bookings.append(booking)

    print("Booking created successfully!")


def view_bookings():
    if not bookings:
        print("No bookings available")
    else:
        for b in bookings:
            b.display_booking()


def save_data():
    save_events(events)
    save_rooms(rooms)
    print("Data saved successfully")


while True:

    print("""
SMART EVENT & SPACE SCHEDULER
1. Add Event
2. Add Room
3. Create Booking
4. View Bookings
5. Save Data
6. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_event()

    elif choice == "2":
        add_room()

    elif choice == "3":
        create_booking()

    elif choice == "4":
        view_bookings()

    elif choice == "5":
        save_data()

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
