import re
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
stc=input()
fntc=stc+'_stop_genes'
# f what function?
nfile=open(f'{fntc}.fa','w')
h=xfile.read()
genel=h.split('>')
# print(type(genel)) list
# print(type(genel[1])) string
# print(len(genel)) 6614
# print(genel[1]) # normal way
sgene=list() 
for i in range(len(genel)):
    sgene.append(i)
    sgene[i]=re.sub(r'\n','',genel[i])
    n=sgene[i].count(stc)
    if n!=0 and sgene[i].endswith(stc):
        test=genel[i].split('\n')
        for item in test:
            if re.search(r'\S+\scdna.+',item):
                nfile.write('\n>'+re.sub(r'([a-zA-Z0-9_-]+)\scdna.*',r'\1',item)+' '+str(n)+'\n') #\n no.? parenthesis
            else: nfile.write(item)
nfile.close()
prif=open(f'{fntc}.fa')
print(prif.name)
for line in prif:
    print(line[:-1])
