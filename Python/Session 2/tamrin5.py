class Car:
    def __init__(self, user_quality):
        self.speed = 0
        self.quality = user_quality

    def setSpeed(self, user_speed):
        self.speed = user_speed


# The Rest Of Code Is Just For Testing...
pride = Car("bullshit")
print(pride.quality)
print(pride.speed)
pride.setSpeed(10)
print(pride.speed)
