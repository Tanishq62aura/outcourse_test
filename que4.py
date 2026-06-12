class UnderAgeError(Exception):
    pass
class InvalidAgeError(Exception):
    pass

class AgeVerification:
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        elif age < 18:
            raise UnderAgeError("Under age")
        elif age > 100:
            raise InvalidAgeError("Invalid age")
        else:
            print("Valid age!")
    
obj = AgeVerification()
try:
    age = int(input("Enter age: "))
    obj.set_age(age)
except ValueError as e:
    print(e)
except UnderAgeError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
finally:
    print("Program ended.")