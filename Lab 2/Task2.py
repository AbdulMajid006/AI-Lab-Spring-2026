# Task#2:
# Smart Fan Controller (Constructor & Methods):
# Create a SmartFan class with:
# • Attributes: room_name, speed
# • Methods: increase_speed(), decrease_speed(), display_status()
# Create multiple fan objects and change their speed.

class SmartFan:
    def __init__(self, room_name):
        self.room_name = room_name
        self.speed = 0
    def increase_speed(self, x):
        self.speed += x
    def decrease_speed(self, x):
        self.speed -= x
    def display_status(self):
        print(f"Room Name: {self.room_name}, Speed: {self.speed}")

sf1 = SmartFan("Bedroom")
sf2 = SmartFan("Lounge")
sf1.display_status()
sf2.display_status()
sf1.increase_speed(50)
sf2.decrease_speed(33)
print("After change")
sf1.display_status()
sf2.display_status()
