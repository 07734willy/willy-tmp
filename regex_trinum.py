import re

def is_tri_num(text):
	text += "~9876543210-"
	while not re.match(r"-*~", text):
		text = re.sub(r"^(-*)0(?=\d)|^(-*)(?:0|([1-9])(?=[\d~]*\3(\d)\d*(-)))", r"\2\5\5\4\1\1\1\1\1\1\1\1\1\1", text)
	text = re.sub(r"~.*", r"", text)
	match = re.match(r"^-{0,2}$|^(--+)(?=\1+$)(?=-(?:\1-)+$)(?!\1*(\1-)+$)", text)
	return bool(match)

value = input()
print(is_tri_num(value))
