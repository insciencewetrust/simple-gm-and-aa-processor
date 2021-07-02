import random as rnd

def baseMatcher(DNASeq):
    complementaryStrand=""
    for i in range(0, len(DNASeq)):
        if DNASeq[i]=="A":
            complementaryStrand+="T"
        elif DNASeq[i]=="T":
            complementaryStrand+="A"
        elif DNASeq[i]=="G":
            complementaryStrand+="C"
        elif DNASeq[i]=="C":
            complementaryStrand+="G"
        else:
            pass
    return complementaryStrand

def DNAtomRNA(DNASeq):
    mRNASeq=""
    for i in range(0, len(DNASeq)):
        if DNASeq[i]=="A":
            mRNASeq+="U"
        elif DNASeq[i]=="T":
            mRNASeq+="A"
        elif DNASeq[i]=="G":
            mRNASeq+="C"
        elif DNASeq[i]=="C":
            mRNASeq+="G"
        else:
            pass
    return mRNASeq

def mRNAtoDNA(mRNASeq):
    DNASeq=""
    for i in range(0, len(mRNASeq)):
        if mRNASeq[i]=="A":
            DNASeq+="T"
        elif mRNASeq[i]=="T":
            DNASeq+="A"
        elif mRNASeq[i]=="G":
            DNASeq+="C"
        elif mRNASeq[i]=="C":
            DNASeq+="G"
        else:
            pass
    return DNASeq

def mRNAtoAA(mRNASeq, aminoacids):
    AA=""
    for i in range(0, len(mRNASeq)-2, 3):
        codon=mRNASeq[i]+mRNASeq[i+1]+mRNASeq[i+2]
        for key in aminoacids.keys():
            if codon in aminoacids[key]:
                AA+=key+" "
            else:
                pass
    AA=AA.strip()
    return AA

def AAtomRNA(AA, aminoacids):
    mRNASeq=""
    for i in range(0, len(AA)-2, 4):
        aa=AA[i]+AA[i+1]+AA[i+2]
        for key in aminoacids.keys():
            if key==aa:
                randInt=rnd.randint(0, len(aminoacids[key])-1)
                codon=aminoacids[key][randInt]
                mRNASeq+=codon
            else:
                pass
    return mRNASeq

aminoacids={"Phe": ["UUU", "UUC"], "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], "Ile": ["AUU", "AUC", "AUA"], "Met": ["AUG"], "Val": ["GUU", "GUC", "GUA", "GUG"], "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "Pro": ["CCU", "CCC", "CCA", "CCG"], "Thr": ["ACU", "ACC", "ACA", "ACG"], "Ala": ["GCU", "GCC", "GCA", "GCG"], "Tyr": ["UAU", "UAC"], "His": ["CAU", "CAC"], "Gln": ["CAA", "CAG"], "Asn": ["AAU", "AAC"], "Lys": ["AAA", "AAG"], "Asp": ["GAU", "GAC"], "Glu": ["GAA", "GAG"], "Cys": ["UGU", "UGC"], "Trp": ["UGG"], "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "Gly": ["GGU", "GGC", "GGA", "GGG"], "STOP": ["UAA", "UAG", "UGA"]}

running=True
while running==True:
    optionStr=input("What do you want to do? (please type the relevant number)\n1) Complementary base pairing\n2) Finding the mRNA sequence corresponding to a DNA sequence\n3) Finding the DNA sequence corresponding to an mRNA sequence\n4) Finding the amino acids encoded by a DNA sequence\n5) Finding the amino acids encoded by an mRNA sequence\n6) Finding a *possible* DNA sequence corresponding to a set of amino acids\n7) Finding a *possible* mRNA sequence corresponding to a set of amino acids\n8) Exit\n")
    if optionStr=="1" or optionStr=="2" or optionStr=="3" or optionStr=="4" or optionStr=="5" or optionStr=="6" or optionStr=="7" or optionStr=="8":
        if optionStr=="1":
            DNASeq=input("Please enter the base sequence of the DNA strand you want to find the complementary strand of: ").upper()
            complementaryStrand=baseMatcher(DNASeq)
            print("The base sequence of the complementary strand is: "+complementaryStrand+"\n")
        elif optionStr=="2":
            DNASeq=input("Please enter the base sequence of the DNA strand: ").upper()
            direction=input("What is the direction of this DNA strand?\n1) 3' to 5'\n2) 5' to 3'\n")
            check=False
            while check==False:
                if direction=="1" or direction=="2":
                    if direction=="1":
                        mRNASeq=DNAtomRNA(DNASeq)
                        print("The base sequence of the mRNA strand is: "+mRNASeq+"\n")
                    elif direction=="2":
                        otherDNASeq=baseMatcher(DNASeq)
                        mRNASeq=DNAtomRNA(otherDNASeq)
                        print("The base sequence of the mRNA strand is: "+mRNASeq+"\n")
                    else:
                        pass
                    check=True
                else:
                    print("Wrong input! Please try again.")
        elif optionStr=="3":
            mRNASeq=input("Please enter the base sequence of the mRNA strand: ").upper()
            DNASeq=mRNAtoDNA(mRNASeq)
            otherDNASeq=baseMatcher(DNASeq)
            print("The base sequence of the DNA strand going from 3' to 5' is: "+DNASeq+"\nThe base sequence of the DNA strand going from 5' to 3' is: "+otherDNASeq+"\n")
        elif optionStr=="4":
            DNASeq=input("Please enter the base sequence of the DNA strand: ").upper()
            direction=input("What is the direction of this DNA strand?\n1) 3' to 5'\n2) 5' to 3'\n")
            check=False
            while check==False:
                if direction=="1" or direction=="2":
                    if direction=="1":
                        mRNASeq=DNAtomRNA(DNASeq)
                        AA=mRNAtoAA(mRNASeq, aminoacids)
                        print("The resulting amino acid sequence is: "+AA+"\n")
                    elif direction=="2":
                        otherDNASeq=baseMatcher(DNASeq)
                        mRNASeq=DNAtomRNA(otherDNASeq)
                        AA=mRNAtoAA(mRNASeq, aminoacids)
                        print("The resulting amino acid sequence is: "+AA+"\n")
                    else:
                        pass
                    check=True
                else:
                    print("Wrong input! Please try again."+"\n")
        elif optionStr=="5":
            mRNASeq=input("Please enter the base sequence of the mRNA strand: ").upper()
            AA=mRNAtoAA(mRNASeq, aminoacids)
            print("The resulting amino acid sequence is: "+AA+"\n")
        elif optionStr=="6":
            AA=input("Please enter a set of amino acids (first letters of the amino acids must be capitalised and there must be single spaces between the amino acids)")
            mRNASeq=AAtomRNA(AA, aminoacids)
            DNASeq=mRNAtoDNA(mRNASeq)
            otherDNASeq=baseMatcher(DNASeq)
            print("The base sequence of the DNA strand going from 3' to 5' is: "+DNASeq+"\nThe base sequence of the DNA strand going from 5' to 3' is: "+otherDNASeq+"\n")
        elif optionStr=="7":
            AA=input("Please enter a set of amino acids (first letters of the amino acids must be capitalised and there must be single spaces between the amino acids)")
            mRNASeq=AAtomRNA(AA, aminoacids)
            print("The base sequence of the mRNA strand is: "+mRNASeq+"\n")
        elif optionStr=="8":
            running=False
        else:
            pass
    else:
        print("Wrong input! Please try again."+"\n")