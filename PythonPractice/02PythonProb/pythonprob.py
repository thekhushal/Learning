Sen = input("Enter your sentence: ") + " "# AIM HELLO YOU ALL
LenSen = len(Sen) # 17

dealBreaker = 0
for SpaceIndex in range(LenSen): # SpaceIndex - (0 - 16)

    if Sen[SpaceIndex] == " ": # 3, 9, 13
        for i in range(1, SpaceIndex+1): # i - ((1-3) (1-9) (1-13))
            CharIndex = SpaceIndex-i
            print(Sen[CharIndex], end = "") # Sen[2,1,0], sen[8,7,6,5,4]
            if CharIndex == dealBreaker:
                dealBreaker = SpaceIndex + 1
                break
        print(" ", end = "")
print()

# def reverse_sentence(sentence):
#     words = sentence.split()  # Split the sentence into words
#     reversed_words = [word[::-1] for word in words]  # Reverse each word
#     reversed_sentence = " ".join(reversed_words)  # Join the reversed words
#     return reversed_sentence

# input_sentence = "AIM HELLO YOU ALL"
# output_sentence = reverse_sentence(input_sentence)
# print(output_sentence)
