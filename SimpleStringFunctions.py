Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
#[GCC 6.3.0 20170124] on linux
#Type "copyright", "credits" or "license()" for more information.
person={}
person['name'] = 'Nowell Strite'
person.update({'favorites': [42, 'food'],'gender' : 'male',})
print(person)

person.keys()
dict_keys(['gender', 'favorites', 'name'])
person.values()


person.get('gender','Anonymous')
person.get('gender','Anonymous')

friut =', '.join(['Pineapple', 'Orange', 'Papaya'])
print(fruit)

name = '%(first)s %(last)s '% {'first':'Nowell','last':'Strite'}
print(name)

 
