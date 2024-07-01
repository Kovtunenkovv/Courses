import os

with open("IP.txt", 'r') as f_in: 
    with open("IP_out.txt", 'w') as f_out: 
        for line in f_in:
            response = os.system("ping -n 1 " + line)
            if response == 0:
                f_out.write(str(line).replace("\n","") + ' : is up!' + "\n")
                print(line.replace("\n","") + 'is up!')
            else:
                f_out.write(str(line).replace("\n","") + ' : is down!' + "\n")
                print(line.replace("\n","") + ' is down!')    
print('finish')
