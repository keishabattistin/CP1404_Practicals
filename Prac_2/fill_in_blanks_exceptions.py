"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0

while not finished:
    try:
        answer = int(input("Enter an Integer:"))
        finished = True
        pass
    except:
        print("Please enter a valid integer.")
print("Valid result is:", result)
