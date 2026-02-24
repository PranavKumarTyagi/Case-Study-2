#Pranav Kumar Tyagi
#Roll No-202501100700106
#ECE-B

import random
import time

# Accept min and max temperature from user
min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))

print("\nStarting Temperature Monitoring System...\n")

while True:
    # Generate random temperature between 0 and 100
    temperature = random.uniform(0, 100)

    print(f"Current Temperature: {temperature:.2f} °C")

    # Compare with limits
    if temperature > max_limit:
        print("Alert: Temperature is too high")
    elif temperature < min_limit:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")

    print("." * 40)

    # Wait for 2 seconds
    time.sleep(2)