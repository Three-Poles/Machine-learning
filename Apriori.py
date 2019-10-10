from numpy import *
import itertools
 
support_dic = {}
 

def loadDataSet():
     return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
 

def createC1(dataSet):
     C1 = set([])
     for item in dataSet:
         C1 = C1.union(set(item))
     return [frozenset([i]) for i in C1]
 

def getLk(dataset, Ck, minSupport):
     global support_dic
     Lk = {}

     for item in dataset:
         for Ci in Ck:
             if Ci.issubset(item):
                 if not Ci in Lk:
                     Lk[Ci] = 1
                 else:
                     Lk[Ci] += 1

     Lk_return = []
     for Li in Lk:
         support_Li = Lk[Li] / float(len(dataSet))
         if support_Li >= minSupport:
             Lk_return.append(Li)
             support_dic[Li] = support_Li
     return Lk_return
 

def genLk1(Lk):
     Ck1 = []
     for i in range(len(Lk) - 1):
         for j in range(i + 1, len(Lk)):
             if sorted(list(Lk[i]))[0:-1] == sorted(list(Lk[j]))[0:-1]:
                 Ck1.append(Lk[i] | Lk[j])
     return Ck1

def genItem(freqSet, support_dic):
     for i in range(1, len(freqSet)):
         for freItem in freqSet[i]:
             genRule(freItem)
 

def genRule(Item, minConf=0.7):
     if len(Item) >= 2:
         for element in itertools.combinations(list(Item), 1):
             if support_dic[Item] / float(support_dic[Item - frozenset(element)]) >= minConf:
                 print str([Item - frozenset(element)]) + "----->" + str(element)
                 print support_dic[Item] / float(support_dic[Item - frozenset(element)])
                 genRule(Item - frozenset(element))
 

if __name__ == '__main__':
     dataSet = loadDataSet()
     result_list = []
     Ck = createC1(dataSet)

     while True:
         Lk = getLk(dataSet, Ck, 0.5)
         if not Lk:
             break
         result_list.append(Lk)
         Ck = genLk1(Lk)
         if not Ck:
             break

     print support_dic

     genItem(result_list, support_dic)