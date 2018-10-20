ch=input()
if('A'<=ch<='Z' or 'a'<=ch<='z'):
  if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print("vowel")
  else:
    print("consonant")
else:
  print("invalid")
