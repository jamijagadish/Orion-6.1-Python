# s = input("Enter a sentence: ").lower()

# split_words = s.split()
# print(split_words)

# for i in split_words:
#     print(len(i), end=' ')

# file = open('Python\PracticeSet1.txt', 'r')
# content = file.read()
# content = file.readline()
# content = file.readline(20)
# print(content)
# content = file.readlines()
# for i in content:
#     print(i)

# file.close()

# with open('Python\PracticeSet1.txt', 'r') as f:
#     content = f.read()
#     print(content)

# with open('Python\PracticeSet1.txt', 'w') as f:
    # f.write("Hello World")
    # f.writelines(["Hello World\n", "How are you?"])
    # print( f.writable())
    # print( f.readable())
    # print("Write Operation Completed")

# with open('Python\example.txt', 'w') as f:
#     f.write("Hello World")


# with open('Python\example.txt', 'a') as f:
#     f.write("\nThis is a new line")
#     print(f.readable())
#     print(f.writable())

# with open('Python\example.txt', 'a+') as f:
#     f.write("\nThis is a new line")
#     # print(f.readable())
#     # print(f.writable())
#     f.seek(0)
#     content = f.readlines()
#     print(content)

# with open('Python\example.txt', 'r+') as f:
#     f.seek(0)
#     content= f.read()
#     print(content)
#     f.write("\nThis is another new line")

with open('Python\example.txt', 'w+') as f:
    f.write("This is a new line")
    f.seek(0)
    content= f.read()
    print(content)
    # print(f.readable())
    # print(f.writable())