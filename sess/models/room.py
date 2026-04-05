# room.py

class Room:

    def __init__(self, room_id, capacity, features):
        self.room_id = room_id
        self.capacity = capacity
        self.features = set(features.lower().split(","))

    def get_features(self):
        return self.features