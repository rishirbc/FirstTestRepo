print('Array is similar to list, but array can have only one type of data in it. But in list we an have'
      'many data types at a single list.')
print('We can also shrink and expand array, but not list.')

import array
ar = array('L', []) #this is the empty array creation
ar1 = array('i', [1, 3, 4, 5, 66, 23, 555])
ar2 = array('i', [100, 200, 300])
print('Our array is:', ar1, 'and its type is:', type(ar1))
ar1.reverse()
print('Our reversed array is:', ar1)
ar1.append(100)
print('Our reversed array after appending is:', ar1)
ar1.pop(1)
print('Our array after popping 1st element is:', ar1)
ar1.pop()
print('Our array after popping last element is:', ar1)
ar1.remove(5)
print('Our array after removing the value in the array is:', ar1)
c = ar1.count(4)
print('The number of times an element(4) repeats in array is:', c)
ar1.insert(1,200)
print('To insert an element in array we hae to provide the index then value:', ar1)
ar1.extend(ar2)
print('To extend or combine two array we can use',ar1)

#COPY AN ARRAY
ar1 = array('I', [1, 3, 4, 5, 66, 23])
ar2 = array(ar1.typecode, (a for a in ar1))
print('COp', ar2)

ar1 = array('i', [1, 3, -4, 5, 66, 23])
ar2 = array(ar1.typecode, (a*a for a in ar1))
print(ar2)

ar1 = array('i', [1, 3, -4, 5, 66, 23])
ar2 = array(ar1.typecode, (a+10 for a in ar1))
print(ar2)



print('\n')
ar1 = array('B', [1, 2, 3])
print('sharacter', ar1)


#MANUALLY ENTER VALUE TO ARRAY
ar3 = array('i', [])
n = int(input('Enter the no: of items in array:'))
for i in range(n):
    a = int(input('Enter the no:'))
    ar3.append(a)
print(ar3)


#FIND A ELEMENT IN AN ARRAY
ele = int(input('Enter the no to find: '))
for i in ar3:
    if i == ele:
        print('Value that we found is at position: ',ar3.index(i))
        break
else:
    print('Value not found.')



