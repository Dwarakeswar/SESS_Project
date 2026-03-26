class Event:

    def __init__(self, title, date, start_time, end_time, department, event_type):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.department = department
        self.event_type = event_type

    def validate_event(self):
        if self.title == "":
            print("Invalid event title")
            return False

        if self.start_time >= self.end_time:
            print("Invalid time: Start time must be before end time")
            return False

        return True

    def display_event(self):
        print("\nEvent Details")
        print("Title:", self.title)
        print("Date:", self.date)
        print("Start Time:", self.start_time)
        print("End Time:", self.end_time)
        print("Department:", self.department)
        print("Event Type:", self.event_type)