import time
import os, psutil, sys
from numbers import Number

#file_path=r'C:\Users\vinut\7023239026_8671674031_9195882821_CSCI570\datapoints\input\in15.txt'
file_path=sys.argv[1]
row4=""
row5=""
start_time = time.perf_counter()

#generating the string for sequence alignment
def createStringSequence(string1,array):
    string=string1
    for i in array:
        string=string[:i+1]+string+string[i+1:]
    return string

alignment_cost=0

#calculating the cost of sequence alignment
def findMinimumAlignmentCost(match_string1, match_string2, mismatch_penalty, gap_penalty):
    strlen1 = len(match_string1)
    strlen2 = len(match_string2)
    
    #solution matrix for opt soln
    opt = [[0 for x in range(strlen1+strlen2+1)] for y in range(strlen1+strlen2+1)]
    
    #solution matrix initialization
    for i in range (0,strlen1+strlen2+1):
        opt[i][0] = i*gap_penalty
        opt[0][i]=i*gap_penalty

    for i in range (1, strlen1+1):
        for j in range (1, strlen2+1):
            if match_string1[i-1] == match_string2[j-1]:
                opt[i][j] = opt[i-1][j-1]
            else:
                pivot=match_string1[i-1]+match_string2[j-1]
                mismatchError=mismatch_penalty[pivot]
                opt[i][j] = min(opt[i-1][j-1]+mismatchError, opt[i-1][j]+gap_penalty, opt[i][j-1]+gap_penalty)
    
    alignment_cost=opt[strlen1][strlen2]

#filling the solution matrix for the final value of optimal solution
    total_length=strlen1+strlen2
    i=strlen1
    j=strlen1
    x=total_length
    y=total_length
    
    result1=[0]*(total_length+1)
    result2=[0]*(total_length+1)
    
    while(i!=0 and j!=0):
        key1=match_string1[i-1]
        key2=match_string2[j-1]
        
        if(key1!=key2):
            pivot=key1+key2
            value=mismatch_penalty[pivot]
        if(key1==key2):
            result1[x]=match_string1[i-1]
            result2[y]=match_string2[j-1]
            x-=1
            y-=1
            i-=1
            j-=1
        elif(opt[i-1][j-1]+value==opt[i][j]):
            result1[x]=match_string1[i-1]
            result2[y]=match_string2[j-1]
            x-=1
            y-=1
            i-=1
            j-=1
        elif(opt[i-1][j]+gap_penalty==opt[i][j]):
            result1[x]=match_string1[i-1]
            result2[y]="_"
            x-=1
            y-=1
            i-=1
        elif (opt[i][j-1]+gap_penalty==opt[i][j]):
            result1[x]="_"
            result2[y]=match_string2[j-1]
            x-=1
            y-=1
            j-=1
        
    while (x>0):
        if(i>0):
            i-=1
            result1[x]=match_string1[i]
        else:
            result1[x]="_"
        x-=1
    
    while (y>0):
        if(j>0):
            j-=1
            result2[y]=match_string2[j]
        else:
            result2[y]="_"
        y-=1
            
    
    index=1
    i=total_length
    while(i>=1):
        if(result1[i]=="_" and result2[i]=="_"):
            index=i+1
            break
        i-=1
    
    output1=""
    output2=""
    for i in range(index,total_length+1):
        output1+=result1[i]
    for i in range(index, total_length+1):
        output2+=result2[i]
    
    if(len(sys.argv)>2):
        ofile=sys.argv[2]
    else:
        ofile="output.txt"
        
#   with open("inp15_op.txt","w") as outputFile:
    with open(ofile,"w") as outputFile:
        row1=(str)(alignment_cost)+"\n"
        row2=output1[0:50]+" "+output1[-50:]+"\n"
        row3=output2[0:50]+" "+ output2[-50:]+"\n"
        total_time = (time.perf_counter() - start_time)*1000 #converting seconds to milliseconds
        row4=((str)(total_time)).split(" ")[0][:7]+"\n"
        row5=str(psutil.Process(os.getpid()).memory_info().rss / 1024)
        outputFile.write(row1)
        outputFile.write(row2)
        outputFile.write(row3)
        outputFile.write(row4)
        outputFile.write(row5)

with open(file_path) as f:
    frow = f.readlines() #file rows
    frow =[s.strip() for s in frow]

    new_list = list(filter(lambda x: isinstance(x, Number), frow))
    strings = []
    j = []
    k = []
    
    for i in range(0, len(frow)):
        if frow[i].isalpha():
            strings.append(frow[i])
        elif len(strings) == 1:
            j.append(frow[i])
        else:
            k.append(frow[i])
    base_string1, base_string2 = strings[0], strings[1]
    j = list(map(int, j))
    k = list(map(int, k))

    s1= createStringSequence(strings[0],j)
    s2= createStringSequence(strings[1],k)

    mismatch_penalty={"AC":110, "AG":48,  "AT":94, 
                      "CA":110, "CG":118, "CT":48, 
                      "GA":48,  "GC":118, "GT":110, 
                      "TA":94,  "TC":48,  "TG":110}
    
    gap_penalty = 30
    
#   slen1 = len(s1)
#   slen2 = len(s2)
#   pow1 = 2**len(j)
#   pow2 = 2**len(k)
#    if((len(j)>=0) and (len(j)<=10) and (len(k)>=0) and (len(k)<=10) and (slen1>=1) and (slen1<=2000) and (slen2>=1) and (slen2<=2000) and (((2**len(j))*slen1)>=1) and (((2**len(j))*slen1)<=2000) and (((2**len(k))*slen2)>=1) and (((2**len(k))*slen2)<=2000)):
    findMinimumAlignmentCost(s1,s2,mismatch_penalty,gap_penalty)