
d1 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Artículos PDF</title>
</head>
<body>
<h1>Artículos PDF</h1>
'''

d2 = '''
</body>
</html>
'''

li = [
"1 vocal.pdf",
"2 Can.pdf",
"3 Spontaneous.pdf",
"4 BAASTA.pdf",
"5 Amping Up.pdf",
"6 Dopamine.pdf",
"7 Scales.pdf",
"8 Intrinsically.pdf",
"9 Modulates.pdf",
"10 Speech.pdf",
]

filo = open('index.html','w', encoding='utf-8')
filo.write(d1)

for ss in li:
    v1 = '<p><a href="pdfs/' + ss + '" target="_blank" rel="noopener">' + ss + '</a></p>\n'
    filo.write(v1)

filo.write(d2)
filo.close()

