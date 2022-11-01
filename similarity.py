from thefuzz import fuzz

text1 = open('data/huckfinn.txt')
text2 = open('data/tomsawyer.txt')
fuzz.ratio(text1, text2)
