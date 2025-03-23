x = input('enter text: ')
char = x[0]
def count_char_occurrences(strng, char):
    count = 0
    for i in strng:
        if i == char:
             count+=1
    return count
print(count_char_occurrences(x,char))