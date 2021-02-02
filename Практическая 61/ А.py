s=input("введите строку:") 
  s1="" 
  for f in s: 
   if f=="а": 
   f="б" 
   elif f=="б": 
   f="а" 
   elif f=="Б": 
   f="А" 
   elif f=="А": 
   f="Б" 
   s1=s1+f
  print(s1)
