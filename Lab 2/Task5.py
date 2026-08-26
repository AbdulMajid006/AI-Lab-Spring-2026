# Task#5:
# Smart Home Light System (OOP Automation):
# Create a SmartLight class with:
# • Attributes: room, status
# • Methods: turn_on(), turn_off(), show_status()
# Create lights for different rooms and control them.

class SmartLight:
    def __init__(self, room, status):
        self.room = room
        self.status = status

    def turn_on(self):
        self.status = "On"
    def turn_off(self):
        self.status = "Off"
    def show_status(self):
        print("Room: ", self.room)
        print("Status: ", self.status)

sl1 = SmartLight("Dining Room", "Off")
sl2 = SmartLight("Lounge", "On")
sl1.show_status()
sl2.show_status()
sl1.turn_on()
sl2.turn_off()
print("After Change")
sl1.show_status()
sl2.show_status()
