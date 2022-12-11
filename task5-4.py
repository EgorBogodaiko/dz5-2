# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом: 
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&
import string

def to_cort(list1,list2):
    list2 = [x.upper() for x in list2]
    result=list(zip(list1,list2))
    return result

def elem_filter_or_correct(element):
    index,lang = element
    print(index,lang)
    sum_points=0
    for sym in lang:
        sum_points+=int(ord(sym))
    print(sum_points)
    if sum_points%index==0:
        element=sum_points,lang
        print(element)
    else: element =''
    return element

def filter_and_correct(list_elems):
    list_elems=[elem_filter_or_correct(x) for x in list_elems]
    list_elems=list(filter(lambda x: x!='', list_elems))
    print(list_elems)
    return list_elems
    # list=filter(lambda x: x[0]%(ord(x[0])))

lang=['python', 'c#','pascal','c++','c+','fortran','sql']
index=[x+1 for x in range(len(lang)+1)]
print(lang,index)
ind_lang=to_cort(index,lang)
print(ind_lang)
filter_and_correct(ind_lang)
