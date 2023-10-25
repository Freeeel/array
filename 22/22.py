class Validator:
    def isEmail(self, str):
        if ('@' in str) and ('.' in str):
            return True
        else:
            return False

    def isDomain(self, str):
        if '.' in str:
            return True
        else:
            return False

    def isNumber(self, str):
        for i in str:
            if not i.isdigit():
                return False
        return True

validator = Validator()

print(validator.isEmail('adsasark@gmail.ru'))
print(validator.isEmail('sadsfsaa@com'))

print(validator.isDomain('sasdk.com'))
print(validator.isDomain('racte!com'))

print(validator.isNumber('128435'))
print(validator.isNumber('abdsf123'))