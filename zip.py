s1={2,1,3}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)

list1=[1,2,3,4]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks=['reliance','infoys','tcs']
prices=[2175.1127,2750]
new_dict={stocks:prices for stocks,
          prices in zip(stocks,prices)}
print('\n{}'.format (new_dict))