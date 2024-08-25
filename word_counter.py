import sys
#Displaying options
print("::::::  Count character using either of the method ::::::")
print("::::::::  A. Using Input : ")
print("::::::::  B. Selecting file : ")
#Selecting option among two
choice=input("Enter your Preferred choice (A/B): ")

#Match case block
match choice:
    case "A" | "a":
        string_input=input("   ENTER THE SENTENCE OF YOUR CHOICE : ")
        #Defining the function to count words in sentence or paragraph
        def count_words(string_input):
            #splits a string into a list.
            words=string_input.split()
            #returns the number of items in an list.
            num_words=len(words)
            return num_words

        #Defining the function to count lines in paragraph
        def count_lines(string_input):
            lines=string_input.split("\n")
            num_liness=len(lines)
            return num_liness

        #Defining the function to count character in sentence/paragraph
        def count_char(string_input):
            num_char=len(string_input)- string_input.count('\n') - string_input.count(' ')
            return num_char

        num_words=count_words(string_input)
        num_lines=count_lines(string_input)
        num_char=count_char(string_input)

        print("The number of words:",num_words)
        print("The number of lines:",num_lines)
        print("The number of characters:",num_char)

    case "B" | "b":
        String_input2=input("     ENTER FILE NAME WITH CORRECT EXTENSION : ")
        try:
            String_input2=open(String_input2, "r")
            inf=String_input2.read()
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(0)
        #Defining the function to count words in sentence or paragraph
        def count_words(inf):
            #splits a string into a list.
            words=inf.split()
            #returns the number of items in an list.
            num_words=len(words)
            return num_words

        num_words=count_words(inf)

        #Defining the function to count lines in paragraph
        def count_lines(inf):
            lines=inf.split("\n")
            num_liness=len(lines)
            return num_liness

        #Defining the function to count character in sentence/paragraph
        def count_char(inf):
            num_char=len(inf)- inf.count('\n')-inf.count(' ')
            return num_char

        num_words=count_words(inf)
        num_lines=count_lines(inf)
        num_char=count_char(inf)
        if num_char == 0:
            print("File is Empty")
            sys.exit(0)

        print("The number of words:",num_words)
        print("The number of lines:",num_lines)
        print("The number of characters:",num_char)

    case _:
        print("Invalid choice")
