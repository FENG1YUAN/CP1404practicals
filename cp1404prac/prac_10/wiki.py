"""
Author: Feng Yuan
Date: 2023-09-22
Time to Complete: 20 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/master/cp1404prac

Pseudo-code:
1. Import the wikipedia module.
2. Define the main function.
   a. Enter a while loop.
   b. Prompt the user to input a page title or search phrase, or to leave blank to exit.
   c. If the user input is blank, break the loop and exit the program.
   d. Within a try-except block:
       i. Fetch the Wikipedia page using the wikipedia.page method, with autosuggest set to False.
       ii. Print the title, summary, and URL of the Wikipedia page.
   e. Handle wikipedia.DisambiguationError, wikipedia.exceptions.PageError, and generic Exception errors.
3. Call the main function if this script is run as the main module.

"""

import wikipedia


def main():
    while True:
        user_input = input("Enter a page title or search phrase (or leave blank to exit): ")
        if not user_input:
            break  # Exit the loop if the input is blank

        try:
            # Fetch the Wikipedia page
            page = wikipedia.page(user_input, autosuggest=False)
            # Print the title, summary, and URL
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
        except wikipedia.exceptions.PageError:
            print(f"No Wikipedia page found for: {user_input}")
        except Exception as e:
            print(f"An error occurred: {e}")

        print("\n")  # Print a newline to separate each iteration


if __name__ == "__main__":
    main()
