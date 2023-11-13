import json

with open("libros.json", "r") as libros:
    data = json.load(libros)

for i in data:
    if i["titulo"] == "The Little Prince":
        print(i["autor"])
