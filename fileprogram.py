def charcount(filename):
    linecount=0
    wordcount=0
    charcount=0
    with open(filename,"r") as f:
        for line in  f:
            linecount+=1
            wordcount+=len(line.split())
            charcount+=len(line)
    print(linecount)
    print(wordcount)
    print(charcount)
def create(filename,content):
    with open(filename,'w')as f:
        f.write(content)

filename="shreesha.txt"
content="""excel pu college 574224
            belthangady"""

create(filename,content)
charcount(filename)
