# Pseudo Code
# Define sentence to be the string "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Replace all "!"s with a space
# Print out the cleaned sentence
# Define the cleaned sentence as a new variable
# Print out the cleaned sentence in all upper case letters
# Print out the cleaned sentence in reverse

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog." # Defines sentence to be the string "The!quick!brown!fox!jumps!over!the!lazy!dog."

print(sentence.replace('!', " ")) # Replaces all "!"s with a space and prints out the sentence

sentence_clean = sentence.replace('!', " ") # Defines the cleaned sentence as a new variable

print(sentence_clean.upper()) # Prints out the cleaned sentence in all upper case letters

print(sentence_clean[::-1]) # Prints out the cleaned sentence in reverse