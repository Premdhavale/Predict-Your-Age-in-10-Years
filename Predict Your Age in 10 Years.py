# Ask the user to enter their name
name = input("What is your name? ")

# Ask the user to enter their age
age = int(input("How old are you? "))  # We convert the input to an integer

# Calculate the future age
future_age = age + 10

# Display the result
print("Hello", name + "!", "In 10 years you will be", future_age, "years old.")
