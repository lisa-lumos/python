# Working with PDFs and Spreadsheets with Python
Pandas could do this. It is a full data analysis library, can work with almost any tabular data type. It also does visualizations. 

Openpyxl is designed specifically for Excel files. 

Google Sheets Python API has direct Python API with Google spreadsheets. Allows you to directly make changes to the spreadsheets hosted online. Available to many programming languages. 

## csv files
```py
import csv
data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data) # a col list of row val lists
for line in data_lines[:5]:
    print(line) # print the first 5 rows
# write to a csv file: 
output_file = open('saved-file.csv', mode='w', newline='')
csv_writer = csv.writer(output_file, delimiter=',')
csv_writer.writerow(['a', 'b', 'c']) # write a single row
csv_writer.writerows(['1', '2', '3'], ['4', '5', '6']) # write multiple rows
output_file.close()
f = open('saved-file.csv', mode='a', newline='') # append to this file
csv_writer = csv.writer(f)
csv_writer.writerow(['a2', 'b2', 'c2']) 
f.close()
```

## PDF files
```py
import PyPDF2 # pip install PyPDF2
f = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages) # show num of pages in the pdf file
page0 = pdf_reader.getPage(0) # grab the first page
page0_text = page0.extractText() # extract text as string
print(page0_text)
f.close()

# write to a new pdf file
f = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page0 = pdf_reader.getPage(0) 
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page0)
f_out = open('newfile.pdf', 'wb')
pdf_writer.write(f_out)
f_out.close()
```
