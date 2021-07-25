print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
)

print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

print("""
***********************************
** What would you like to order? **
***********************************
"""
)

snake_order = {'Wings':0, 'Cookies':0, 'Spring Rolls':0, 'Salmon':0, 'Steak':0, 'Meat Tornado':0, 'A Literal Garden':0, 'Ice Cream':0, 'Cake':0, 'Pie':0, 'Coffee':0, 'Tea':0, 'Unicorn Tears':0}



orders=[]

while(True):
    my_order = input('> ')
    my_order=my_order.capitalize()

    
    if(my_order in snake_order):

        snake_order[my_order] += 1
        counter = snake_order[my_order]
        print(f'** {counter} order of {my_order} have been added to your meal **')

    elif (my_order == 'quit'):
        break


# x = 1
# if (my_order in orders):
#         x=+1
    
# else:
#         x=1

# if (my_order.capitalize() in snake_order):
#         print(f'** {x} order of {my_order} have been added to your meal **')
# else:
#         print(f'sorry {my_order} is not in the menu')



