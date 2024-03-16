class FoodCollection:
    def __init__(self):
        self.food_list = []

    def add_food(self, food):
        self.food_list.append(food)

    def get_food_list(self):
        return self.food_list
