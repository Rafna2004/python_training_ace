def ageChecker(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "kid"
    else:
        return "adult"

print(ageChecker(100))