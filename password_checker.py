def checkPasswordStrength(password):
    if len(password) < 8:
        return False

    # Validation criteria & possible results
    criteria = {
        'lower': any(char.islower() for char in password),  
        'upper': any(char.isupper() for char in password),  
        'digit': any(char.isdigit() for char in password),  
        'special': any(not char.isalnum() for char in password),
    }

    # Do the math
    points = sum(criteria.values())

    return points >= 2

# Tests (not my passwords lol)
checkPasswordStrength('Password02')
checkPasswordStrength('!SkyFly250')
checkPasswordStrength('1234567')
checkPasswordStrength('12345678')
