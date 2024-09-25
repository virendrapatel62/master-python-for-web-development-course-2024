class Phone:
    def __init__(self, name):
        self.name = name

    def call(self, contact):
        print(f"calling {contact} from {self.name}")


class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def click_photo(self):
        print(f"Capturing photo in {self.resolution}")


class SmartPhone(Phone, Camera):
    def __init__(self, name, resolution):
        Phone.__init__(self, name)
        Camera.__init__(self, resolution)


my_phone = SmartPhone("Apple 13", '1080px')
my_phone.call("9393049503")
my_phone.click_photo()
