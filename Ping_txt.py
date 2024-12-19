import os

with open("IP.txt", 'r') as f_in: 
    with open("IP_out.txt", 'w') as f_out: 
        for line in f_in:
            line = line.strip()
            response = os.system(f"ping -n 1 {line}") #Windows '-n 1', Linux/macOS '-c 1'.
            if response == 0:
                status = 'is up!'
            else:
                status = 'is down!'
            f_out.write (f'{line} - {status}\n')
            print(f'{line} {status}')
print('finish')
