'''
1. Read the file
2. calcualte word cound
3. calcualte line count
4. calculate character count
5. frequency of each word
'''



with open('input.txt') as file:
    lines = file.readlines()
    line_count = len(lines)
    char_count = 0
    words_count = 0
    frequency = {}

    for line in lines:
        char_count_in_line = len(line)
        char_count += char_count_in_line
        words = line.split(sep=" ")
        words_count += len(words)

        for word in words:
            raw = word.replace('\n' , '')
            count = frequency.get(raw)
            if count is None:
                frequency[raw] = 1
            else:
                frequency[raw] = count + 1



    print(frequency)
    print(f"Line Count is : {line_count}")
    print(f"Char Count is : {char_count}")
    print(f"Word Count is : {words_count}")
    