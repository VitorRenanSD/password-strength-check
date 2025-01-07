def checkPasswordStrength(password):
    validPassword = False
    if len(password) < 8:
        print('Your password is too short. Use another one')
        return

    # Validation criteria & possible results
    criteria = {
        'lower': any(char.islower() for char in password),  
        'upper': any(char.isupper() for char in password),  
        'digit': any(char.isdigit() for char in password),  
        'special': any(not char.isalnum() for char in password),
    }
    results = {
        4: 'Your password is excellent!',
        3: 'Your password is good!',
        2: 'Your password is weak. Use another one',
        1: 'Your password is very weak. Use another one',
    }

    # Do the math
    points = sum(1 if met else 0 for met in criteria.values())
    if points >= 2:
        validPassword = True

    print(results.get(points))
    return validPassword

# Tests (not my passwords lol)
checkPasswordStrength('Password02')
checkPasswordStrength('!SkyFly250')
checkPasswordStrength('1234567')
checkPasswordStrength('12345678')
