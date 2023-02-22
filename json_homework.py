import json

with open('phonebook_data.json') as data:
    user_data = data.read()
users = json.loads(user_data)

print('Type "add" if you want to add new users, type "search" if you want to find user info, type "delete"\n'
      'if you want to delete a record, type "update" if you want to update the record, type "quit" if you want\nto leave'
      ' the program')

def first_name_search(first_name):
    users_record = []

    for i in users:
        record = i.get("name")

        if first_name == record:
            users_record.append(f'{i["name"]} {i["surname"]}, phone number:{i["telephone"]}, city:{i["city"]}')

    return users_record if len(users_record)>0 else None

def second_name_search(second_name):
    users_record = []

    for i in users:
        record = i.get("surname")

        if second_name == record:
            users_record.append(f'{i["name"]} {i["surname"]}, phone number:{i["telephone"]}, city:{i["city"]}')

    return users_record if len(users_record)>0 else None

def full_name_search(first_name,second_name):
    users_record = []
    for i in users:

        record1 = i.get("surname")
        record2 = i.get("name")

        if second_name == record1 and record2 == first_name:
            users_record.append(f'{i["name"]} {i["surname"]}, phone number:{i["telephone"]}, city:{i["city"]}')

    return users_record if len(users_record)>0 else None

def city_search(city_name):
    users_record = []
    for i in users:

        record = i.get("city")

        if city_name == record:
            users_record.append(f'{i["name"]} {i["surname"]}, phone number:{i["telephone"]}, city:{i["city"]}')

    return users_record if len(users_record)>0 else None

def delete_record(phone_num):
    for i in users:
        record = i.get("telephone")

        if record == phone_num:

            index = users.index(i)
            users.pop(index)
            print('You successfully deleted the record!')
            break
    else:
        print('There is no such telephone!')

def update_record(phone_num):
    for i in users:

        record = i.get("telephone")

        if record == phone_num:

            index = users.index(i)
            new_name = input('Enter your new first name ').lower()
            new_last_name = input('Enter your new second name ').lower()
            new_telephone = input('Enter your new phone number ').lower()
            new_city = input('Enter your new city name ').lower()

            users[index]["name"] = new_name
            users[index]["surname"] = new_last_name
            users[index]["telephone"] = new_telephone
            users[index]["city"] = new_city

            return 'You successfully updated info!'
    else:
        return 'There are no such users!'
while True:
    user_choice = input('Enter your choice >>> ')
    if user_choice == 'add':

        name = input('Enter your first name ').lower()
        last_name = input('Enter your second name ').lower()
        telephone = input('Enter your phone number ').lower()
        city = input('Enter your city name ').lower()

        data_dict = {}

        data_dict["name"] = name
        data_dict["surname"] = last_name
        data_dict["telephone"] = telephone
        data_dict["city"] = city

        users.append(data_dict)
    elif user_choice == 'search':
        search_choice = input('Search by first name,second name,full name or city?')

        if search_choice == 'first name':
            name = input('Enter the first name ')
            result = first_name_search(name)

            if result == None:
                print('There are no such users')

            else:
                for i in result:
                    print(i)
        elif search_choice == 'second name':

            name = input('Enter the second name ')
            result = second_name_search(name)

            if result == None:
                print('There are no such users')

            else:
                for i in result:
                    print(i)
        elif search_choice == 'full name':

            first_name = input('Enter the first name ')
            second_name = input('Enter the second name ')
            result = full_name_search(first_name,second_name)

            if result == None:
                print('There are no such users')

            else:
                for i in result:
                    print(i)
        elif search_choice == 'city':

            name = input('Enter the city name ')
            result = city_search(name)

            if result == None:
                print('There are no such users')

            else:
                for i in result:
                    print(i)

    elif user_choice == 'delete':
        phone_num = input('Enter the phone number ')
        delete_record(phone_num)

    elif user_choice == 'update':
        phone_num = input('Enter the phone number ')
        x = update_record(phone_num)
        print(x)

    elif user_choice == 'quit':
        with open('phonebook_data.json','w') as data: # дуже дивно,але в json файлі все записується в один рядок ...
            new_data = json.dumps(users)
            data.write(new_data)
            exit()
    else:
        print('Invalid input!')
        user_choice = input('Enter your choice >>> ')
