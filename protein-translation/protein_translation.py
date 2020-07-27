def proteins(strand):
    proteinStrand = []
    codons = []
    proteinDict = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine',
                   'UUA':'Leucine', 'UUG':'Leucine','UCU':'Serine', 'UCC':'Serine',
                   'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine',
                   'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan'}
    
    for items in range (0,len(strand),3):
         proteinStrand.append(strand[items:items+3])
    for items in proteinStrand:
        if items == 'UAA' or items == 'UAG' or items == 'UGA' or items not in proteinDict.keys():
            break
        else:
            codons.append(proteinDict[items])
            
    return(codons)
