# O(N) Time, O(N) Space
def caesarCipherEncryptor(string, key):
    output = ""
	
	for char in string:
		position = ord(char) - ord("a") + key
		new_letter = chr((position % 26) + ord("a"))
		output += new_letter
	
    return output
