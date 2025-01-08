def checkPasswordStrength(password):
    if len(password) < 8:
        return False

    # Validation criteria
    criteria = {
        'lower': any(char.islower() for char in password),  
        'upper': any(char.isupper() for char in password),  
        'digit': any(char.isdigit() for char in password),  
        'special': any(not char.isalnum() for char in password),
    }

    points = sum(criteria.values())

    return points >= 2 # Boolean


# Tests
passwords = [
    'Password02',  # True
    '!SkyFly250',  # True
    '1234567',     # False
    '12345678',    # False
    'pass',        # False
    'WeakPass!',   # True
]

for pwd in passwords:
    print(f'Testing: {pwd}')
    result = checkPasswordStrength(pwd)
    print(f'Valid: {result}\n')
