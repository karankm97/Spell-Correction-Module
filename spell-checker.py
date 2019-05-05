#!C:\Python27\python.exe

import cgi
import cgitb



form = cgi.FieldStorage()

fn = form.getvalue('user')

qq = str(fn)


def intersect(a,b):
    lst1=list(set(a) & set(b))
    len1=len(lst1)
    return len1

def union(a,b):
    lst2 = list(set(a) | set(b))
    len2 = len(lst2)
    return len2

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head><title>Spell Correction</title></head>"
print "<body>"
vocab=['abroad','about','boardroom','border','king','sunflower','railway','remote','broken','shoes','napkin','aeroplane','cricket','football','basketball','inbox','brave','magnify','cruise','novel']
y=[]
for i in vocab:
    b=i
    for x in range(len(b)-1):
        n=b[x:x+2]
        y.append(n)

print "<br>"

print "<br><br><hr>"


q = qq
print "<h2>Given query: </h2>", q

query=[]

for i in range(len(q)-1):
    n=q[i:i+2]
    query.append(n)
    
print "<h3>Bi-Gram of Query: </h3>",query

print "<br><br><hr>"

#print('--------------------------------------------------------------')

#condensed code

#for breaking down all the words separately into bigrams
#checing scores word by word with the query term
#and string the jaccard coeff

count=0
scores=[]
print "<h1>Bi-Grams of the individual terms:</h1>"
for i in vocab:
    b=i
    temp = []
    for x in range(len(b)-1):
        n=b[x:x+2]
        temp.append(n)
    count=count+1
    print 'term',count,'(',i,')','------>',temp,"<br>"
    aa=float(intersect(query,temp))
    bb=float(union(query,temp))
    cc = float(aa/bb)
    #print cc
    scores.append(cc)
print "<br><hr>"

count=0
print "<h1>Jacard Coefficients are:</h1>"

for i in scores:
    count+=1
    print 'term',count,'(',vocab[count-1],')','------>',i,"<br>"

print "<br><hr>"

#to sort the scores array and get top 5 elements

nn=len(vocab)
pos = range(nn)

n=len(scores)
for i in range(n):
    for j in range(0,n-i-1):
        if(scores[j]<scores[j+1]):
            scores[j],scores[j+1]=scores[j+1],scores[j]
            pos[j],pos[j+1]=pos[j+1],pos[j]

#print(scores)
#print(pos)
print "<h1>Top 5 terms are:</h1>"
#top 5 poss need to be read

top5=[]
for i in range(5):
    index=pos[i]
    term=vocab[index]
    top5.append(term)
    print term,"<br>"



#print(levenshteinDistance("hello","hallo"),'is the distace')


#calculating all edit distances with the original query term

print "<h1>Edit distance scores:</h1> "
LDscores=[]
for i in top5:
    abc=levenshteinDistance(q,i)
    print abc,"<br>"
    LDscores.append(abc)


#sort the scores to get min distance

n=len(LDscores)
for i in range(n):
    for j in range(0,n-i-1):
        if(LDscores[j]>LDscores[j+1]):
            LDscores[j],LDscores[j+1]=LDscores[j+1],LDscores[j]
            pos[j],pos[j+1]=pos[j+1],pos[j]

#reading the min distance pos -> 1st element of sorted array

#print pos
final_index=pos[0]

print "<h1>The closest word to the given query is:</h1>",vocab[final_index]

print "</body>"
print "</html>"


