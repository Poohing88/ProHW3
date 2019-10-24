

class Contact:
    def __init__(self, name, lastname, number, choise=False, *agrs, **kwargs):
        self.name = name
        self.lastname = lastname
        self.number = number
        self.choise = choise
        self.agrs = agrs
        self.kwargs = kwargs

    def __str__(self):
        if self.choise:
            chois = "Да"
        else:
            chois = "Нет"
        print(f'Имя: {self.name}\nФамилия: {self.lastname}\nНомер: {self.number}\nВ избранных: {chois}')
        print('Дополнительная информация:')
        print(f'Допольнительные номера:')
        for namber in self.agrs:
            print(namber)
        for key, value in self.kwargs.items():
            print(f'{key}: {value}')
        return "Это вся информация о пользователе в телефонной кинге"


class PhoneBook:
    def __init__(self, name, list_contact):
        self.name = name
        self.list_contact = list(list_contact)

    def out(self):
        for i in self.list_contact:
            print(i)

    def creat(self, name, lastname, number, choise=False, *agrs, **kwargs):
        contact = Contact(name, lastname, number, choise=False, *agrs, **kwargs)
        self.list_contact.append(contact)
        return contact

    def add(self, Contact):
        self.list_contact.append(Contact)
        return self.list_contact

    def remove(self, number):
        for contact in self.list_contact:
            if contact.number == number:
                self.list_contact.remove(contact)
        return self.list_contact

    def find_choise(self):
        for contact in self.list_contact:
            if contact.choise:
                print(contact)

    def find_name(self, name, lastname):
        for contact in self.list_contact:
            if contact.name == name and contact.lastname == lastname:
                print(contact)


def test():
    namesen = Contact('mikle', 'mikki', '0000', choise=True, f='ffff', ggdg='lmkmk')
    nuber = Contact('Pooh', 'Serman', '+798767657', True, '65478545')
    igor = Contact('igor', 'alfenyr', '645637')
    list_1 = [namesen, nuber]
    book = PhoneBook('book', list_1)

    book.out()
    book.creat('egor', 'asiliev', '78554646')
    book.add(igor)
    print('______________________________________________________')
    book.out()
    book.remove('645637')
    print('______________________________________________________')
    book.out()
    print('______________________________________________________')
    book.find_choise()
    print('______________________________________________________')
    book.find_name('Pooh', 'Serman')


test()