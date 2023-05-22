import re
# task1
# way1 pseudocode
# find TAG/TAA/TGA, count+1, change them to ZZZ in seq1, loop until find every under ATG
# print count

# way1 [not so concise ]
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
count=0
while re.search(r'[A-Z]*ATG[A-Z]*TGA',seq):
 count=count+1
 seq=re.sub('TGA','ZZZ',seq,1)
while re.search(r'[A-Z]*ATG[A-Z]*TAA',seq):
 count=count+1
 seq=re.sub('TAA','ZZZ',seq,1)
while re.search(r'[A-Z]*ATG[A-Z]*TAG',seq):
 count=count+1
 seq=re.sub('TAG','ZZZ',seq,1)
print(seq)
print('Total number of possible coding sequences formed by this sequence is',count)

# way2 pseudocode
# select out the ATG and its following
# change all TGA/TAA/TAG to ZZZ
# count ZZZ

# way2 [concise and nice]
'''
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
seqhead=re.sub(r'.*ATG(.*$)',r'\1',seq)
seqtail=re.sub(r'TGA|TAA|TAG','ZZZ',seqhead) #???
num=seqtail.count('ZZZ')
print('Total number of possible coding sequences formed by this sequence is',num)
'''

# Advance: 1.some possible intergrated version to find the stop codons: 
#            while r'[A-Z]*ATG[A-Z]*TA[GA]
# Question:1.recognize tail's code with ambiguity in regular expression? are there?
#          2.how to differ $ in text or end?
#          3.mean of r before regular expression?

# consecutive string. how to count, ######, count(###), the result is 2, so smart the program, isn't it?


