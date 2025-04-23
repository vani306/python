class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def display(self):
        print(f"{self.hours} hours, {self.minutes} minutes")

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + (total_minutes // 60)
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def to_minutes(self):
        return self.hours * 60 + self.minutes

    def from_minutes(self, total_minutes):
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

t1 = Time(2, 50)
t2 = Time(1, 30)

print("Time 1:")
t1.display()

print("Time 2:")
t2.display()

sum_time = t1.add(t2)
print("Added Time:")
sum_time.display()

print("Time 1 in total minutes:", t1.to_minutes())
print("Time 2 in total minutes:", t2.to_minutes())
