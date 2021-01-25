from PyPDF2 import PdfFileMerger, PdfFileReader
import os, sys
 
sys.setrecursionlimit(50000)
dir_in = ('/Users/Name/Desktop/2012pdfs')
os.chdir(dir_in)
dir_out = 'merged_pdfs'
 
pdfs = [name for name in os.listdir(dir_in) if name.endswith(".pdf")]
 

if os.path.exists(dir_out):
    pass
else:
    try:
        os.mkdir(dir_out)
    except OSError:
        print ("Could not create output dir %s " % dir_out)
        sys.exit(1)
    else:
        print ("Created output dir %s " % dir_out)

pdfs.sort(reverse=False)
print("Number of pdfs: " + str(len(pdfs)))
 
batch_pdfs = []
 
list_of_batches= []

batchsize = 500
print("Batchsize: " + str(batchsize))
 
for count, pdf in enumerate(pdfs, 1):        
    batch_pdfs.append(pdf)
    if count % batchsize == 0:
        list_of_batches.append(batch_pdfs)
        batch_pdfs = []
    if count > len(pdfs) + 2:
        print('List count larger than number of PDFs.')        
        os.sys.exit(1)
    
list_of_batches.append(batch_pdfs)
print("No of batches: "+str(len(list_of_batches)))
 
i = 1
for batchlist in list_of_batches:
    print("Processing Batch: " + str(i) + " with length: " + str(len(batchlist)))    
    if len(batchlist) > 0:
        merger = PdfFileMerger()
        for pdf in batchlist:
            try:
                with open(pdf, "rb") as file:                           
                    merger.append(PdfFileReader(file))
            except:
                print("error merging: " + pdf)
        merger.write(dir_out+"/"+"Merged-"+str(i)+".pdf")
        merger.close()
    i+=1
 
print('Check folder: \"'+ dir_out + '\" for PDFs.')
print('Process Complete')