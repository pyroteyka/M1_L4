from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1, 1000)
        
        # Получаем данные с API один раз
        self.data = self.get_data()

        self.name = self.get_name()
        self.img = self.get_img()
        self.types = self.get_types()
        self.height = self.get_height()
        self.weight = self.get_weight()
        self.base_experience = self.get_experience()
        self.abilities = self.get_abilities()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_data(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}' 
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def get_name(self):
        return self.data['forms'][0]['name'] if self.data else "Pikachu"

    def get_img(self):
        if self.data:
            return self.data['sprites']['other']['official-artwork']['front_default']
        return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

    def get_types(self):
        if self.data:
            return [t['type']['name'] for t in self.data['types']]
        return ["electric"]

    def get_height(self):
        return self.data['height'] if self.data else 10  # в дециметрах

    def get_weight(self):
        return self.data['weight'] if self.data else 100  # в гекто-граммах

    def get_experience(self):
        return self.data['base_experience'] if self.data else 50

    def get_abilities(self):
        if self.data:
            return [a['ability']['name'] for a in self.data['abilities']]
        return ["static"]

    def info(self):
        return (
            f"Имя: {self.name.title()}\n"
            f"Тип(ы): {', '.join(self.types)}\n"
            f"Рост: {self.height / 10} м\n"
            f"Вес: {self.weight / 10} кг\n"
            f"Опыт: {self.base_experience}\n"
            f"Способности: {', '.join(self.abilities)}"
        )

    def show_img(self):
        return self.img


