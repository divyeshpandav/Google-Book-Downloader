# Google-Book-Downloader [books.google.co.in]
Here simple step to download it 

step 1:  Check this repo and generate a link to all pages of Google Books.
https://github.com/mcdxn/google-books-preview-pages-downloader.git

      here steps for this repo.
      1) open the gbppd.js file and copy js code
      2) open Google Book which you have to download 
      3) right click on the page and  click to inspect 
      4) paste this code into the console and press enter
      5) now type gbppd.start() [page start for scrolling generate a link for every page]
      6) wait until the scroll complete
      7) type gbppd.finish()
      8) copy all links and follow the next step

step 2:
Copy all links and save them to eBook.txt files

step 3:
run pdfconvert.py and wait to generate eBook.pdf
 
```bash
  pip install reportlab
```

```bash
  pip install PyPDF2
```

```bash
  pip install Pillow
```
