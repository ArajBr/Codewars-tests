'''You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.'''

# Solution

def likes(strn):
    x = len(strn)
    aux = ' like this'
    if x == 0:
        aux = "no one likes this"
    #for i in reversed(range(x)):
    elif x > 3:
        aux = strn[0] + ', ' + strn[1] +  ' and ' + format(x-2) + " others" + aux
    elif x == 3:
        aux = strn[0] + ', ' + strn[1] + ' and ' + strn[2] + aux
    elif x == 2:
        aux = strn[0] + ' and '+ strn[1]  + aux
    else:
        aux = strn[0] + ' likes this'
    return(''.join(aux))







