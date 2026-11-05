def make_validator(min_value):

    def validate(number):
        if number >= min_value:
            print(number, "is valid")
        else:
            print(number, "is not valid")

    return validate


validator1 = make_validator(10)
validator2 = make_validator(50)

print("Validator 1:")
validator1(15)
validator1(5)

print("Validator 2:")
validator2(60)
validator2(30)