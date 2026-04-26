from services.scheduler import Scheduler
from utils.file_handler import load_events, load_rooms, save_events, save_rooms

events = load_events()
rooms = load_rooms()
bookings = []

scheduler = Scheduler(events, rooms, bookings)

while True:
    print("""
1. Add Event
2. Add Room
3. Create Booking
4. View Bookings
5. Save Data
6. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        scheduler.add_event()
    elif ch == "2":
        scheduler.add_room()
    elif ch == "3":
        scheduler.create_booking()
    elif ch == "4":
        scheduler.view_bookings()
    elif ch == "5":
        save_events(events)
        save_rooms(rooms)
    elif ch == "6":
        break
    else:
        print("Invalid choice")
