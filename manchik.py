import re
list_1 = open('C:/phytonProjects/lesson0/Homework/text3.txt', 'w', encoding='utf-8')
with open('text.txt', 'r', encoding='utf-8') as f:
    #print("utf-8")
    text = f.read()
    patn = re.sub(r"[\([{«,.:;—»})\]]","", text)
    #print(patn)
    list_1.write(patn)
    list_1.close()
    f.close()

def Sortirovka(*args):

    list_3 = open('text4.txt', 'w+', encoding='utf-8')
    f1_text = list_3.read()
    list_3.close()
    with open('text3.txt', 'r+', encoding='utf-8') as list_2:
        f_text = list_2.read()
        list_2.close()
        for number in f_text.split():
            if number in f1_text.split():
                continue
            else:
                f1_text.
        return f1_text



Sortirovka(patn)
#print(list_2)
# print()
# print()
# print(Anton_loh(list_2))