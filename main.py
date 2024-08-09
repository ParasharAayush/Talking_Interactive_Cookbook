from recipe_parser import RecipeParser
from conversation_bot import ConversationBot

def main():
    url = input("Please enter the URL of the recipe: ")
    parser = RecipeParser(url)
    recipe = parser.get_recipe()

    bot = ConversationBot(recipe)
    bot.start_conversation()

if __name__ == "__main__":
    main()
