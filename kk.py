def likes(lst):
    a = len(lst)
    if a == 0:
        return('no one likes this')
    elif a == 1:
        return(f'{lst[0]}ы likes this')
    elif a == 2:
        return(f'{lst[0]} and {lst[1]} like this')
    elif a == 3:
        return(f'{lst[0]}, {lst[1]} and {lst[2]} like this')
    else:
        return(f'{lst[0]}, {lst[1]} and {a-2} like this')


lst_0 = []
lst_1 = ['Alex']
lst_2 = ['Alex', 'Bob']
lst_3 = ['Alex', 'Bob', 'Margo']
lst_4 = ['Alex', 'Bob', 'Margo', 'Elizabet']
lst_5 = ['Alex', 'Bob', 'Margo', 'Elizabet', 'David']

print(likes(lst_0))
print(likes(lst_1))
print(likes(lst_2))
print(likes(lst_3))
print(likes(lst_4))
print(likes(lst_5))