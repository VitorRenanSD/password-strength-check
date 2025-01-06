def checkPasswordStrength(password):
    while len(password) < 8:
        print('Your password is too short!')
        password = input('Type your password: ')

    # Validation criteria && possible results
    criteria = {
        "lower": any(char.islower() for char in password),  
        "upper": any(char.isupper() for char in password),  
        "digit": any(char.isdigit() for char in password),  
        "special": any(not char.isalnum() for char in password),
    }
    results = {
        4: "Your password is excellent!",
        3: "Your password is good!",
        2: "Your password is weak.",
        1: "Your password is very weak.",
    }

    # Do the math
    points = sum(1 if met else 0 for met in criteria.values())

    print(results.get(points))
    
# Tests
checkPasswordStrength()
checkPasswordStrength()
checkPasswordStrength()
