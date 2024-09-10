def q1(s):
    print(f"s")


def q2():
    s = input("Введите строку:")
    print(s[-1])


def q3():
    s1 = input("Введите строку:")
    s2 = input("Введите подстроку:")

    if s1[len(s1)-len(s2):] == s2:
        return True
    return False


def q4():
    s1 = input("Введите строку:")
    s2 = input("Введите подстроку:")

    if s1[:len(s2)] == s2:
        return True
    return False


def q5():
    s1 = input("Введите строку:")
    s2 = input("Введите подстроку:")

    if s2 in s1:
        return True
    return False


def q6():
    s1 = input("Введите строку:")
    s2 = input("Введите подстроку:")
    s = len(s1.split(s2)[0])
    print(s)


def q7():
    text = input("Введите текст:")
    text_to_words = []
    text_to_words_count = []
    words = ''
    count = 0
    for i in text:
        if i == '.':
            text_to_words.append(words)
            text_to_words_count.append(count)
            words = ''
            count = 0

        else:
            if i == ' ':
                count += 1
                words += i
            else:
                words += i

    for i in range(len(text_to_words_count)):
        print(text_to_words[text_to_words_count.index(max(text_to_words_count))])
        text_to_words_count[text_to_words_count.index(max(text_to_words_count))] = 0


def q8():
    s1 = input("Введите строку:")
    arr = [i for i in s1]
    print(arr)


def q9():
    s1 = input("Введите строку:")
    s1 = s1.replace(' ', '-')
    print(s1)


def q10():
    s1 = input("Введите строку:")
    arr = ['']
    i = 0
    for j in s1:
        if j == ' ':
            i += 1
            arr.append('')
        else:
            arr[i] += j
    print(arr)


def q11():
    s1 = input("Введите строку:")
    char = input("Введите символ:")[0]
    arr = ['']
    i = 0
    for j in s1:
        if j == ' ':
            i += 1
            arr.append('')
        else:
            arr[i] += j

    arr = [i for i in arr if i[0] ==  char]
    print(arr)



def q12():
    s1 = input("Введите строку:") + ' '
    final = ''


    for i in range(len(s1)-1):
        if s1[i+1] == ' ':
            final += s1[i].upper()
        else:
            final += s1[i]
    print(final)


def q13():
    s = ''
    for i in range(11):
        s += 'A'
    print(s)


def q14():
    s1 = input("Введите строку:")
    n = int(input("Введите количество слов:"))
    arr = ['']
    i = 0
    j = 0
    while (j < len(s1)) and (len(arr) <= n):
        if s1[j] == ' ':
            i += 1
            arr.append('')
            j += 1
        else:
            arr[i] += s1[j]
            j += 1
    del arr[-1]
    print(arr)


def q15():
    s1 = input("Введите строку:").lower()
    target = '1234567890'
    for i in s1:
        if i not in target:
            print(False)
            return False
    print(True)




if __name__ == "__main__":
    q15()