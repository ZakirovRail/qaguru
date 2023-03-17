from zipfile import ZipFile


with ZipFile("resources/Архив.zip") as zip_:
    print(zip_.namelist())
    text = zip_.read("text")
    print(text)
    zip_.extract("text1")