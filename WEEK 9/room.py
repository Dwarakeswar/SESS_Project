from record import Record

class Room(Record):

    def __init__(self, room_id, capacity, features):
        super().__init__()

        self._room_id = room_id
        self._capacity = capacity
        self._features = features

    def get_room_id(self):
        return self._room_id

    def validate_room(self):
        if self._capacity <= 0:
            print("Invalid capacity")
            return False
        return True
