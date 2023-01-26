import os
import random
import requests
from bs4 import BeautifulSoup
import re

url = "https://pt.wikipedia.org/wiki/Brasil"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = soup.get_text()

content_list = text.split()

random_word = random.choice(content_list)

while (not random_word.isalpha()) or (len(random_word) < 4) or (bool(re.search('[áéíóúãõâêîôû]', random_word))):
    random_word = random.choice(content_list)


chave = random_word.lower()
count = 0
acertos = ''

#print(random_word)

while True:
    count += 1        
    user_letra = input ('Digite uma letra: ')
    if len(user_letra)>1:
        print('Digite uma letra de cada vez')
        print ('Tentativa', count)
        continue  
    print ('Tentativa', count)

    if user_letra in chave:
        acertos += user_letra

    i = 0 
    temp = ''   
    for letra in chave:  
        if letra in acertos:            
            temp += letra
        else:
            temp += '*'         
    
    print ('Palavra: ',temp) 
    if temp == chave:
        os.system('cls')        
        print('Parabéns, você acertou')
        print('A palavra era:', chave.upper())
        break

    if count>20:
        print('Número máximo de tentativas')
        print('A palavra era:', chave.upper())
        break

print('FIM')
    
        

