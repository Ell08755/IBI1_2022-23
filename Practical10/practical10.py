# task1 Mortgage affordability calculator
def afford (v,s):
    '''
    input: salary and house value, numeric
    returns Yes if house value<=5times annual salary
            No  if house value>5 times annual salary
    '''
    if v<=5*s:
        return 'Yes'
    else:
        return 'No'
print('value=10000, salary=1',afford(10000,1)) #example test
value=int(input('value='))
salary=int(input('salary='))
print(afford(value,salary))

# task2 Triathlon times database
class triathlon(object):
    '''
    first and last name
    location
    time for each 3 disciplines (swim, cycle, run)
    total time
    '''
    def __init__(self,firstname,lastname,location,swim,cycle,run):
        self.firstname=firstname
        self.lastname=lastname
        self.location=location
        self.swim=swim
        self.cycle=cycle
        self.run=run
        self.total=swim+cycle+run
    def fulldata(x):
        print(x.__dict__)
    def datavalue(x):
        print(x.firstname,x.lastname,x.location,x.swim,x.cycle,x.run,x.total)
example=triathlon('Jerry', 'Hanna','USA',1,1,1)
triathlon.fulldata(example)
triathlon.datavalue(example)

# task3 Protein-coding capability calculator
import re
def pro(seq):
    '''
protein coding or not
distance between ATG and TGA, exacly one
>50% in these codons protein-coding
<10% non-coding
else unclear

input: DNA string
return: percentage of coding, pro or not, upper or lower
'''
    total=len(seq)
    tein=re.sub('.*(ATG.*TGA).*',r'\1',seq,flags=re.IGNORECASE) # or re.I
    print(tein)
    teinl=len(tein)
    per=teinl/total*100
    if per>0.5:
        return 'Percentage='+str(per)+'% Protein-coding'
    elif per<0.1:
        return 'Percentage='+str(per)+'% Non-coding'
    else:
        return 'Percentage='+str(per)+'% Unclear'
test='AtGCCCCCCCCCCCCCCCCCCCCCCCCCCcccccctGaaaaaaaaaaaaaaaaaa'
print(pro(test))
input_pro=input('sequence to test:')
print(pro(input_pro))