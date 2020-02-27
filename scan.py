from queue import Queue
import threading, time, socket, sys
import netaddr, keyboard
from multiprocessing import Pool


def get_raw_ip():
    #  for new_ip in reversed(range(2 ** 30)):
    for new_ip in reversed(range(1073741824)):
        yield new_ip


def push_treads(ip):
    thread_scan = threading.Thread(target=func_scan, args=(ip,))  # Запустим поток создания очереди
    thread_scan.start()


def save_ip(ip):
    with open('ip_open_port.txt', 'a') as f:
        f.write(f'{ip}\n')
    print('Сохранили в файл')


def func_scan(inp_ip):

    try:
        ip = str(netaddr.IPAddress(inp_ip))
        sys.stdout.write("\r" + ip)
        sys.stdout.flush()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, 3128))
        sock.close()
        print(f'\n Хост {ip} Доступен')
        save_ip(ip)
    except:
        # print(f'Хост {ip} Недоступен\n')
        pass


def stop_scan():
    while True:
        if keyboard.is_pressed('q'):
            sys.stdout.write('\n Остановка!')
            global stop
            stop = 1
            break
        else:
            pass
        time.sleep(0.1)


if __name__ == '__main__':
    stop = 0
    ##### Запустим поток остановки
    thread_stop = threading.Thread(target=stop_scan)
    thread_stop.start()

    ips = get_raw_ip()
    count_ip = 8000  # Сколько брать из очереди за раз и сколько потоков запускать
    start_t = time.time()
    x = 0
    while True:
        x = x + count_ip
        if stop == 1:
            break
        ip_list = [next(ips) for i in range(count_ip)]
        with Pool(16) as p:
            results = p.map(push_treads, ip_list)  # 1000 потоков на процесс
    end_t = time.time()
    times = end_t - start_t
    print(f'\n Затрачено времени: {round(times)} sec')
    print(f'\n Проверено ip: {x}')
    print(f'\n Скорость: {round(x / times)} host\s')
    print('\n Нажмите любую клавищу для выхода')
    input()
