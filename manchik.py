import re

list_1 = open('C:/phytonProjects/lesson0/Homework/text3.txt', 'w', encoding='utf-8')
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    patn = re.sub(r"[\([{«,.:;—»})\]]","", text)
    list_1.write(patn)
    list_1.close()
    f.close()

def Sortirovka(*args):

    list_3 = open('text4.txt', 'w+', encoding='utf-8')

    with open('text3.txt', 'r+', encoding='utf-8') as list_2:
        f_text = list_2.read()
        print(type(f_text))
        f_text_1 = f_text.lower()
        f_text_2 = f_text_1.split()
        f_text_3 = list(set(f_text_2))
        for items in f_text_3:
            list_3.write('%s\n' % items)
    list_3.close()



Sortirovka()
