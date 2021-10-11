import time
import math
from Star_Tracker.stepper import Stepper

### Global variables ###
_rotationPerHour = 15.0410687329
_rotationPerMin = 0.2506844789
_rotationPerSec = 0.0041780746

radius = 215
pitch = 1

motorTeeth = 20
gearTeeth = 80

### Motor variables ###

_steps = int(input('Step count (1024 / 2048): '))
if _steps == 2048:
    _type = 'half'
else:
    _type = "full"
_pins = [3, 17, 23, 24]
_switch = 4


### Functions ###

def NutRevs(angle):
    revs = 2 * math.pi * radius * (angle / 360)
    return revs


def CalculateSteps(revs):
    gearRatio = gearTeeth / motorTeeth
    steps = revs * gearRatio * _steps
    return steps


### Main ###

def main():
    # Stepper initialisation
    stepper = Stepper(_pins, _type)
    # stepper.SetupGPIO()
    # stepper.SetupSwitch(_switch)

    # Calculations
    factor = float(input('Number of hours? '))

    revs = NutRevs(_rotationPerHour * factor)
    steps = CalculateSteps(revs)
    delay = 1000 / (steps / factor / 3600)

    # Print results
    print(f'Total Nut revs : {revs}')
    print(f'Total motor steps : {steps}')
    print(f'Total motor rotations : {steps / _steps}')
    print()
    print(f'Nut revs per second : {revs / factor / 3600}')
    print(f'Motor steps per second : {steps / factor / 3600}')
    print(f'Delay between steps : {delay} ms')

    # Run Stepper
    while True:
        while stepper.Switch(_switch):
            stepper.Step(10, delay)
        else:
            stepper.PowerOff()


main()
