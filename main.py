def count_and_replace_terrible(input_text):
    count = 0
    words = input_text.split()
    new_words = []
    replace_terrible = False

    for word in words:
        cleaned_word = word.strip(".,?!")
        if cleaned_word == "terrible":
            count += 1
            if replace_terrible:
                new_words.append("pathetic")
            else:
                new_words.append("marvellous")
            replace_terrible = not replace_terrible
        else:
            new_words.append(word)

    new_text = " ".join(new_words)
    return count, new_text

def main():
    with open("file_to_read.txt", "r") as file:
        input_text = file.read()

    count, new_text = count_and_replace_terrible(input_text)

    with open("result.txt", "w") as file:
        file.write(new_text)

    print("Total number of 'terrible':", count)

if __name__ == "__main__":
    main()