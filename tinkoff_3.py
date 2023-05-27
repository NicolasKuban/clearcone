##clients_count, timeout = map(int, input().split())
##
##clients = {i:level for i, level in enumerate(map(int, input().split()))}
##client_timeout = int(input())
##
clients_count, timeout = map(int, '6  4'.split())
clients = {i:level for i, level in enumerate(map(int, '1  2  3  6  8  25'.split()))}
client_timeout = 5

print(clients_count, timeout)
print(clients)
print(client_timeout)

longtime = {}
for key_parent, value_parent in clients.items():
    longtime[key_parent] = {}
    for key_child, value_child in clients.items():
        longtime[key_parent][key_child]=abs(value_parent - value_child)
        

for i in longtime.items():
    print(i)

client_timeout_list = longtime[client_timeout]
for i in range(clients_count):
    # Список клиентов
    check_list = list(range(clients_count))
    # берем минимальное время в словаре клиента который уходит

    first = min(longtime[client_timeout], key=longtime[client_timeout].get)
    a = client_timeout_list.pop(first)
    print(a)
    print(f'{first = }')
    if first < timeout:
        continue
##    result = 0
##    while check_list:
##        print(check_list.pop(0))
##        
