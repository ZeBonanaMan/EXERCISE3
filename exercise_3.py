original_string = "pynative"
print("Original String is ", original_string)
print("Printing only even index chars")

length_word = len(original_string)

for i in range(0, length_word, 2):
    print(original_string[i])