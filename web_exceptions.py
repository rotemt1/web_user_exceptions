import string


class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, arg, uchar):
        self._arg = arg
        self._uchar = uchar

    def __str__(self):
        return "Provided username %s contains an illegal character \"%s\" at index %s." % self._arg, self._arg.find(self._uchar)

    def get_arg(self):
        return self._arg

    def get_uchar(self):
        return self._uchar

    def uchar_index(self):
        return self._arg.find(self._uchar)


class UsernameTooShort(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided username %s len is shorter than 3." % self._arg

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided username %s len is longer than 16." % self._arg

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided password %s does not meet the conditions. " % self._arg

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided password %s len is shorter than 8. " % self._arg

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided username %s len is longer than 40. " % self._arg

    def get_arg(self):
        return self._arg


class PassUpperCase(PasswordMissingCharacter):

    def __init__(self, arg, problem):
        PasswordMissingCharacter.__init__(self, arg)
        self._problem = problem

    def __str__(self):
        return "The password is missing a character (%s)" % self._problem

    def get_type(self):
        return self._problem


class PassLowerCase(PasswordMissingCharacter):

    def __init__(self, arg, problem):
        PasswordMissingCharacter.__init__(self, arg)
        self._problem = problem

    def __str__(self):
        return "The password is missing a character (%s)" % self._problem

    def get_type(self):
        return self._problem


class PassDigit(PasswordMissingCharacter):

    def __init__(self, arg, problem):
        PasswordMissingCharacter.__init__(self, arg)
        self._problem = problem

    def __str__(self):
        return "The password is missing a character (%s)" % self._problem

    def get_type(self):
        return self._problem


class PassSpecial(PasswordMissingCharacter):

    def __init__(self, arg, problem):
        PasswordMissingCharacter.__init__(self, arg)
        self._problem = problem

    def __str__(self):
        return "The password is missing a character (%s)" % self._problem

    def get_type(self):
        return self._problem


def check_input(username, password):
    for char in username:
        if not(char.isalpha()) and not(char.isnumeric()) and char != '_':
            raise UsernameContainsIllegalCharacter(username, char)

    if len(username) < 3:
        raise UsernameTooShort(username)

    elif len(username) > 16:
        raise UsernameTooLong(username)

    count_special = 0
    count_upper = 0
    count_lower = 0
    count_numbers = 0

    type_special = "Special"
    type_upper = "Uppercase"
    type_lower = "Lowercase"
    type_number = "Digit"

    for char in password:
        if char >= 'A' and char <= 'Z':
            count_upper += 1
        elif char >= 'a' and char <= 'z':
            count_lower += 1
        elif char.isnumeric():
            count_numbers += 1
        elif char in string.punctuation:
            count_special += 1

    if not(count_upper >= 1):
        raise PassUpperCase(password, type_upper)

    elif not(count_lower >= 1):
        raise PassLowerCase(password, type_lower)

    elif not(count_numbers >= 1):
        raise PassDigit(password, type_number)

    elif not(count_special >= 1) :
        raise PassSpecial(password, type_special)

    elif len(password) < 8:
        raise PasswordTooShort(password)

    elif len(password) > 40:
        raise PasswordTooLong(password)

    else:
        return "OK"


def main():

    username1 = input("Enter a username: ")
    password1 = input("Enter a password: ")

    try:
        check_input(username1, password1)

    except UsernameContainsIllegalCharacter as UCIC:
       print("The username contains an illegal character \"%s\" at index" % UCIC.get_uchar(), UCIC.uchar_index())

    except UsernameTooShort as UTS:
        print("The username is too short")

    except UsernameTooLong as UTL:
        print("The username is too long")

    except PassUpperCase as PUC:
        print("The password is missing a character (%s)" % PUC.get_type())

    except PassLowerCase as PLC:
        print("The password is missing a character (%s)" % PLC.get_type())

    except PassDigit as PD:
        print("The password is missing a character (%s)" % PD.get_type())

    except PassSpecial as PS:
        print("The password is missing a character (%s)" % PS.get_type())

    except PasswordTooShort as PTS:
        print("The password is too short")

    except PasswordTooLong as PTL:
        print("The password is too long")




if __name__ == "__main__":
    main()
























