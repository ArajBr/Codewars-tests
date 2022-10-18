'''An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)'''


#Solution
def is_isogram(string):
    # Put the upper function to avoid the case sensitive
    string = string.upper()
    # Compares each item to the rest of the string, but never to themselves
    for i, k in enumerate(string):
        for j, l in enumerate(string):
            if (string[i] == string[j]) & (i != j):
                return False
    return True

