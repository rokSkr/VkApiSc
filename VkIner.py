mess = ("Standard value ")
## Терминальное приложение для различных ищменений в страницы VK

## Импортирование библиотеки vk_api
import vk_api
## Переменные
errorc = ("Была выбранна неверная комманда,повторите запрос, так: \n 1. Не используя буквы \n 2. Не нудно вводить цифры номера меню")
rlp = ("""__________.Вводить номер по такому примеру: \n __________.+71234567890. \n __________.почту по такому примеру: \n __________.google@gmail.com.""")
merror_msg = ("Вы ввели не правельный логин /пороль(Как вводить пороль логин:)" + rlp)

## Интерфейс

print("/\/\/\/\/\* Ваши данные не будут переданны 3-им лицам, все что вы введете останется только в переменной vklog, vkpass) ")
print("/\/\/\/\/\* Для чего нужны эти данные вы можите прочитать в вложенном файле 'Sefety Information.txt'")
vklog =  input (""" Введите логин пользователя  (номер телефона,ел.почта)\n __________.Вводить номер по такому примеру: \n __________.+71234567890. \n __________.почту по такому примеру: \n __________.google@gmail.com. \n Введите логин: """ )
vkpass = input("Введите пароль: ")
def main():
    vk_session = vk_api.VkApi(vklog, vkpass)
    
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(merror_msg)
        return
        vk= vk_session.get_api()

a = (""" ( 0-0 ) Полная информация по странице \n ( 0-1 ) Флуд по странице \n ( 0-2 ) Управление профилем \n ( 0-3 )  Информация по текущей сессии /n ( 0-4 ) Выход """)
print (a)
menu = int (input("Выберите: "))
## Вывод информации по пользователю

if int (menu)== (0):
     vkid = input("Введите id пользователя:")

## Информация по текущей сессии
if int (menu) == (3):
    def infosess (api_version = api_version, login = vklog, password = vkpass, client_secret =None, token = None):
        print ("( 3-0 )Допольнительные настройки входа ")
        print (" ( 3-1 )Информация о текущей сессии") 
        check_sid()
## Запуск флуда

if int (menu)== (1):
     print("flood")
## Выход из приложения

if int (menu) == (4):
    print("Exited... \n ////// \n Enter command 'python Vkiner.py, for continue'")
## Управление профилем
if int (menu) == (2):
    bm = print("""Выберите действие которое хотите совершить в вашем аккаунте: \n ( 2-0 ) Запостить сообщение на вашем аккаунте от именни ' hello world' \n ( 2-1 ) Удалить фотографии с вашего аккаунта \n ( 2-2 ) Удалить все видеозаписи с вашего аккаунта \n ( 2-3 ) Удалить всех друзей \n ( 2-4 ) Установка фотографии профиля \n ( 2- 5 ) Скачать все фотографии выдоженные с этого аккаунта \n ( 2-5 ) Скачать все видео выложенные с этого аккаунта \n ( 2-6 ) Скопировать всю музыку с этого аккаунта \n ( 2-7 ) Скачать все изображения с этого аккаунта(которые были отправлены) \n ( 2-8 ) Скачать все видеозаписи с этого аккаунта(которые были отправлены) \n ( 2-9 ) Салянка ( Все вместе) \n ( 2-10 ) Назад""")
## Выбор меню 2
    menu1 = int (input("Inject: ")) 
## Работа постинга

    if int (menu1) == (0):
        mess = input("Введите сообщение поста: ")
        vk_session = vk_api.VkApi(vklog, vkpass)
        vk_session.auth()
        vk = vk_session.get_api()
        print(vk.wall.post(message= mess))
## Установка фотографии профиля
    if int (menu1) == (4):
        setph = input("Введите путь к изображению: ")
        def chph (login = vklog, password = vkpass, token =None):
            vk_session = vk_api.VkApi(vklog, vkpass)
        vk_session.auth()
        vk = vk_session.get_api()
        def photo_profile(setph, owner_id=None, crop_x=None, crop_y=None, crop_width=None):
            values = {}
        if owner_id:
            values['owner_id'] = owner_id
            crop_params = {} 
        if crop_x is not None and crop_y is not None and crop_width is not None:
            crop_params['_square_crop'] = '{},{},{}'.format( crop_x, crop_y, crop_width ) response = self.vk.photos.getOwnerPhotoUploadServer(**values)
            url = response['upload_url'] 
            with FilesOpener(photo, key_format='file') as photo_files: 
            response = self.http.post( url, data=crop_params, files=photo_files )
        return     self.vk.photos.saveOwnerPhoto(**response.json())    
    if int (menu1) == (1):
        print("Не багуется...")
## При выходе ( 2-4 ):
    if int (menu1)== 10:
        menu1 - 11
        print(a)
        menuw24 = input("Inject: ")
## Циклы


# Цикл меню

while menu>4:
    print(a)
    print("Была выбранна неверная комманда...")
    menuw1 = int (input("Выберите: "))
    if int (menuw1)== (0):
        vkid = input("Введите id пользователя: ")
    if int (menuw1)== (1):
        vkid1 = input("Введите id пользователя: ")
    
    if int (menuw1) == (2):
        menuw1 = int (input ("Введите сообщение поста: "))
    if int (0):
        messw = input("Введите сообщение поста:   ")
    vk_session = vk_api.VkApi(vklog, vkpass)
    vk_session.auth()
    vk = vk_session.get_api()
    print(vk.wall.post(message = messw))
    if int (menuw) == (3):
        print("Exited... \n ////// \nEnter command 'python Vkiner.py', for continue")
# Цикл ( 0-2 )
while menu1>4:
    print(bm)
    print(errorc)
    menuw2 = int (input ("Введите сообщение поста: "))
    if int (0):
        messw = input("Введите сообщение поста:   ")
    vk_session = vk_api.VkApi(vklog, vkpass)
    vk_session.auth()
    vk = vk_session.get_api()
    print(vk.wall.post(message = messw))
# Цикл "Назад"( 2-4 )
    