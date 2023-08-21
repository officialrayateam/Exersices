class Car:
    def __init__(self, quality):
        self.speed = 0
        self.quality = quality

    def setSpeed(self, speed):
        self.speed = speed


# The Rest Of Code Is Just For Testing...
pride = Car("bullshit")
print(pride.quality)
print(pride.speed)
print(pride.setSpeed(10))
print(pride.speed)
