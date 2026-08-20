class Apple:
    def display(self):
        print("This is Apple")


class Mango:
    def display(self):
        print("This is Mango")


class Orange:
    def display(self):
        print("This is Orange")


class FruitFactory:
    @staticmethod
    def get_fruit(fruit_name):

        if fruit_name.lower() == "apple":
            return Apple()

        elif fruit_name.lower() == "mango":
            return Mango()

        elif fruit_name.lower() == "orange":
            return Orange()

        else:
            return None


choice = input("Enter fruit (Apple/Mango/Orange): ")

fruit = FruitFactory.get_fruit(choice)

if fruit:
    fruit.display()
else:
    print("Invalid fruit")