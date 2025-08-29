from password_checker import is_valid_password

correctPasswords = ["Password123"]
incorrectPasswords = ["password", "password123", "Password", "PASSWORD123"]

def testCorrectPasswords():
    correctPasswordString = ", ".join(correctPasswords)
    for password in correctPasswords:
        assert(is_valid_password(password)) == True
    print("% s is Correct" % correctPasswordString) 

def testIncorrectPasswords():
    incorrectPasswordString = ", ".join(incorrectPasswords)
    for password in incorrectPasswords:
        assert(is_valid_password(password)) == False
    print("% s are Incorrect" % incorrectPasswordString)


def test():
    testCorrectPasswords()
    testIncorrectPasswords()

test()