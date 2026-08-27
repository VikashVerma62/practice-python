# 1. Convert the string "hello world" to uppercase using upper().
a="this is python"
print(a.upper())

#2. Convert the string "PYTHON" to lowercase using lower().
a="PYTHON"
print(a.lower())

#3. Check whether the string "PYTHON" is written in all uppercase letters using isupper().
print(a.isupper())

#4. Check whether the string "hello" is written in all lowercase letters using islower().
a="hello"
print(a.islower())

#5. Find the length of the string "Data Science" using len().
l="data science"
print(len(l))

#6. Replace the word "cat" with "dog" in the sentence "The cat is sleeping" using replace().
s="The cat is sleeping"
print(s.replace("cat","dog"))

#7. Count the number of times the letter 'a' appears in "banana" using count().
b="banana"
print(b.count("a"))

#8. Split the sentence "I love Python programming" into a list of words using split().
p="I love python programming"
print(p.split())

#Join the list ["I", "love", "Python"] into a single string separated by spaces using join().
a=["I","love","python"]
b=" ".join(a)
print(b)


#10. Remove the leading and trailing spaces from the string " Hello World " using strip().
s="   Hello World   "
print(s.strip())

#11. Check if the string "Python" contains only alphabetic characters using isalpha().
s="python"
print(s.isalpha())

#12. Check if the string "Python3" contains only alphanumeric characters using isalnum().

s="python123"
print(s.isalnum())

#13. Check if the string "12345" contains only numeric digits using isdigit().
s="1234"
print(s.isdigit())

#14. Find the index of the substring "World" in "Hello World" using find().
s="Hello World"
print(s.find("World"))


#15. Count how many times the word "the" appears in "the quick fox jumped over the lazy dog" using
#count().

s="the quick fox jumped over the lazy dog"
print(s.count("the"))

#16. Write a program to count the number of words in the sentence "Python is fun to learn" using split().

s="Python is fun to learn"
print(s.split())


#17. Join the characters of the list ['P', 'y', 't', 'h', 'o', 'n'] into a single word using join().
a=['p','y','t','h','o','n']
b="".join(a)
print(b)


#21. Check if the string "Programming" starts with "Pro" using startswith().
p="programming"
print(p.startswith("pro"))



# lis method
a=[1,2,3,4]
a.append(2)
print(a)

a.insert(2,10)
print(a)

a.extend([1,2,3])
print(a)

a[2]=4
print(a)

a[2:3]=12,13
print(a)

a[2:2]=23,34
print(a)



a.remove(12)
print(a)

a.pop(1)
print(a)
print(a.count(2))

a.sort()
print(a)

a.sort(reverse=True)
print(a)


# methods of tupple

a=(1,2,3,4)
print(a.index(2))
print(a.count(3))



# method of set
s={1,2,3,4,"hello"}
print(s)
s.add(6)
print(s)


s={1,2,3,4,5,6}
print(s)

s.update([7,8])
print(s)

s.remove(2)
print(s)

s.discard(6)
print(s)

s.pop()

# methods of dict

d={"name":"vikash","marks":89}
print(d.get("name"))

print(d.keys())

print(d.values())

d.update({"name":"vikki","rollno":45})
print(d)

d.pop("rollno")
print(d)



d.popitem()
print(d)

