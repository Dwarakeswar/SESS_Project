# main.py
from services.scheduler import Scheduler
from utils.file_handler import load_events, load_rooms, save_events, save_rooms
from utils.file_handler import save_bookings, load_bookings
from utils.stats import generate_stats
from utils.charts import plot_room_usage


events = load_events()
rooms = load_rooms()
bookings = load_bookings(events, rooms)


scheduler = Scheduler(events, rooms, bookings)

while True:
    print("""
    1. Add Event
    2. Add Room
    3. Create Booking
    4. View Bookings
    5. Save Data
    6. Show Analytics
    7. Delete Event
    8. Update Event
    9. Delete Room
    10. Update Room
    11. Delete Booking
    12. Search Booking
    13. Exit
    """)

    ch = input("Choice: ")

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
        save_bookings(bookings)
    elif ch == "6":
        stats = generate_stats(bookings)
        print(stats)
        plot_room_usage(stats)
    elif ch == "7":
        scheduler.delete_event()
    elif ch == "8":
        scheduler.update_event()
    elif ch == "9":
        scheduler.delete_room()
    elif ch == "10":
        scheduler.update_room()
    elif ch == "11":
        scheduler.delete_booking()
    elif ch == "12":
        scheduler.search_booking()
    elif ch == "13":
        break