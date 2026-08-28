
#! Q1. What will be the output after calling append()?
# fruits = ["apple", "banana", "mango"]
# fruits.append("orange")
# print(fruits)

#! Q2. What will be the output after using extend()?
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)


#! Q3. What does count() return here?
# nums = [1, 2, 3, 2, 4, 2, 5]
# print(nums.count(2))

#! Q4. What will be the list after remove()?
# colors = ["red", "blue", "green", "blue"]
# colors.remove("blue")
# print(colors) 


#! Q5. What does pop() return and what is the list after?
# lst = [10, 20, 30, 40, 50]
# val = lst.pop(2)
# print(val)
# print(lst)


#! Q6. What does index() return?
# items = ["cat", "dog", "fish", "dog"]
# print(items.index("dog"))





 #! Q7. What happens after clear()?
# data = [100, 200, 300]
# data.clear()
# print(data)


#! Q8. What is the output after sort() in ascending order?
# marks = [85, 42, 97, 61, 33]
# marks.sort()
# print(marks)

#! Q9. What is the output after sort() in descending order?
# marks = [85, 42, 97, 61, 33]

# marks.sort(reverse=True)
# print(marks)



#! Q10. What is the output?
# lst = [10, 20, 30, 40, 50]
# val = lst.pop(2)
# lst.append(val * 2)
# print(lst)




# t = (1, 2, 3, 1, 4, 1, 5)
# print(t.count(1))



#! Q12. What does index() return?
# t = ("a", "b", "c", "d", "e")
# print(t.index("c"))



#! Q13. What will be the output?
# t = (10, 20, 10, 30, 10, 40)
# print(t.count(10))
# print(t.index(30))


#! Q14. What does count() return for a value not in the tuple?
# t = (5, 10, 15, 20)
# print(t.count(99))



#! Q15. What is the output?
# t = (1, 2, 3, 2, 4, 2)
# print(t.index(2, 2))


#set methods
#! Q16. What does union() return?
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.union(B))


#! Q17. What does intersection() return?
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A.intersection(B))


#! Q18. What happens after add()?
# s = {10, 20, 30}
# s.add(40)
# s.add(50)
# print(s)


#! Q19. What happens when you add a duplicate using add()?
# s = {1, 2, 3}
# s.add(2)
# print(s)


#! Q20. What does update() do to the set?
# s = {1, 2, 3}
# s.update([4, 5, 6])
# print(s)


#! Q21. What does clear() do?
# s = {"apple", "banana", "cherry"}
# s.clear()
# print(s)


#! Q22. What happens after remove()?
# s = {10, 20, 30, 40}
# s.remove(20)
# print(s)


#! Q23. What error does remove() raise if element is not found?
# s = {1, 2, 3}

# s.remove(99)


#! Q24. What is the output after update() with another set?
A = {1, 2, 3}
B = {3, 4, 5}
A.update(B)
print(A)



#! Q25. What is the output? (union vs update difference)
A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print(C)
