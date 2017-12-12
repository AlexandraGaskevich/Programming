with open("Ozhegov.txt", encoding="utf-8") as f: 
     for line in f: 
         a=line.split("|") 
         b=len(a[0]) 
         if b>=20: 
             print(line)
         c=a[2]
         d=len(c)
         i=0
         if d>0:
             print(c,d)
             i+=1
             print(i)
         


        
        
            
