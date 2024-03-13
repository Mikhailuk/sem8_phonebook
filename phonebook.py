def input_name():
    return input('Введите имя: ')

def input_surname():
    return input("Введите фамилию: ")

def input_patronumic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите телефон: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronumic} {phone}\n{address}\n\n"

def add_contact():
    contact = create_contact()
    with open('phonebook.txt','a') as f_w:
        f_w.write(contact)

def print_phonebook():
    with open('phonebook.txt','r') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    for i,contact in enumerate(list_contacts,1):
         print(i,contact+'\n')
         
def find_contact():
    search = input('Введите данные для поиска: ')
    print(
            '\nВозможные варианты поиска:\n'
            "1.По фамилии\n"
            "2.По имени\n"
            "3.По отчеству\n"
            "4.По телефону\n"
            "5.По адресу\n"
            )
        
    var = input("Выберите вариант поиска: ")
    while var not in ('1','2','3','4','5'):
        print('Некорретные данные')
        var = input("Выберите вариант поиска: ")
    i_var = int(var)-1
    with open('phonebook.txt','r') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    for contact in list_contacts:
        contact_lst = contact.split()
        if search in contact_lst[i_var]:
            print(f"\n{contact}")
            
def copy_contact():
    print_phonebook()
    user_id = int(input('Выберете id-пользователя для копирования: '))
    
    with open('phonebook.txt','r') as f_r:
        con_list = f_r.read().rstrip().split("\n\n")
    for i,contact in enumerate(con_list,1):
         if user_id == i:
             with open('reserve.txt','a') as f_a:
                f_a.write(contact+'\n\n')
                print('Запись успешно внесена')
         elif  user_id <= 0 or user_id >= len(con_list)+1:
                 print('\nid-пользователя введён некорректно')
                 break
                 
def ui():
    with open('phonebook.txt','a'):
        pass
    choise = '0'
    while choise !='5':
        print(
            '\nВозможные варианты действий:\n'
            "1.Добавление нового контакта\n"
            "2.Вывод данных на экран\n"
            "3.Поиск контакта\n"
            "4.Копирование контакта\n"
            "5.Выход\n"
            )
        
        choise = input("Выберите вариант действия: ")
        while choise not in ('1','2','3','4','5'):
            print('Некорретные данные')
            choise = input("Выберите вариант действия: ")
        match choise:
            case '1':
                add_contact()
                pass
            case '2':
                print_phonebook()
                pass
            case '3':
                find_contact()
                pass
            case '4':
                copy_contact()
            case '5':
                print('Всего доброго!')


ui()


    
        
