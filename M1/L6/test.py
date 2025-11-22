import random
import time

car_pos = 5        # starting position (middle)
road_width = 10    # width of the road
score = 0

print("Car Game")
print("Move the car left (L) or right (R). Avoid the obstacles!")
print("Press Enter to stay in the same spot.\n")

while True:
    # Generate obstacle
    obstacle_pos = random.randint(1, road_width)

    # Show the road
    print("\n" + "-" * (road_width + 2))
    row = ""

    for x in range(1, road_width + 1):
        if x == obstacle_pos:
            row += "X"  # obstacle
        elif x == car_pos:
            row += "A"  # car
        else:
            row += " "

    print("|" + row + "|")
    print("-" * (road_width + 2))

    # Check collision
    if car_pos == obstacle_pos:
        print("\n💥 CRASH! Game Over!")
        print("Your final score:", score)
        break

    # Player move
    move = input("Move (L/R or Enter): ").lower()

    if move == "l" and car_pos > 1:
        car_pos -= 1
    elif move == "r" and car_pos < road_width:
        car_pos += 1

    score += 1
    time.sleep(0.2)