import math

# Convert degrees to radians (since math functions use radians)
angle_degrees = float(input("Enter an angle in degrees: "))
angle_radians = math.radians(angle_degrees)

# Calculate sin, cos, and tan
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

# Display the results
print(f"\nAngle: {angle_degrees}°")
print(f"Sin({angle_degrees}°) = {sin_value:.4f}")
print(f"Cos({angle_degrees}°) = {cos_value:.4f}")
print(f"Tan({angle_degrees}°) = {tan_value:.4f}")