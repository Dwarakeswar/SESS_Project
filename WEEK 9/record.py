import time

class Record:
    def __init__(self):
        self.timestamp = time.ctime()

    def display_timestamp(self):
        print("Created At:", self.timestamp)