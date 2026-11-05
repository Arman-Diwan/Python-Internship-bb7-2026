def make_greeting(language):

    def greet(name):
        if language == "hindi":
            print("Namaste,", name)
        else:
            print("Hello,", name)

    return greet


english = make_greeting("english")
hindi = make_greeting("hindi")

english("Arman")
hindi("Arman")