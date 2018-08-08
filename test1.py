import pdfkit


path_wkthmltopdf = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
#pdfkit.from_url('http://bts-resumes.herokuapp.com', "out2.pdf", configuration=config)
#pdfkit.from_string('MicroPyramid', 'micro1.pdf', configuration=config)

#pdfkit.from_file('C:/Users/Asus X5555LJ-X01034T/Desktop/resumes_2/formuploads/templates/formuploads/success.html', 'micro2.pdf', configuration=config)
pdfkit.from_url('http://bts-resumes.herokuapp.com', 'micro3.pdf', configuration=config)
