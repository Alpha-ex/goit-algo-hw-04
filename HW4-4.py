class AssistantBot:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Контакт {name} додано з номером {phone}.")

    def show_phone(self, name):
        if name in self.contacts:
            print(f"Номер телефону для {name}: {self.contacts[name]}")
        else:
            print(f"Контакт {name} не знайдено.")

    def list_contacts(self):
        if not self.contacts:
            print("Список контактів пустий.")
        else:
            print("Список контактів:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    bot = AssistantBot()

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command == "exit" or command == "close":
            print("Вихід з програми.")
            break
        elif command == "add_contact":
            if len(args) == 2:
                bot.add_contact(args[0], args[1])
            else:
                print("Невірна кількість аргументів. Використовуйте: add_contact <ім' я> <телефон>")
        elif command == "show_phone":
            if len(args) == 1:
                bot.show_phone(args[0])
            else:
                print("Невірна кількість аргументів. Використовуйте: show_phone <Ім'я>")
        elif command == "list_contacts":
            bot.list_contacts()
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()