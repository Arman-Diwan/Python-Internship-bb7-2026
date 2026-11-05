height_cm = "175"
weight_kg = "68.5"

# Convert string values into numeric types
height_cm = int(height_cm)
weight_kg = float(weight_kg)

# Convert height from cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / (height_m * height_m)

print("Height:", height_m, "meters")
print("Weight:", weight_kg, "kg")
print("Your BMI is:", bmi)