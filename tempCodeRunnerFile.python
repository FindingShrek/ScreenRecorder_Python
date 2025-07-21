import random

size = 'Regular'
def size_choices(self):
        sizes = {'Small': 30,
                'Medium': 40,
                'Large': 55}
        choice = input('(Small/Medium/Large)\nPlease choose your size: ').title()
        while True:
            if choice in sizes:
                self.size = choice
                return sizes[self.size]
            continue

mainDish = {'Spaghetti': 60,
            'Chicken': 100,
            'Fillet': 55,
            'BurgerSteak': 75}

sideDish = {'Burger': 55,
            'Fries': 50,
            'PeachMangoPie': 35,
            'Sundae': 40}

drinks = {'Coke': size_choices,
          'Sprite': size_choices,
          'Royal': size_choices,
          'Juice': 30,
          'Water': 0} #water is free

# class for values
class TotalOrder():
    def __init__(self, totalValue = 0, 
                 totalChange = 0, 
                 totalPayment = 0, 
                 mainDish=None, 
                 sideDish=None, 
                 drink=None,
                 size='Regular',
                 seniorCitizen=False,
                 receiptBalance=None,
                 valueAddedTax = 0,
                 seniorCitizenValue=0):
        self.totalValue = totalValue
        self.totalChange = totalChange
        self.totalPayment = totalPayment
        self.mainDish = mainDish
        self.sideDish = sideDish
        self.drink = drink
        self.size = size
        self.seniorCitizen = seniorCitizen
        self.seniorCitizenValue = seniorCitizenValue
        self.valueAddedTax = valueAddedTax
        self.receiptBalance = receiptBalance


class OrderSystem(TotalOrder):
    def main_dish_order(self):
        for key in mainDish:
            print(key, end='  ')
        while True:
            customerChoice = input('\nChoose your main dish: ').title().replace(' ', '')
            if customerChoice not in mainDish:
                continue
            self.totalValue += mainDish[customerChoice]
            self.mainDish = customerChoice
            return self.totalValue, self.mainDish 

    def side_dish_order(self):
        for key in sideDish:
            print(key, end='  ')
        while True:
            customerChoice = input('\nChoose your side dish: ').title().replace(' ', '')
            if customerChoice not in sideDish:
                continue
            self.totalValue += sideDish[customerChoice]
            self.sideDish = customerChoice
            return self.totalValue, self.sideDish

    def drinks_order(self):
        for key in drinks:
            print(key, end='  ')
        while True:
            customerChoice = input('\nChoose your drinks: ').title().replace(' ', '')
            if customerChoice not in drinks:
                continue
            elif customerChoice == 'Coke' or customerChoice == 'Sprite' or customerChoice == 'Royal':
                self.size = size_choices(self)
                self.totalValue += self.size
                self.drink = customerChoice
            elif customerChoice == 'Juice' or customerChoice == 'Water':
                self.totalValue += drinks[customerChoice]
                self.drink = customerChoice
            return self.totalValue, self.drink
    def payment_system(self):
        if self.seniorCitizen:
            self.seniorCitizenValue = self.totalValue * 0.20
            self.totalValue -= self.seniorCitizenValue
        self.valueAddedTax += self.totalValue * 0.05
        self.totalValue += self.valueAddedTax
        self.receiptBalance = self.totalValue
        while True:
            try:
                self.totalPayment += int(input(f'\nBalance: {self.totalValue}'
                                    '\nPlease input your payment: '))
                if self.totalPayment < self.totalValue:
                    print('\nInsufficient payment.')
                    self.totalPayment = 0
                    continue
                elif self.totalPayment > self.totalValue or self.totalPayment == self.totalValue:
                    self.totalChange = self.totalPayment - self.totalValue
                    print(f'Your change is: {self.totalChange}')
                    break
            except Exception:
                print('\nPlease input an appropriate number.')
                continue
    def personal_info(self):
        while not self.seniorCitizen:
            senior = input('(Yes/No) \nAre you a senior citizen/PWD?: ').lower()
            if senior == 'yes':
                self.seniorCitizen = True
            elif senior == 'no':
                self.seniorCitizen = False
                break
            else:
                print('\nInvalid input.')
                continue
        
    def receipt_print(self):
        print(f'\nOrder Number: {random.randint(1000,9999)}'
              f'\n\nSenior Citizen/PWD: {self.seniorCitizen}'
              f'\nMain Dish: {self.mainDish}  {mainDish[self.mainDish]}'
              f'\nSide Dish: {self.sideDish}  {sideDish[self.sideDish]}'
              f'\nDrinks: {size} {self.drink}  {self.size}'
              f'\nVAT: {self.valueAddedTax}'
              f'\nSenior Citizen/PWD Discount: {self.seniorCitizenValue}'
              f'\nBalance: {self.receiptBalance}'
              f'\nPayment: {self.totalPayment}'
              f'\nChange: {round(self.totalChange, 2)}')


if __name__ == "__main__":
    order = TotalOrder()
    system = OrderSystem()
    system.main_dish_order()
    system.side_dish_order()
    system.drinks_order()
    system.personal_info()
    system.payment_system()
    system.receipt_print()