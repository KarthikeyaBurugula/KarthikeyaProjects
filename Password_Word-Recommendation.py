#Word an Password Recommendation System.
print("Enter 1 for Word Recommendation System")
print("Enter 2 for Password Recommendation System")

choice=int(input())

if choice==1:
    # Word and Paragraph recommendation System.
    print("Welcome to word Recommendation System")

    # In this Project we are trying to take a paragraph as an input from the user and ldiscover how many words are present in it and determine
    # how many vowel words present in it in addion to it and represent the occurance of each word as well finally provide some recommendations too.

    # Let us take a sample paragraph and let us name it as para

    print("Kindly enter your text here")

    para = input()
    print(para)

    # Module 1 In this module we will try to know how many words are present in the paragraph.
    # Let us split the paragraph as list of words.

    Words = para.split()  # By using split method we have divided the paragraph into the list of words into individual words whenever space occurs
    print("The list of words that are present in the para are ")
    print(Words)
    print()
    print("The number of words that are present in the paragraph are", end=" ")
    print(len(Words))
    # So these are the total number of words that are present in the paragraph.
    # But there are some repetations of words in the paragraph.
    # In order to know how many distinct words present in the paragraph we will be converting the list in to set.

    Distinct_words = set(Words)
    print("The Distinct words that are present in the paragraph are ")
    print()
    print(Distinct_words)
    print()
    print("The number of distinct words present in the paragraph are ", end=" ")
    print(len(Distinct_words))

    # We have seen how many words that are present in the paragraph and determined how many distinct words that are present.

    # Module 2 In this module we try to figure out how the occurances of each word and zip it up in to a dictionary.
    # Let us take the distinct word and see their occurance in the original list.

    for i in Distinct_words:
        # We are taking the entry from the distinct set of words
        print(i, end=" ")
        # By taking the words we are retriving the count of the word in Words the original list.
        print(Words.count(i))

    # Lets zip the words and their occurances into a dictionary.
    Word_Occurances = {}
    for i in Distinct_words:
        Word_Occurances[i] = Words.count(i)

    print()
    print("The words and their occurances are ")
    print()
    print(Word_Occurances)

    # Module 3

    # In this module we will try to find out which word has occured the most times and try for some recommendations.

    m = list(Word_Occurances.keys())
    n = list(Word_Occurances.values())
    # Finding out the maximum value in values list ie n.
    y = max(n)
    z = n.index(y)
    x = m[z]
    print("The maximum occured word of the Paragraph is  ", x)

    # Recommendations
    # Let us do some of the Common recommendations to improve the grammer of the paragraph.

    if x == 'and':
        print("Dear user you have used the word ", x,
              " heavily insted of it you can improvize it by adding Words like IN ADDITION TO IT,FURTHER MORE, IN SUMMARY and so on")
    else:
        print("Dear user you have used the word ", x,
              " heavily insted of it you can improvize it by adding Some Synnonyms or Phrasal verbs related to it")

    # Moule 4

    # In this module we will try to divide how many words are starting with owels and how many are consonents.
    # Lets take the distinct set of words

    vowels = []
    consonents = []

    for i in Distinct_words:
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' or i[0] == 'E' or i[
            0] == 'I' or i[0] == 'O' or i[0] == 'U':
            vowels.append(i)
        else:
            consonents.append(i)

    print("The Vowels are ")
    print(vowels)
    print()
    print("The Consonents are ")
    print(consonents)
    print()
    print("The number of vowels are ", len(vowels))
    print()
    print("The number of consonents are ", len(consonents))


elif choice==2:
    #Password Recommendation and generation
    #In this password recommendation system we will try to analyze the strength of the password that they have entered and recommend some best password for them.
    print("Welcome Password Recommendation System")
    print("The Password should contain a minimum of 8 and a maximum of 15 charecters")
    print("Kindly enter your password")
    password=input()
    #Finding the length of password
    x=len(password)
    if x<8:
        print("Shortage in length of password kindly enter a password of length minimum of 8 charecters")
    elif x>15:
        print("Limited length of password is breached kindly enter password of length range between 8 and 15 ")
    elif x>=8 and x<=15:
        if any(i.isupper() for i in password):
            pass
        else:
            print("Kindly Include an upper case letter in your password")
        if any(i.isnumeric() for i in password):
            pass
        else:
            print("Kindly include some digits between 0-9 in your password")

        if '@' not in password or '$' not in password or '#' not in pasword or '*' not in password:
            print("Password is a bit weak")
            password=password+'@123$'
            print("We recommend you to keep this as password ",password)





