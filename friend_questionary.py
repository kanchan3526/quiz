print("🔹 Best Friend Questionnaire 🔹\n")

score = 0

# Q1
print("1) What is your friend's favorite color?")
print("1. Blue\n2. Red\n3. Black\n4. Pink")

option = int(input("Enter your choice (1-4): "))

match option:
    case 1:
        score += 1  # Correct answer = Blue

# Q2
print("\n2) What is their favorite food?")
print("1. Pizza\n2. Biryani\n3. Pasta\n4. Burger")

option = int(input("Enter your choice (1-4): "))

match option:
    case 1:
        score += 1  # Correct answer = Pizza

# Q3
print("\n3) What makes them happy the most?")
print("1. Music\n2. Shopping\n3. Sleep\n4. Games")

option = int(input("Enter your choice (1-4): "))

match option:
    case 1:
        score += 1  # Correct answer = Music

# RESULT
print("\n----------------------------------")
print("You scored:", score, "/3")

percent = (score * 100) // 3
print("Friendship level:", percent, "% ❤️")
