from xml.dom.minidom import parse 
import pandas as pd
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("go_obo.xml")
Root=DOMTree.documentElement
genes=Root.getElementsByTagName('term')
definition=[]
id=[]
name=[]
childnodes=[]
print('It may take little long time...')
def count_child_gene(gene_1,genes_1):
    sub_genes=set()
    name_data_0=gene_1.getElementsByTagName('id')[0]
    name_data=name_data_0.childNodes[0].data
    for other_gene in genes_1:
        is_a_nodes=other_gene.getElementsByTagName('is_a')
        for is_a_node in is_a_nodes:
            if is_a_node.childNodes[0].data==name_data:
                sub_genes.add(other_gene)
                sub_genes|=count_child_gene(other_gene,genes_1)
    return sub_genes

for gene in genes:
    defstr=gene.getElementsByTagName('defstr')[0]
    test=defstr.childNodes[0].data
    if 'autophagosome' in test:
        definition.append(test)
        id_test=gene.getElementsByTagName('id')[0]
        id.append(id_test.childNodes[0].data)
        name_test=gene.getElementsByTagName('name')[0]
        name.append(name_test.childNodes[0].data)
        num=len(count_child_gene(gene,genes))
        childnodes.append(num)

data={'id':id,'name':name,'definition':definition,'childnodes':childnodes}
df=pd.DataFrame(data)
df.to_excel('autophagosome.xlsx',index=False)
