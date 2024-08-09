import webbrowser
from recipe_parser import RecipeParser

class ConversationBot:
    def __init__(self, recipe):
        self.recipe = recipe
        self.current_step = 0

    def start_conversation(self):
        print(f"Let's start working with '{self.recipe.title}'")

        while True:
            print("\nWhat do you want to do?")
            print("[1] Go over ingredients list")
            print("[2] Go over recipe steps")
            print("[3] Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.show_ingredients()
            elif choice == '2':
                self.handle_steps()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def show_ingredients(self):
        print("\nIngredients:")
        for ingredient in self.recipe.ingredients:
            print(ingredient)

    def handle_steps(self):
        while True:
            print("\nWhat do you want to do?")
            print("[1] Show current step")
            print("[2] Go to next step")
            print("[3] Go back one step")
            print("[4] Exit to main menu")
            choice = input("Enter choice: ")

            if choice == '1':
                self.show_current_step()
            elif choice == '2':
                self.next_step()
            elif choice == '3':
                self.previous_step()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def show_current_step(self):
        if 0 <= self.current_step < len(self.recipe.steps):
            print(f"Step {self.current_step + 1}: {self.recipe.steps[self.current_step]}")
        else:
            print("No more steps.")

    def next_step(self):
        if self.current_step < len(self.recipe.steps) - 1:
            self.current_step += 1
            self.show_current_step()
        else:
            print("This is the last step.")

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_current_step()
        else:
            print("This is the first step.")

    def answer_how_to(self, query):
        search_query = query.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
