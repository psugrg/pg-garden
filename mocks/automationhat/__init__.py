
class Relay():
    def __init__(self, name):
        self.name = name
    def on(self):
        print("[automationhat.relay." + self.name + "] ON")

    def off(self):
        print("[automationhat.relay." + self.name + "] OFF")

class Relays():
    def __init__(self):
        self.one = Relay("one")

relay = Relays()