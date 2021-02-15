def rem_vowel(string):
	vowels = ('a','e','e','i','o','u')
	for x in string.lower():
		if x in vowels:
   			string = string.replace(x,"")
	print(string) 
string= "programe"
rem_vowel(string)
			