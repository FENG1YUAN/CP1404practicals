"""
CP1404/CP5632 - Practical
FENG YUAN

Emails to Names
Estimate: 25 minutes
Actual: 19 minutes
Pseudo-code:

The code uses the main function to prompt users for their email addresses and determines plausible names from the
emails. Each name is then displayed alongside the email for confirmation.

Using the function extract_name_from_email(email), it splits the email prefix before the "@" symbol, forms a name
by joining the components, and converts them to title case.

The main function collects emails in a loop until the user provides an empty input. It then pairs the extracted
or provided name with its corresponding email in a dictionary. Finally, the email-name pairs are printed out.
"""


def extract_name_from_email(email):
    """Extract a plausible name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    """Store and display user's emails and names."""
    emails_to_names = {}

    email = input("Email: ")
    while email:
        name = extract_name_from_email(email)
        correct = input(f"Is your name {name}? (Y/n) ").lower()

        if correct == 'n' or correct == 'no':
            name = input("Name: ")

        emails_to_names[email] = name
        email = input("Email: ")

    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


if __name__ == '__main__':
    main()
