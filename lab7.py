#1
hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")

count_ffd = hashes.count("ffd222")
print("Количество вхождений:", count_ffd)


#2
users = ("guest", "moderator", "admin", "root")

index_admin = users.index("admin")
print("Индекс admin:", index_admin)


#3
key_params = ("AES", 256, "CBC")

algorithm, key_size, mode = key_params
print("Algorithm:", algorithm)
print("Key size:", key_size)
print("Mode:", mode)


#4
log = ("login", "download", "upload", "logout")
print(log[-1])


#5
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
entered_ip = input("Enter ip: ")

if entered_ip in ips:
    print('Found')
else:
    print('Not found')


#6
name = input("Имя: ")
role = input("Роль: ")
status = input("Статус: ")

user = (name, role, status)
print(user)


#7
access = ("read", "write", "execute")
new_value = input("Введите новое значение для второго элемента: ")

new_access = (access[0], new_value, access[2])
print(new_access)


#8
attempts = ("success", "fail", "fail", "success", "fail", "fail")
cnt_success = attempts.count("success")
cnt_fail = attempts.count("fail")

print("success: ", cnt_success)
print("fail: ", cnt_fail)


#9
admins = ("root", "admin")
users = ("alex", "bob")

combined = admins + users
print(combined)


#10
logs = ("login", "upload", "download", "logout")

start, *middle, end = logs

print("Start:", start)
print("Middle:", tuple(middle))
print("End:", end)


"""
КОНТРОЛЬНЫЕ ВОПРОСЫ:
1. Кортеж - неизменяемый класс, тогда как списки- изменяемые обьекты.
2. Кортеж считается безопаснее списков потому что там нельзя случайно изменить какой-то элемент,
это бывает нужно при хранении информации,больших данных.
3. Нет, напрямую изменить элемент кортежа нельзя.
4. Упаковка - создание кортежа из значений, распаковка- разбиение кортежа на значения
5. count()- считает колличество вхождений элемента, а index()- возвращает индекс первого элемента
6. Да, использование скобок для создания кортежа необязательно.
7.Кортежи подходят для того, что должно быть зафиксировано:
    параметры шифрования, права доступа, хэши, настройки политик,
    статические таблицы, неизменяемые конфигурации.
Так как изменить кортеж нельзя — меньше риска повреждения данных.

"""
