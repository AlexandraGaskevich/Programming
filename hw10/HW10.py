import re

with open ("hamster.html", "r", encoding="utf-8") as f:

    wiki = f.read()

otryad = re.findall('Отряд[^А-Я]+\w*', wiki)

result = re.search(r'\w*$', otryad[0])


print("Отряд:", result.group())
