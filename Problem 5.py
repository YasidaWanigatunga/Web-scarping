import camelot

pdf_path = 'sample.pdf'
#Using camelot libry read the sample.pdf
tables = camelot.read_pdf(pdf_path, pages='1')

if tables:
    # Save the first table as an HTML file
    first_table = tables[1]
    output_html_path = 'output_table.html'
    first_table.to_html(output_html_path)
    print(f"First table saved as {output_html_path}")
else:
    print("No tables found on the first page")
