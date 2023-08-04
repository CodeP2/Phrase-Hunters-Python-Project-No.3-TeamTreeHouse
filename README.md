# Phrase-Hunters-Python-Project-No.3-TeamTreeHouse
Phrase Hunters Game


Hello heres my explaination for couple of things in my code 
I have been practising a lot before taking this project so I wasn't using google
(and making my own versions of this project the only difference is that I did it in one file instead)

altho I have to explain this line:

if any(char in string.punctuation for char in guess_letter)\
                or len(guess_letter) > 1:
https://docs.python.org/3/library/functions.html?highlight=any#any
https://docs.python.org/3/library/string.html?highlight=string%20punctuatio#string.punctuation

this code here uses any and returns True if in this case a char is punctuation sign (string.punctuation) for each char in my guess (guess_letter) if it is
it returns True and raises Value Error (len part of course check for the length)

elif guess_letter.isdigit():
                raise TypeError("Error")
https://docs.python.org/3/library/stdtypes.html?highlight=isdigit

this line check if the passed guess is an int, float and so on basically it checks if passed "letter" is a number or not if it is it returns Type Error

I think this two lines are the ones I have to explain if theres gonna be further questions about my code I will gladly answer but also I wasn't sure how much I should comment/doc so I wasn't using that much 
hopefuly the code isn't too unclear
