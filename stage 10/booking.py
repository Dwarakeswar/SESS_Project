class Booking:

    def __init__(self, event, room):
        self.event = event
        self.room = room
        self.status = "CONFIRMED"

    def display_booking(self):
        print(f"{self.event.get_title()} -> Room {self.room.get_room_id()}")
