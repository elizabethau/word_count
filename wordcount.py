def word_count(file_name):
    # counts the amount of each word in the txt file
        
    text = open(file_name)

    big_text = []

    for line in text:

        line = line.strip()

        text_list = line.split(" ")

        big_text.extend(text_list)

    my_dict = {}

    for word in big_text:

        my_dict[word] = my_dict.get(word, 0) + 1

    for key, val in my_dict.items():

        print(key, val)

    return


word_count("test.txt")
