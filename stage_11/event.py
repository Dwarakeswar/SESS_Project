from sess.models.record import Record

class Event(Record):

    def __init__(self, title, date, start_time, end_time, department, event_type):
        super().__init__()
        self._title = title
        self._date = date
        self._start_time = start_time
        self._end_time = end_time
        self._department = department
        self._event_type = event_type

    def get_title(self):
        return self._title

    def get_date(self):
        return self._date

    def get_times(self):
        return self._start_time, self._end_time

    def validate_event(self):
        if self._title == "":
            print("Invalid event title")
            return False
        if self._start_time >= self._end_time:
            print("Invalid time")
            return False
        return True
