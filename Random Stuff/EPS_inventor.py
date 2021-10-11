import random

range_duration = range(30, 60, 5)
range_BPM = range(150, 175)

duration = random.choice(range_duration)
BPM = random.choice(range_BPM)

if duration - 60 >= 0:
    duration -= 60
    print(f"1h{duration} - {BPM} BPM")
else:
    print(f"<p>Séance de Workout<br>{duration} minutes - {BPM} BPM</p>")


