# Dictionary and It's Methods
# student = {
#     'name': 'John Doe',
#     'age': 21,
# }

# address = dict(city='Bhubaneswar', state='Odisha', country='India', pin=751030)
# print(student)
# print(address)
# print(student["age"])
# print(address['country'])

#Adding new key-value pair to dictionary
# student['department'] = 'Computer Science'
# print(student)
#Updating existing key-value pair in dictionary
# student['name'] = 'Smith'
# print(student)
#Removing key-value pair from dictionary
# del student['age']
# print(student)

# for k in address:
#     print(k)
#     print(address[k])

# print(address)
# for key, val in address.items():
#     print(key, val)
#     print(f"{key} : {val}")

# name = "Smith"
# age = 22
# print('Hello my name is ', name, 'and I am', age, 'years old.')
# print(f'Hello my name is {name} and I am {age} years old.')
# print('Hello my name is {} and I am {} years old.'.format(name, age))


# Inbuilt methods
# s1 = student
# s1['age'] = 20
# print(s1)
# print(student)
# s2 = student.copy()
# s2['age'] = 25
# print(s2)
# print(student)

course = {
    'name': 'Python Programming',
    'duration': '3 months',
    'fees': 15000,
    'discount': 5000,
    'rating': 4.5
}

# print(course.keys())
# print(course.values())
# print(course.items())
# print(course.get('name'))
# print(course.get('instructor', 'Not Assigned'))
# print(course.pop('discount'))
# print(course)
# print(course.popitem())
# print(course)
# course.clear()
# print(course)
# course.update({'instructor': 'Jane Doe', 'level': 'Beginner', 'rating': 4.7})
# print(course)
# course.setdefault('language', 'English')

# List and It's Methods
l1 = [100, 20,10, 30, 10, 40, 50]
l2 = list((60, 70, 80, 90, 100))
# print(l1)
# print(l2)

# Update elements to list
# l1[2] = 15
# print(l1)

#Methods
# print(len(l1))

#Adding elements to list
# l1.append(60)
# l1.append(70)
# print(l1)
# l1.extend(l2)
# print(l1)
# l1.insert(2, 25)
# print(l1)

#Removing elements from list
# l1.remove(10)
# print(l1)
# a = l1.pop()
# print(a)
# print(l1)
# l1.clear()
# print(l1)

#Searching & Counting elements in list
# print(l1.index(10))
# print(l1.count(10))

#Sorting elements in list
# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

l1.sort(reverse=True)
print(l1)

l3 = l1.copy()
print(l3)