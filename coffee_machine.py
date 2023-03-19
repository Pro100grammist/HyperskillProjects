class CoffeeMachine:

    def __init__(self):
        self.cmd = None
        self.milk = 540  # ml
        self.water = 400  # ml
        self.beans = 120  # g
        self.cups = 9  #
        self.cash = 550  # $

    def main_menu(self):
        self.cmd = input('Write action (buy, fill, take, remaining, exit): ')
        if self.cmd == 'exit':
            exit()
        elif self.cmd == 'buy':
            self.make_coffee()
        elif self.cmd == 'fill':
            self.fill_coffee_machine()
        elif self.cmd == 'take':
            self.extract_money()
        elif self.cmd == 'remaining':
            self.show_balance()
            self.main_menu()

    def make_coffee(self):
        select = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        acc_msg = 'I have enough resources, making you a coffee!'
        if select == '1':
            if not self.water >= 250:
                print('Sorry, not enough water!')
                self.main_menu()
            if not self.beans >= 16:
                print('Sorry, not enough coffee beans!')
                self.main_menu()
            if not self.cups >= 1:
                print('Sorry, not enough coffee cups!')
                self.main_menu()
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.cash += 4
            print(acc_msg)
            self.main_menu()

        elif select == '2':
            if not self.water >= 350:
                print('Sorry, not enough water!')
                self.main_menu()
            if not self.milk >= 75:
                print('Sorry, not enough milk!')
                self.main_menu()
            if not self.beans >= 20:
                print('Sorry, not enough coffee beans!')
                self.main_menu()
            if not self.cups >= 1:
                print('Sorry, not enough coffee cups!')
                self.main_menu()
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.cash += 7
            print(acc_msg)
            self.main_menu()

        elif select == '3':
            if not self.water >= 200:
                print('Sorry, not enough water!')
                self.main_menu()
            if not self.milk >= 100:
                print('Sorry, not enough milk!')
                self.main_menu()
            if not self.beans >= 12:
                print('Sorry, not enough coffee beans!')
                self.main_menu()
            if not self.cups >= 1:
                print('Sorry, not enough coffee cups!')
                self.main_menu()
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.cash += 6
            print(acc_msg)
            self.main_menu()

        elif select == 'back':
            self.main_menu()

        else:
            print('Available only three kinds of coffee')

    def fill_coffee_machine(self):
        water = int(input('Write how many ml of water you want to add: '))
        if water > 0:
            self.water += water
        milk = int(input('Write how many ml of milk you want to add: '))
        if milk > 0:
            self.milk += milk
        beans = int(input('Write how many grams of coffee beans you want to add: '))
        if beans > 0:
            self.beans += beans
        cups = int(input('Write how many disposable cups you want to add: '))
        if cups > 0:
            self.cups += cups
        self.main_menu()

    def extract_money(self):
        print(f'I gave you ${self.cash}')
        self.cash = 0
        self.main_menu()

    def show_balance(self):
        print(f'The coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n'
              f'{self.beans} g of coffee beans\n{self.cups} disposable cups\n${self.cash} of money')


cm = CoffeeMachine()
cm.main_menu()
