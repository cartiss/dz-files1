cook_book = {}

class Dish:
    def __init__(self, name, ing_list):
        self.name = name
        self.ing_list = ing_list


class Ingredient:
    def __init__(self, ingredient_name, quantity, measure):
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.measure = measure

with open('ing.txt', 'r', encoding="utf-8") as file:
    file_list = file.read()
    file_list = file_list.split('\n\n')

    for dish in file_list:
        temp_list = []
        dish = dish.split('\n')
        new_dish = Dish(dish[0], dish[2:])
        for ing in new_dish.ing_list:
            ing = ing.split(' | ')
            new_ing = Ingredient(ing[0], ing[1], ing[2])
            temp_dict = {'ingredient_name': new_ing.ingredient_name, 'quantity': new_ing.quantity, 'measure': new_ing.measure}
            temp_list.append(temp_dict)
        cook_book.setdefault(new_dish.name, temp_list)

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish_list, value in cook_book.items():
        for dish in dishes: # перебираю массив с блюдами
            if dish == dish_list: # нахожу блюдо в словаре cook_book
                for ingredients in value: # перебираю ингредиенты в списке блюда
                    temp_dict2 = {'quantity': int(ingredients['quantity']) * person_count, 'measure': ingredients['measure']} # в словарь записываю значения quantity и measure
                    for key_, value_ in result.items(): # проверка на повторяющиеся ингредиенты
                        if key_ == ingredients['ingredient_name']:
                            continue
                    result.setdefault(ingredients['ingredient_name'], temp_dict2) # записываю результат в словарь result
    return result

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))