import math
import random
# 1:
def one():
    try:
        a = int(input("Number: "))
        if a % 2:
            print("odd")
        else:
            print("even")
    except ValueError:
        print("Not an integer!")

# 2:
def two(count=20):
    sum=0
    top=0
    for i in range(count):
        temp = random.randint(10, 99)
        if top < temp:
            top = temp
        sum += temp
    print(sum/count, top)

# 3:
def three(v1:tuple, v2:tuple):
    num = 0
    for i in range(len(v1)):
        num += v1[i]*v2[i]
    den = 1
    for v in v1, v2:
        vlen = 0
        for i in v:
            vlen += i**2
        den *= math.sqrt(vlen)
    print(num/den)

# 4 (what the author probably meant, "... lists all integers *in the list* that...):
def four(l:list, c:int):
    for i in l:
        if i > l[0] and i < l[-1] and i % c == 0:
            print(i)

# 4 (what is written):
def four(l:list, c:int):
    for i in range(l[0], l[-1]):
        if not i % c:
            print(i)

# 5: (assuming any list. With sortable it could go quicker as sorting 2 lists would still be nlogn with another logn
# from the matching?)
def five(l1:list, l2:list):
   for i in l1:
       for j in l2:
           if i == j:
               print(i)

# 6:
def six(text:str, letter:str):
    print(text.replace(letter, ''))

# 7:
def seven(text:str):
    alphas = 0
    digits = 0
    for i in text:
        if i.isalpha():
            alphas += 1
        if i.isdecimal():
            digits += 1
    print(alphas, digits)

# 8:(could be done with generating all binary masks and XORing too! (and would be faster. And wouldn't give duplicates):
def eight(l:list):
    if l == []:
        pass
    else:
        print(l)
        for i in l:
            templ = l[:]
            templ.remove(i)
            eight(templ)

# 9:
def nine(text:str):
    res=sorted(text, key=lambda i: text.count(i))
    print(res[0], res[-1])

# 10: (since python does this oob with `f'{number:b}'` f.e.: print(f'{123:b}') will print `1111011` I assume this needs
# to be done manually
def ten(number:int):
    if number == 0:
        pass
    elif number == 1:
        print(1, end='')
    elif number % 2:
        ten(int(number/2))
        print(1, end='')
    else:
        ten(int(number/2))
        print(0, end='')
if __name__ == "__main__":
    one()
    two()
    three((1, 0), (0, 1))
    three((1, 0), (2, 0))
    four([3, 4, 5, 6, 7], 2)
    five([1, 2, 3, 4], [2, 4, 6, 8])
    six('Lorem ipsum sit amet', 'm')
    seven('j3ZpuW0PaQSfBAphKYg8')
    eight([1,2,3,4])
    nine('It actually did remind him of a spider, in fact. One particular genus that had become legendary among invertebrate zoologists and computational physicists alike: a problem-solver that improvised and drew up plans far beyond anything that should have been able to fit into such a pinheaded pair of ganglia. Portia. The eight-legged cat, some had called it. The spider that thought like a mammal.')
    ten(1337)
