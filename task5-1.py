# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок
def exclude(txt:str,string:str):
    # txt=txt.replace(',','')
    # txt=txt.replace('!','')
    # txt=txt.replace('.','')
    # txt=txt.replace('?','')
    # txt=txt.replace(':','')
    # txt=txt.replace(';','')
    # txt=txt.replace('"','')
    # txt=txt.lower()
    result=''
    words=txt.split(' ')
    print (words)
    for word in words:
        if word.find(string) !=-1:
            word=''
        else:
            result+=word+' '
    return result

input_text=input('Введите текст для обработки: ')
needed_string=input('Введите строку, которую будем удалять из текста: ')
result_text=exclude(input_text,needed_string)
print('Текст после обработки: ', result_text)