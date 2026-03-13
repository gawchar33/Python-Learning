class Animal:
    type="animals"
    def speak(self):
        print("animal sound")
class dog(Animal):
    def speak(self):
        #super.speak()
        print("dog bark")
bruno=dog()
print(bruno.type)
print(bruno.speak())

