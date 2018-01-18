fin=open('input.txt','r')
line=fin.readlines()
for x in line:
    if '/' in x:
        n1,n2=x.split('/')
        print(int(n1)/int(n2))
    if '*' in x:
        n1,n2=x.split('*')
        print(int(n1)*int(n2))
    if '+' in x:
        n1,n2=x.split('+')
        print(int(n1)+int(n2))
    if '-' in x:
        n1,n2=x.split('-')
        print(int(n1)-int(n2))
fin.close()
