import re
import linecache as lc
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
nfile=open('TGA_genes.fa','w')
count=0
q=0
for line in xfile:
    count=count+1
    if line.startswith('>'):
        if count != 1:
            h=lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',count-1)
            if h.endswith('TGA\n'):
                ini=lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',q)
                nfile.write(re.sub(r'(>[a-zA-Z0-9_-]+)\scdna.*',r'\1',ini))
                for i in range(q+1,count):
                    nfile.write(lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',i))
        q=count
if lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',count).endswith('TGA\n'):
    ini=lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',q)
    nfile.write(re.sub(r'(>[a-zA-Z0-9_-]+)\scdna.*',r'\1',ini))
    for i in range(q+1,count):
        nfile.write(lc.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',i))
nfile.close()
tst= open('TGA_genes.fa')
for line in tst:
    print(line[:-1])   
print(q)
print(count)

