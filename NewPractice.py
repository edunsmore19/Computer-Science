##NewPractice.py

doorknobs = ["brass", "iron", "diamond", "gold"]
switchMe = []

print(*doorknobs)

switchMe.append(doorknobs[1])
switchMe.append(doorknobs[3])

doorknobs[1] = switchMe[1]
doorknobs[3] = switchMe[0]

print(*doorknobs)