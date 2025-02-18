#importing modules

import random
import itertools

#setting lists up
# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# veggies = ['broccoli','carrots','cauliflour','peppers','salad']
# cuisines = ['chinese', 'greek', 'middle eastern', 'mexican', 'italian']
# days = ['M' , 'T', 'W', 'H', 'F']


#returning list of protiens - WORKED
# def protiens (protiens):
#     for protien in protiens:
#         msg = f'I want {protien} for dinner'
#         print(msg)

# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# protiens(protiens)

#returning list of randomized protiens, then not as message - WORKED
#https://www.w3schools.com/python/ref_random_shuffle.asp
# def random_protiens (protiens):
#     random.shuffle(protiens)
#     for protien in protiens:
#         # msg = f'I want {protien} for dinner'
#         # print(msg)
#         print(protien)

# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# random_protiens(protiens)


#iterating through lists with three parts - WORKED
#https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/
# def dinner (protiens, veggies, cuisines):
#     for (protien, veggie, cuisine) in zip(protiens,veggies,cuisines):
#         msg = f'I want {cuisine.title()} {protien} with {veggie} for dinner'
#         print(msg)

# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# veggies = ['broccoli','carrots','cauliflour','peppers','salad']
# cuisines = ['chinese', 'greek', 'middle eastern', 'mexican', 'italian']
# dinner(protiens, veggies, cuisines)

#adding weeknight
# def dinner (protiens, veggies, cuisines, days):
#     for (protien, veggie, cuisine, day) in zip(protiens,veggies,cuisines, days):
#         msg = f'I want {cuisine.title()} {protien} with {veggie} for dinner on {day}.'
#         print(msg)

# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# veggies = ['broccoli','carrots','cauliflour','peppers','salad']
# cuisines = ['chinese', 'greek', 'middle eastern', 'mexican', 'italian']
# days = ['Monday' , 'Tuesday', 'Wendesday', 'Thursday', 'Friday']
# dinner(protiens, veggies, cuisines,days)

#shuffling three parameter - WORKED
# def dinner (protiens, veggies, cuisines, days):
#     random.shuffle(protiens)
#     random.shuffle(veggies)
#     random.shuffle(cuisines)
#     for (protien, veggie, cuisine, day) in zip(protiens,veggies,cuisines, days):
#         msg = f'I want {cuisine.title()} {protien} with {veggie} for dinner on {day}.'
#         print(msg)

# protiens = ['chicken', 'beef', 'tofu', 'shrimp', 'salmon']
# veggies = ['broccoli','carrots','cauliflour','peppers','salad']
# cuisines = ['chinese', 'greek', 'middle eastern', 'mexican', 'italian']
# days = ['Monday' , 'Tuesday', 'Wendesday', 'Thursday', 'Friday']
# dinner(protiens, veggies, cuisines, days)


# ###Creating User input section for protiens
# print('You will need to enter 5 protiens, 5 veggies, and 5 cusines.')
# user_protiens = input('enter protiens: ' )
# _user_protiens = user_protiens.split(',')
# #print(_user_protiens)
# user_veggies = input('enter veggies: ' )
# _user_veggies = user_veggies.split(',')
# print(_user_veggies)
# user_cuisines = input('enter cusiines: ')
# _user_cuisines = user_cuisines.split(',')
# print(_user_cuisines)


#adding input to def

print('You will need to enter 5 protiens, 5 veggies, and 5 cusines.')
user_protiens = input('enter protiens: ' )
_user_protiens = user_protiens.split(',')
# print(_user_protiens)
user_veggies = input('enter veggies: ' )
_user_veggies = user_veggies.split(',')
# print(_user_veggies)
user_cuisines = input('enter cusiines: ')
_user_cuisines = user_cuisines.split(',')
# print(_user_cuisines)

def dinner (_user_protiens, _user_veggies, _user_cuisines, day):
    random.shuffle(_user_protiens)
    random.shuffle(_user_veggies)
    random.shuffle(_user_cuisines)
    for (_user_protiens, _user_veggies, cuisine, day) in zip(_user_protiens,_user_veggies,_user_cuisines, day):
        msg = f'We are going to have {cuisine.title()} {_user_protiens} with {_user_veggies} for dinner on {day}.'
        print(msg)

day = ['Monday' , 'Tuesday', 'Wendesday', 'Thursday', 'Friday']
dinner(_user_protiens, _user_veggies, _user_cuisines, day)