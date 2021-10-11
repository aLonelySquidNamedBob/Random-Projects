import time
# from RPi import GPIO


class Stepper:
    def __init__(self, pins, stepType):
        self.pins = pins
        self.stepType = stepType
        self.switchPin = None

        self.SetupGPIO()

        if self.stepType == 'half':
            self.stepCount = 8
            self.stepSeq = []
            self.stepSeq = [i for i in range(0, self.stepCount)]
            self.stepSeq[0] = [1, 0, 0, 0]
            self.stepSeq[1] = [1, 1, 0, 0]
            self.stepSeq[2] = [0, 1, 0, 0]
            self.stepSeq[3] = [0, 1, 1, 0]
            self.stepSeq[4] = [0, 0, 1, 0]
            self.stepSeq[5] = [0, 0, 1, 1]
            self.stepSeq[6] = [0, 0, 0, 1]
            self.stepSeq[7] = [1, 0, 0, 1]

        elif self.stepType == 'full':
            self.stepCount = 4
            self.stepSeq = []
            self.stepSeq = [i for i in range(0, self.stepCount)]
            self.stepSeq[0] = [1, 0, 0, 0]
            self.stepSeq[1] = [0, 1, 0, 0]
            self.stepSeq[2] = [0, 0, 1, 0]
            self.stepSeq[3] = [0, 0, 0, 1]

        else:
            raise Exception("Step type not defined : 'half' / 'full'")

    def SetupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def SetStep(self, values):
        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], values[i])

    def Step(self, num, delay):
        if num < 0:
            raise Exception("Step count negative")
        for i in range(num):
            self.SetStep(self.stepSeq[int(i % self.stepCount)])
            time.sleep(delay / 1000)

    def PowerOff(self):
        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], GPIO.LOW)

    def SetupSwitch(self, pin):
        self.switchPin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.IN)

    def Switch(self):
        return GPIO.input(self.switchPin)


def main():
    pins = [3, 17, 23, 24]
    stepper = Stepper(pins, 'full')
    stepper.Step(400, 3)
    stepper.PowerOff()


if __name__ == '__main__':
    main()
