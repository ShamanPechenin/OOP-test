class Human:
    def __init__(self, name, age, favourite_food):
        self.name = name
        self.age = age
        self.favourite_food = favourite_food

    def _check_restricted_food(self, food_name):
        if self.age >= 18:
            return False
        if food_name in ["beer", "vodka", "alcohol"]:
            return True

    def eat(self, food_name):
        food_name = food_name.lower().strip()
        print(f"{self.name} Tries to eat {food_name}...")
        if self._check_restricted_food(food_name):
            print("He can't eat that!")
            return
        if food_name == self.favourite_food:
            print("Tasty!")
            return
        print("Meh...")


class AllergicHuman(Human):
    def __init__(self, name, age, favourite_food, allergic_food):
        super(AllergicHuman, self).__init__(name=name, age=age, favourite_food=favourite_food)
        self.__allergic_food = allergic_food

    def _check_restricted_food(self, food_name):
        if food_name in self.__allergic_food:
            return True
        if self.age >= 18:
            return False
        if food_name in ["beer", "vodka", "alcohol"]:
            return True


artoms = Human("Artoms", 18, "banana")
sergejs = AllergicHuman("Sergejs", 17, "cacao", "peanuts")

artoms.eat("cacao")
artoms.eat("banana")
artoms.eat("vodka")
artoms.eat("peanuts")

sergejs.eat("cacao")
sergejs.eat("banana")
sergejs.eat("vodka")
sergejs.eat("peanuts")
