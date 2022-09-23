import sys
import time
import os, psutil

string_array=[]
j=[]
k=[]
alpha={'AA': 0,'CC': 0,'GG': 0,'TT': 0,'AC': 110, 'AG': 48, 'AT': 94, 'CG': 118, 'CT': 48, 'GT': 110, 'CA': 110, 'GA': 48, 'TA': 94, 'GC': 118, 'TC': 48, 'TG': 110}
delta=30
filename=sys.argv[1]

if len(sys.argv)>2: 
    outputFilename=sys.argv[2]
else:
    outputFilename="output.txt"

#open input file
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#parse input file
for line in lines:
    if line.isalpha():
        string_array.append(line)
    elif len(string_array)==1:
        j.append(line)
    else:
        k.append(line)
        
j=list(map(int, j))
k=list(map(int, k))

#function to generate final strings.
def stringGeneration(st, nums):
    for i in nums:
        st=st[:i+1]+st+st[i+1:]
    return st

s1=stringGeneration(string_array[0],j)
s2=stringGeneration(string_array[1],k)

def baseCase(x, y, alpha, delta):
    n=len(x)
    m=len(y)
    opt=[]
    for i in range(n+1):
        opt.append([0]*(m+1))
    for j in range(m+1):
        opt[0][j]=delta*j
    for i in range(n+1):
        opt[i][0]=delta*i
    for i in range(1, n+1):
        for j in range(1, m+1):
            key=x[i-1]+y[j-1]
            opt[i][j] = min(opt[i-1][j-1] + alpha[key], opt[i][j-1] + delta, opt[i-1][j] + delta)
    x_ans=""
    y_ans=""
    i=n
    j=m
    while i and j:
        score=opt[i][j]
        score_diag=opt[i-1][j-1]
        score_up=opt[i-1][j]
        score_left=opt[i][j-1]
        key=x[i-1]+y[j-1]
        if score==score_diag+alpha[key]:
            x_ans=x[i-1]+x_ans
            y_ans=y[j-1]+y_ans
            i-=1
            j-=1
        elif score==score_up+delta:
            x_ans=x[i-1]+x_ans
            y_ans='_'+y_ans
            i-=1
        elif score==score_left+delta:
            x_ans='_'+x_ans
            y_ans=y[j-1]+y_ans
            j-=1
    while i:
        x_ans=x[i-1]+x_ans
        y_ans='_'+y_ans
        i-=1
    while j:
        x_ans='_'+x_ans
        y_ans=y[j-1]+y_ans
        j-=1
    return [x_ans, y_ans, opt[n][m]]


# function to calculate memory efficient version of sequence alignment
def memoryEfficient(str1, str2, alpha, delta):
    n = len(str1)
    m = len(str2)
    if n<2 or m<2:
        return baseCase(str1,str2,alpha, delta)
    else:
        F = fwdPass(str1[:n//2], str2, alpha, delta)
        B = bwdPass(str1[n//2:], str2, alpha, delta)
        partition = [F[j] + B[m-j] for j in range(m+1)]
        cut = partition.index(min(partition))
        F=[]
        B=[]
        partition=[]
        call_left = memoryEfficient(str1[:n//2], str2[:cut], alpha, delta)
        call_right = memoryEfficient(str1[n//2:], str2[cut:], alpha, delta)
        return [call_left[r] + call_right[r] for r in range(3)]

def bwdPass(str1,str2,alpha,delta):
    n = len(str1)
    m = len(str2)
    opt = []
    for i in range(n+1):
        opt.append([0]*(m+1))
    for j in range(m+1):
        opt[0][j] = delta*j
    for i in range(1, n+1):
        opt[i][0] = opt[i-1][0] + delta
        for j in range(1, m+1):
            key=str1[n-i]+str2[m-j]
            opt[i][j] = min(opt[i-1][j]+delta, opt[i][j-1]+delta, opt[i-1][j-1]+alpha[key])
        opt[i-1] = []
    return opt[n]

def fwdPass(str1,str2,alpha,delta):
    n = len(str1)
    m = len(str2)
    opt = []
    for i in range(n+1):
        opt.append([0]*(m+1))
    for j in range(m+1):
        opt[0][j] = delta*j
    for i in range(1, n+1):
        opt[i][0] = opt[i-1][0]+delta
        for j in range(1, m+1):
            key=str1[i-1]+str2[j-1]
            opt[i][j]=min(opt[i-1][j]+delta, opt[i-1][j-1]+alpha[key], opt[i][j-1]+delta)
        opt[i-1]=[]
    return opt[n]


time_start = time.perf_counter()
z=memoryEfficient(s1, s2, alpha, delta)
end=time.time()


with open(outputFilename,"w") as outputFile:
    line1=str(z[2])+"\n"
    line2=z[0][0:50]+" "+z[0][-50:]+"\n"
    line3=z[1][0:50]+" "+z[1][-50:]+"\n"
    time_elapsed = ((time.perf_counter() - time_start)*1000)
    line4=((str)(time_elapsed)).split(" ")[0][:7]+"\n"
    line5=str(psutil.Process(os.getpid()).memory_info().rss / 1024)       
    outputFile.write(line1)     # print cost of alignment
    outputFile.write(line2)     # print first string alignment ( Consists of A, C, T, G, _ (gap) characters)
    outputFile.write(line3)     # print second string alignment ( Consists of A, C, T, G, _ (gap) characters)
    outputFile.write(line4)     # print time in mili seconds
    outputFile.write(line5)     # print memory in Kilobytes 
