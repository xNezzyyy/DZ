print("Hello, World")
num_sym="123"
let_sym="XO"
cnt_moves=3
history=[["!", "!", "!"], ["!", "!", "!"], ["!", "!", "!"]]
for i in range(3):
        print(history[i])
order="1"
while cnt_moves>0:
    if cnt_moves%2!=0:
         a=str(input("Игрок1: введите номер столбца, номер строки и X/O без пробелов: "))
    else:
         a=str(input("Игрок2: введите номер столбца, номер строки и X/O без пробелов: "))
    if len(a)==3 and (a[:1] in num_sym and a[1:2] in num_sym and a[2:] in let_sym) and\
          history[int(a[:1])-1][int(a[1:2])-1]=="!" and a[-1]!=order[-1]:
        order=a[-1]
        cnt_moves-=1
        history[int(a[:1])-1][int(a[1:2])-1]=a[-1]
    else: print("Измените исходные данные")
    for i in range(3):
        print(history[i])