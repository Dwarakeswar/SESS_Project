# event.py

class Event:

    def __init__(self, title, date, start_time, end_time, department, event_type):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.department = department
        self.event_type = event_type

    def get_times(self):
        return self.start_time, self.end_time