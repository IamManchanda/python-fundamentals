timesInput = input('How many times do I have to tell you? ')
times = range(int(timesInput))

print(" ")
print("Ohk, Let's go!")
for time in times:
    print(f"{time + 1}: Clean up your room")
