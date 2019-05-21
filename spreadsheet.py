import os

# Command 1:
def count_files(folder_path):
    dirList = os.listdir(folder_path)
    for file in dirList:
        print(file)
    return len(dirList)

# Command 2:
def read_all(file_name):
    data = []
    # Read and write a file. If the file not exists, then create that file
    f = open(file_name, 'a+')
    f.seek(0)
    for line in f:
        data.append(line.strip().split(';'))
    return data

# Command 3:
def sort_goods_by_name(A):
    for i in range(1, len(A)): 
        index = i
        for j in range(i+1, len(A)): 
            if A[j][1] < A[index][1]: 
                index = j
        # Swap the found minimum element with the first element         
        A[i], A[index] = A[index], A[i]
    for i in range(1, len(A)):
        print(A[i], '\n')

# Command 4:
def increase(A):
    amount = int(input("Amount to increase: "))
    array = list(map(int,input("Input number of good that need to increase: ").split()))
    for i in array:
        A[i][3] = ' ' + str(int(A[i][3]) + amount)
    return A

# Command 5:
def save_into_new_file(A, file):
    f = open(file, 'a')
    for item in A:
        f.write(';'.join(item) + '\n')
    f.close()

def edit_file(filename, A):
    print('... Editing file {}'.format(filename))
    # Commands for editing file
    command = ''
    while command not in ['no', '0', 'N']:
        print('''
Menu:
    0. Exit program\n
    1. File View\n
    2. Product View by name\n
    3. Product View by number\n
    4. Add product\n
    5. Save information into new file.
        ''')
        command = input('Enter command: ')
        if command not in ['0', '1', '2', '3', '4', '5', 'yes', 'Y', 'no', 'N']:
            print('Invalid')
            continue
        if command == '1':
            # Change the path in the code
            print('There are', count_files("C:/Users/ThucUyen/Desktop/Lab Files"), 'files')
        elif command == '2':
            read_all('products.txt')
            print("File readed")
        elif command == '3':
            B = A
            sort_goods_by_name(B)
        elif command == '4':
            A = increase(A)
        elif command == '5':
            save_into_new_file(A, 'newfile.txt')
    return True

A = read_all('products.txt')
edit_file('products.txt', A)