
tictactoel=["  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",
            "--------------",
            "  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",
            "--------------",
            "  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",
            "  ","|", "  ","|","  ",

]

a=0
count=0

while a < 47:
  print (tictactoel[a], end="")
  a+=1
  count+=1
  if count %5==0:
    print()
  if count ==16:
    print()
    count =0

a= input("Do you want to be X or O?")
flag=1
while flag:
  if a== 'X' or a == "x":
    print("You have the first turn")
    flag=0
  elif a =="O" or a =="o" :
    print("You have the second turn")
    flag=0
  else:
    a=input("Please, give valid character")
a="X "

notfinished=1
evenodd=0
winner="nobody"
full=0
l=[0,0,0,0,0,0,0,0]
while notfinished:
  char = int(input(a+"'s turn.Please give a number between 1-9 "))
  temp =3
  temp += char*2
  if char >3 and char <7:
    temp= 19
    temp += (char-3)*2
  elif char >6 and char <10:
    temp=35
    temp += (char-6)*2

  if tictactoel[temp]!="  ":
    print("not available")
    continue
  else:
    tictactoel[temp]=a
    full+=1
    if char==1:
      if a== "X ":
        l[0]-=1
        l[3]-=1
        l[6]-=1
      elif a == "O ":
        l[0]+=2
        l[3]+=2
        l[6]+=2

    elif char==2:
      if a=="X ":
        l[0]-=1
        l[4]-=1

      elif a == "O ":
        l[0]+=2
        l[4]+=2


    elif char==3:
      if a=="X ":
        l[0]-=1
        l[5]-=1
        l[7]-=1
      elif a == "O ":
        l[0]+=2
        l[5]+=2
        l[7]+=2

    elif char==4:
      if a=="X ":
        l[1]-=1
        l[3]-=1

      elif a == "O ":
        l[1]+=2
        l[3]+=2

    elif char==5:
      if a=="X ":
        l[1]-=1
        l[4]-=1
        l[6]-=1
        l[7]-=1
      elif a == "O ":
        l[1]+=2
        l[4]+=2
        l[6]+=2
        l[7]+=2

    elif char==6:
      if a=="X ":
        l[1]-=1
        l[5]-=1

      elif a == "O ":
        l[1]+=2
        l[5]+=2

    elif char==7:
      if a=="X ":
        l[2]-=1
        l[3]-=1
        l[7]-=1
      elif a == "O ":
        l[2]+=2
        l[3]+=2
        l[7]+=2

    elif char==8:
      if a=="X ":
        l[2]-=1
        l[4]-=1

      elif a == "O ":
        l[2]+=2
        l[4]+=2


    elif char==9:
      if a=="X ":
        l[2]-=1
        l[5]-=1
        l[6]-=1
      elif a == "O ":
        l[2]+=2
        l[5]+=2
        l[6]+=2

    if -3 in l:
      notfinished=0
      winner="X"
    elif 6 in l:
      winner="O"
      notfinished=0

    i=0
    count=0
    while i < 47:
      print (tictactoel[i], end="")
      i+=1
      count+=1
      if count %5==0:
        print()
      if count ==16:
        print()
        count =0
  if notfinished==0:
      print(winner+" won!")
      break
  if full==9:
      print("nobody won")
  evenodd+=1

  if evenodd%2==0:
    a="X "
  else:
    a="O "
