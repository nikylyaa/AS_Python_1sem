# удаление цифр из файла
def remove_digits(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    result = ""
    for smvl in text:
        if smvl < '0' or smvl > '9':
            result = result + smvl
    f = open(filename, 'w')
    f.write(result)
    f.close()
    
# подсчёт символов в файле
def count_smvl(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return len(text)

# подсчёт строк в файле
def count_lines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return len(lines)
