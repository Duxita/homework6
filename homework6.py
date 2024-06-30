my_dict = {'Andrey': 1982,'Svetlana': 1985, 'Polina': 2006, 'Viktoriya': 2007}
print('Dict:', my_dict)
print('Existing value:',my_dict.get('Polina'))
print('Not existing value:',my_dict.get('Stesha','Имя отсутствует'))
my_dict.update({'Sergey': 2004, 'Roma': 2001})
a = my_dict.pop('Svetlana')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)
my_set = {'start',5,8,9,5,2,6,2,'stop','start', True}
print('Set:',my_set)
my_set.add(45)
my_set.add(33)
my_set.discard(9)
print('Modified set:',my_set)