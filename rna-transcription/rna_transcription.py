def to_rna(dna_strand):

    rna_strand = ''
    converterDict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    for toConvert in dna_strand:
        rna_strand += converterDict[toConvert]
        
    return(rna_strand)
