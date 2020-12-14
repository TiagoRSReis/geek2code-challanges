'''###### Basico ######
import random
password = random.randrange(10000)
for i in range(0,10000):
    guesspass=i
    if i == password:
        break
print(password)
print(i)
'''

########## medio ########### 
'''import string
import random
import time
import multiprocessing
num= str(1234567890)
letras=string.ascii_letters + num

password = random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) 
#password = "aaaaaaaa"
gesspass=[0,0,0,0,0,0,0,0]
for frs in letras:
    gesspass[0]=frs
    for scd in letras:
        gesspass[1]=scd
        for ter in letras:
            gesspass[2]=ter
            for quar in letras:
                gesspass[3]=quar
                for qui in letras:
                    gesspass[4]=qui  
                    for sex in letras:
                        gesspass[5]=sex     
                        for set in letras:
                            gesspass[6]=set         
                            for oit in letras:
                                gesspass[7]=oit
                                gesspass_str = ''.join(map(str, gesspass)) 
                                print(str(gesspass_str))
                                #time.sleep(5)
                                if gesspass_str == password:
                                    break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

print('you guess')
print(gesspass_str)
print(password)'''

####### advanced #########
import string
import random
import itertools
num= str(1234567890)
#letras=string.ascii_letters + num
letras=string.printable
print(letras)
k=int(input('inserir numero de carateres \n'))

password="".join(random.sample(letras,k))
print(password)

for s in itertools.product(letras, repeat=k):
    #print("".join(s))
    gesspass="".join(s)
    if password == gesspass:
        break
print('You guess')