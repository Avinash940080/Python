#numeric datatypes
a = 5 #int
print(type(a))


b = 3.14 #float
print(type(b))

c = 3+2j #complex
print(type(c))




#string datatype
fruit = 'apple' #collection of characters
print(type(fruit))



#boolean datatype
A = False  #true or false
print(type(A))


#list datatype
#represeented by '[]' and they are mutable.
List = [1,2,4,'mango']
List[0] = 6
List.append(6)
print(type(List))
print(List) 


#tuple datatype
#reprented by '()' and they are immutable.
tuple = (1,2,3,5,'BMW')
print(type(tuple))
print(tuple)

#set datatype
#represented by'{}' and it only takes prints unique values.It is immutable.
set = {1,2,3,3,4,4,'mercedes'}
print(set)#no duplicate values are printed.

#dictionary datatypes
#It is a collection of key-value pairs.
#keys are the unique identifiers.
#values are the definitions of the keys.
#dictionary is represented by '{}'.

dict = {
    'car': 'volvo', 'model': 'xc90'
}
print(type(dict))
#syntax is print(dict[key])
print(dict)
print(dict['car'])

#range datatype
#It is often used in loops 

for i in range(5):
    print('hello')