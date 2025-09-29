
d1 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Primeras páginas</title>
</head>
<body>
<h1>Artículos</h1>
<hr>
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

f = open('pdrfrev.html','w', encoding='utf-8')
f.write(d1)

i = 0
while i < len(li):
    nombre = li[i]
    src = 'pdfs/' + nombre
    f.write('<h2>' + nombre + '</h2>\n')
    f.write('<embed src="' + src + '" type="application/pdf">\n')
    f.write('<hr>\n')
    i = i + 1

f.write(d2)
f.close()

