import zipfile as z

Target = 'demo.zip'

print("Starting to unzip the file..")

root = z.ZipFile(Target)
root.extractall('destination')
root.close

print('/nFile is successfully Unzipped')