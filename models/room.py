from record import Record

class Room(Record):

    def __init__(self, room_id, capacity, features):
        super().__init__()   # Call Record constructor

        self.room_id = room_id
        self.capacity = capacity
        self.features = features

    def validate_room(self):
        if self.capacity <= 0:
            print("Invalid capacity")
            return False
        return True

    def display_room(self):
        print("\n--- Room Details ---")
        print("Room ID:", self.room_id)
        print("Capacity:", self.capacity)
        print("Features:", self.features)
        print("Created At:", self.timestamp)
