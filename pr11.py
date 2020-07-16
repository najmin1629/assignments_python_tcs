wordlist = ["This", "is", "a", "beautiful", "day"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))