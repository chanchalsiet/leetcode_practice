"""1. Basic for Loop
Explanation: The loop iterates over each element in the fruits list, printing each fruit."""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#Ierating Over a String:
word = "Python"
for letter in word:
    print(letter)

"""2. for Loop with range()
Explanation: range(5) generates numbers from 0 to 4, and the loop iterates over these ."""
for i in range(5):
    print(i)

#Using range(start, stop)
for i in range(1, 6):
    print(i)

#Using range(start, stop, step):
for i in range(0, 10, 2):
    print(i)

"""3. for Loop with enumerate()
Explanation: enumerate() returns both the index and the value, allowing you to access both in the loop."""
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)



"""4. for Loop with zip()
Explanation: zip() pairs up elements from names and ages, and the loop iterates over these pairs."""
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)


"""5. List Comprehension
A Compact Way to Write a for Loop:
Explanation: List comprehension is a concise way to create lists. It’s essentially a for loop inside a list.
."""
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)


