# assistant_bot.py
"""
Команди:
  hello
  add <name> <phone>
  change <name> <new_phone>
  phone <name>
  all
  close / exit
"""


def parse_input(user_input: str):
    """
    Розбирає рядок користувача на команду та аргументи.
    Повертає (command, *args), де command у нижньому регістрі.
    """
    parts = user_input.split()

    if not parts:
        return "", []

    cmd, *args = parts

    return cmd.strip().lower(), args


def add_contact(args, contacts: dict) -> str:
    """
    Додає контакт у словник у форматі name -> phone.
    Очікує рівно два аргументи: ім'я та телефон.
    """
    if len(args) != 2:
        return "Invalid command."

    name, phone = args

    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    """
    Оновлює номер телефону існуючого контакту.
    Очікує рівно два аргументи: ім'я та новий телефон.
    """

    if len(args) != 2:
        return "Invalid command."

    name, new_phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = new_phone

    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    """
    Повертає номер телефону для вказаного імені.
    Очікує рівно один аргумент: ім'я.
    """

    if len(args) != 1:
        return "Invalid command."
    
    name = args[0]

    if name not in contacts:
        return "Contact not found."
    
    return contacts[name]


def show_all(contacts: dict) -> str:
    """
    Повертає усі збережені контакти у вигляді кількох рядків:
      name: phone
    Якщо контактів немає — повертає порожній рядок.
    """
    
    if not contacts:
        return ""
    
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    
    return "\n".join(lines)


def main():
    contacts = {}
    
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            out = show_all(contacts)
            print(out if out else "")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
