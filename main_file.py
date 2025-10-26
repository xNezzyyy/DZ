print("Hello, World")
num_sym="123"
let_sym="XO"
cnt_moves=3
history=[["!", "!", "!"], ["!", "!", "!"], ["!", "!", "!"]]
for i in range(3):
        print(history[i])
while cnt_moves>0:
    
    a=str(input("Введите номер столбца, номер строки и X/O без пробелов: "))
    if len(a)==3 and (a[:1] in num_sym and a[1:2] in num_sym and a[2:] in let_sym) and\
          history[int(a[:1])-1][int(a[1:2])-1]=="!":
        cnt_moves-=1
        history[int(a[:1])-1][int(a[1:2])-1]=a[-1]
        #print(cnt_moves)
    else: print("Измените исходные данные")
    for i in range(3):
        print(history[i])

#a=str(input())
#print(num_sym.count(a[:1]))

# mas = ["", "", "", "", "", "", "", "", ""] 
# k=0
# a=3
# # for i in range(a):
# #     for j in range(a): 
# #         mas[i][j] = 0

# #for i in range(0, 9, 3):
# for i in range(9):
#     mas[i]=0
# for i in range(3):
#     print(mas[i], mas[i+1], mas[i+2])
