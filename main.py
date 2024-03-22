import string
alphabet = string.ascii_uppercase
print(alphabet[2])

chunks  = 100

for l in alphabet:
    print(l)
    letter = l

    with open(f'/by_letter/{l}.txt','r') as file:
        # print(f'{l}.txt')
        num_of_names = len(file.readlines())
        num_of_files = num_of_names // chunks
        last_chunk = num_of_names % chunks
        

    with open(f'/by_letter/{l}.txt','r') as file:

        count = 1
        file_name = f'/chunks_of_100/{l}-{count}00.txt'

        for i in range(num_of_files):

            with open(file_name,'w') as write:
                for i in range(100):
                    write.write(file.readline())
            count += 1
            file_name = f'/chunks_of_100/{l}-{count}00.txt'
        
        with open(file_name,'w') as write:
            for i in range(last_chunk):
                write.write(file.readline())



