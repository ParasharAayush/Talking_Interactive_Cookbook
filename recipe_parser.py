import requests
from bs4 import BeautifulSoup

class Recipe:
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

class RecipeParser:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        response = session.get(self.url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content[:500]}")

        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception("Failed to fetch the webpage.")

    def parse_recipe(self):
        # Find the title
        title_element = self.soup.find('h1', class_='article-heading type--lion')
        if not title_element:
            raise Exception("Failed to find the recipe title.")
        
        title = title_element.get_text().strip()

        # Extract ingredients
        ingredients = []
        ingredients_list = self.soup.find('ul', class_='mm-recipes-structured-ingredients__list')
        if not ingredients_list:
            raise Exception("Failed to find the ingredients.")

        ingredients_items = ingredients_list.find_all('li', class_='mm-recipes-structured-ingredients__list-item')
        for item in ingredients_items:
            quantity = item.find('span', attrs={"data-ingredient-quantity": "true"}).get_text(strip=True)
            unit = item.find('span', attrs={"data-ingredient-unit": "true"}).get_text(strip=True)
            name = item.find('span', attrs={"data-ingredient-name": "true"}).get_text(strip=True)
            
            # Combine quantity, unit, and name into a single string
            ingredient = f"{quantity} {unit} {name}".strip()
            ingredients.append(ingredient)

        # Extract steps
        steps = []
        steps_list = self.soup.find('ol', id='mntl-sc-block_1-0')
        if not steps_list:
            raise Exception("Failed to find the recipe steps.")

        steps_items = steps_list.find_all('li')
        for step in steps_items:
            step_text = step.find('p').get_text(strip=True)
            steps.append(step_text)

        return Recipe(title, ingredients, steps)

    def get_recipe(self):
        self.fetch_page()
        return self.parse_recipe()
