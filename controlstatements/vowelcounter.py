vowelList = ["a", "e", "i", "o", "u"]
word = input("Enter a word : ")
vowelCounter = {}
for vowel in vowelList: vowelCounter[vowel] = word.count(vowel)
for k,v in vowelCounter.items(): print("Vowel {} is present {} times in a given word".format(k,v))
# or
#for vowel in vowelList: print("Vowel {} is present {} times in a given word".format(vowel,vowelCounter.get(vowel,0)))
# or
#for vowel in vowelList: print("Vowel '{}' repeated {} times in a word".format(vowel,word.count(vowel)))
vowelCount = 0
for vowel in vowelList :
    if word != word.replace(vowel, ""): vowelCount+=1
print("Altogether, {} vowel(s) we have in a word".format(vowelCount))
