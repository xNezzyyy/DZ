print("Hello, World")
num_sym="123"
let_sym="XO"
cnt_moves=9
hist=[["!", "!", "!"], ["!", "!", "!"], ["!", "!", "!"]]
for i in range(3):
        print(hist[i])
order="1"
while cnt_moves>0:
    if cnt_moves%2!=0:
         a=str(input("Игрок1: введите номер столбца, номер строки и X/O без пробелов: "))
    else:
         a=str(input("Игрок2: введите номер столбца, номер строки и X/O без пробелов: "))
    if len(a)==3 and (a[:1] in num_sym and a[1:2] in num_sym and a[2:] in let_sym) and\
          hist[int(a[:1])-1][int(a[1:2])-1]=="!" and a[-1]!=order[-1]:
        order=a[-1]
        cnt_moves-=1
        hist[int(a[:1])-1][int(a[1:2])-1]=a[-1]
    else: print("ИЗМЕНИТЕ ИСХОДНЫЕ ДАННЫЕ")
    for i in range(3):
        print(hist[i])
    if cnt_moves<=4:
         if hist[0][0]==hist[1][1]==hist[2][2] or hist[0][0]==hist[1][0]==hist[2][0] or hist[0][1]==hist[1][1]==hist[2][1]\
         or hist[0][2]==hist[1][2]==hist[2][2] or hist[0][0]==hist[0][1]==hist[0][2] or hist[1][0]==hist[1][1]==hist[1][2]\
         or hist[2][0]==hist[2][1]==hist[2][2] or hist[0][2]==hist[1][1]==hist[2][0]:
              if cnt_moves%2==0:
                   print("ПОБЕДИЛ Игрок1")
              else:
                   print("ПОБЕДИЛ Игрок2")
              break
              
