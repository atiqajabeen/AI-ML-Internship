class cat:
    def sound(self):
        print("Meow")
class dog:
    def sound(self):
        print("Bark")
class cow:
    def sound(self):
        print("Moo")
animals=[cat(),dog(),cow()]
for animal in animals:
    animal.sound()
