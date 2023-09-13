#✅ 1. Demonstrate First Class Functions
import ipdb;
#🛑 first class function: stored as variables, in data structures, passed as arguments, etc.
#🛑 higher order function: fxns that operate on other fxns

def walk(pet):
    print(f'{pet} has been walked')
def feed(pet):
    print(f'{pet} has been fed')

#✅ 1a. Create functions to be used as callbacks 
#✅ 1b. Create a higher-order function that will take a callback as an argument
def higher_order(func, pet):
    func(pet)
#higher_order(walk, "Momo")
#✅ 2. Higher order functions
#✅ 2a. Create a higher-order function that returns a function

#✅ 3. Create a higher-order function that returns two functions

def higher_order_two():
    def brushed(pet):
        print(f'{pet} has been brushed')
    def play(pet):
        print(f'{pet} has played')
    return [brushed,play]
#test = higher_order_two()[1]("Momo")

#✅ 4. Demonstrate how to create a decorator
# Create a function that:
#✅ 4a. takes a function as an argument, 
#✅ 4b. has an inner function, and 
#✅ 4c. returns the inner function

#✅ Decorator (coupon_calculator)
def coupon_calculator(func):
    print(f'in coupon calculator')
    def print_price(price):
        return(f'in print_price Initial Price={func(price)}') #final result
    return print_price

#✅ Inner Function
#✅ Callback function to Calculate New Price
@coupon_calculator #coupon_calculator(calculate_price)
def calculate_price(price):
    print(f'in calculate price')
    return f'{price/2}'

# invoke calculate price
# calculate price is passed into coupon calculator
# coupon calculator invokes calculate price
# coupon calculator invokes inner function (print_price)
# print_price is returned as final value


print(f'invoke calculateprice {calculate_price(8)}')
ipdb.set_trace()