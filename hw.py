# Exercises
# Exercise #1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
def swap(input_list, i, j, k, l):
    input_list[i], input_list[j], input_list[k], input_list[l] = input_list[l], input_list[k], input_list[j],input_list[i]

    return input_list

swap(words, 0,1,2,3)

# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(str):

    counts = dict()

    words = str.split()

    for word in words:

        if word in counts:

            counts[word] += 1

        else:

            counts[word] = 1

    return counts

print( word_count('In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'))

# Exercise #3
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.¶

nums_list = [10,23,45,70,11,15]
target = 70

def search(a_string, y):
 
    for i in range(len(a_string)):
         if a_string[i] == y:
            return i
         else:
                print(-1)
    return -1

search(nums_list, 70)
