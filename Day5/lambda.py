'''
def doubleit(x):
   return x

x=[1,2,3]
ok=map(doubleit,x)
print(list(ok))
'''

#Without using lambda function
x= ["hello", "hi"]
def start(x):
    return len(x)>3
y=filter(start, x)
print(list(y))


#Using Lambda function
x= ["hello", "hi"]
y=filter(lambda x: len(x)>3,x)
print(list(y))


#Example: With using Lambda
words = ["apple", "banana", "cherry"]
uppercased_words = list(map(lambda x: x.upper(), words))
print(uppercased_words)

#Example: Without using Lambda
words = ["apple", "banana", "cherry"]
def to_upper(text):
    return text.upper()
uppercased_words = list(map(to_upper, words))
print(uppercased_words)

