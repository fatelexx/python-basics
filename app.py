import sys;

class MyClass:
  x = 5

p1 = MyClass();
print(p1.x);

x = lambda a : a + 10
print(x(5))

first = float(input('First: '))
second = float(input('Second: '))
sum = str(first + second);
print('Sum: ' + sum)
nums = [1, 2 ,3];
print(nums);
set = {"apple", "banana", "cherry"}
print(set)
print(sys.version)
dictionary = {"name" : "John", "age" : 36};
print(dictionary);

#This is a comment