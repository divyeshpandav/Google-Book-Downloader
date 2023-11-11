import requests
from reportlab.pdfgen import canvas
from PIL import Image
from PyPDF2 import PdfFileMerger
import time
import os

# Read the .txt file to extract image links
with open("ebook.txt", "r") as file:
    image_links = file.read().splitlines()

pdf_merger = PdfFileMerger()

single_pdf_files = [] 
for i, image_url in enumerate(image_links):
    retry = 3  
    success = False

    while retry > 0 and not success:

        response = requests.get(image_url)

        if response.status_code == 200:
            with open(f"image_{i}.jpg", "wb") as file:
                file.write(response.content)
            print(f"Image {i} downloaded successfully as 'image_{i}.jpg'")
        else:
            print(f"Failed to download Image {i}, Retrying...")
        if os.path.exists(f"image_{i}.jpg"):
            success = True
        else:
            time.sleep(1)  
            retry -= 1

    if success:

        img = Image.open(f"image_{i}.jpg")
        img_width, img_height = img.size
        pdf_file = f"image_to_pdf_{i}.pdf"
        c = canvas.Canvas(pdf_file, pagesize=(img_width, img_height))
        c.drawImage(f"image_{i}.jpg", 0, 0, width=img_width, height=img_height)
        c.showPage()
        c.save()
        img.close() 
        print(f"Image {i} converted to PDF as 'image_to_pdf_{i}.pdf")
        
        single_pdf_files.append(pdf_file) 

    else:
        print(f"Failed to download Image {i} after retries")

    if success:
        pdf_merger.append(f"image_to_pdf_{i}.pdf")

    if os.path.exists(f"image_{i}.jpg"):
        os.remove(f"image_{i}.jpg")

with open("merged_images.pdf", "wb") as output_pdf:
    pdf_merger.write(output_pdf)

for pdf_file in single_pdf_files:
    if os.path.exists(pdf_file):
        os.remove(pdf_file)

print("All images merged into 'merged_images.pdf', and single PDF and image files removed")
