# # def outer(n,y):        # внешняя функция
# #     # n = 5           # лексическое окружение - локальная переменная
# #     def add():
# #         nonlocal n,y
    
# #         return n + y
    
# #     def inner():      # локальная функция
# #         nonlocal n
# #         n += 1        # операции с лексическим окружением
# #         print(n)
# #     outer.add = add
# #     # print( outer.add) 
# #     return outer

# # a = outer(5,12)
# # print( a.add() ) 


# # def outer():
# #     x = 0
# #     def inner():
# #         nonlocal x
# #         x += 1
# #         print(x)
# #     return inner 


# # def calculate(a:int,b:int):
# #     def add():
# #         nonlocal a,b
# #         return a + b
    
# #     def multiply():
# #         nonlocal a,b
# #         return a * b
    
# #     def divide():
# #         nonlocal a,b
# #         return a / b
# #     calculate.add = add
# #     calculate.multiply = multiply
# #     calculate.divide = divide
# #     return calculate

# # c = calculate(10,5)
# # print(c.add() )
# import time


# def timer():
#     start = time.time()

#     def inner():
#         return time.time() - start
#     return inner


# def avg_numbers():
#     summa = 0
#     cnt = 0
#     def inner(number):
#         nonlocal  summa
#         nonlocal  cnt
#         summa += number
#         cnt += 1
#         print('Summa ', summa)
#         return summa // cnt
#     return inner


# def counter(func):
#     cnt = 0
#     def inner(*args, **kwargs):
#         nonlocal  cnt
#         cnt += 1
#         print(f" {func.__name__} {cnt} marta chaqirildi")
#         return func(*args, **kwargs)
#     return inner

# @counter
# def add_(a,b):
#     return a + b

# print( add_(2,5) )






# x = 0.1
# y = 0.2
# import decimal

# r = x + y
# r = decimal.Decimal( str(r ))
# print( r.quantize( decimal.Decimal('0.01')) )



# x = decimal.Decimal(str(x))
# y = decimal.Decimal(str(y))

# print(x+y)



# def f(name):
#     cnt = 0
#     def inner():
#         nonlocal cnt
#         cnt += 1
#         print(f" Hello {name} count = {cnt} ")
#     return inner

# r = f("Olim")

# r() 


# def calculate(x,y):
#     """Calculates the value"""
#     assert type(x) in (int, float) , "Invalid value type for x"
#     assert type(y) in (int, float) , "Invalid value type for y"
#     limit = 10
#     work = 0

#     def add():
#         nonlocal work
#         work += 1 
#         if work == limit:
#             return False
#         print( limit )
#         # limit += 1
#         return x + y
    
#     def multiply():
#         # limit += 1 
#         return x * y
#     calculate.add = add
#     calculate.multiply = multiply

# c = calculate(10,12)
# print(  calculate.add()  )    
# print(  calculate.add()  )    
# print(  calculate.multiply()  )    



