from PyPDF2 import PdfReader

reader = PdfReader("docs-pytest-org-en-latest.pdf")

numbers_of_pages = len(reader.pages)
text = reader.pages[0].extract_text()

print(text)
print(f"num of pages: {numbers_of_pages}")

assert "pytest Documentation" in text
