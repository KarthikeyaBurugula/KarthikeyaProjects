#Word and Paragraph recommendation System.


#In this Project we are trying to take a paragraph as an input from the user and ldiscover how many words are present in it and determine
#how many vowel words present in it in addion to it and represent the occurance of each word as well finally provide some recommendations too.

#Let us take a sample paragraph and let us name it as para

para="Hi my name is Karthikeya I am an Engineering fresher and skilled in Python and SQL and have been working on them since 1 year in addition having a bisc idea of HTML R an Java as well, my aim is to score a super dream 12 Lpa Job and work in Bangalore for that i am working hard without loosing hope and praying to god with a belief that I can do my best and God will do the rest i have faith in god that he nevere let me fail and help me to reach my goal and succeed and start my career  with a bang"
print(para)

#Module 1 In this module we will try to know how many words are present in the paragraph.
#Let us split the paragraph as list of words.

Words=para.split()  #By using split method we have divided the paragraph into the list of words into individual words whenever space occurs
print("The list of words that are present in the para are ")
print(Words)
print()
print("The number of words that are present in the paragraph are",end=" ")
print(len(Words))
#So these are the total number of words that are present in the paragraph.
#But there are some repetations of words in the paragraph.
#In order to know how many distinct words present in the paragraph we will be converting the list in to set.

Distinct_words=set(Words)
print("The Distinct words that are present in the paragraph are ")
print()
print(Distinct_words)
print()
print("The number of distinct words present in the paragraph are ",end=" ")
print(len(Distinct_words))

#We have seen how many words that are present in the paragraph and determined how many distinct words that are present.

#Module 2 In this module we try to figure out how the occurances of each word and zip it up in to a dictionary.
#Let us take the distinct word and see their occurance in the original list.

for i in Distinct_words:
    #We are taking the entry from the distinct set of words
    print(i,end=" ")
    #By taking the words we are retriving the count of the word in Words the original list.
    print(Words.count(i))

#Lets zip the words and their occurances into a dictionary.
Word_Occurances={}
for i in Distinct_words:
    Word_Occurances[i]=Words.count(i)

print()
print("The words and their occurances are ")
print()
print(Word_Occurances)