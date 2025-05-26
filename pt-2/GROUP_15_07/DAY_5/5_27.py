class Door:
    def open(self):
        print("Door is open")


class Alarm:
    def activate(self):
        print("Alarm is activated")


class SecuritySystem:

    def __init__(self):
        self.door = Door()
        self.alarm = Alarm()

    def arm(self):
        self.door.open()
        self.alarm.activate()
        print("Security system armed")

# my_security_system = SecuritySystem()
# my_security_system.arm()




class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play_instrument(self):
        return f"{self.name} is playing {self.instrument}"


class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def play_music(self):
        if not self.members:
            return f"Я соло {self.name}",
        return [member.play_instrument() for member in self.members]



group = Band("Любе")
for mus in group.play_music():
    print(mus)


john = Musician("John", "guitar")
paul = Musician("Paul", "bass")
george = Musician("George", "guitar")
ringo = Musician("Ringo", "drums")


beatles = Band("Beatles", [john, paul, george, ringo])

for music in beatles.play_music():
    print(music)

















