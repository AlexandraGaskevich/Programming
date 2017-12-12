with open("Ozhegov.txt", encoding="utf-8") as f:
    for line in f:
        a=line.split("|")
        b=len(a[0])
        if b>=20:
            print(line)
        
            
