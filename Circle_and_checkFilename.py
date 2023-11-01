import math
r=float(input("Input the radius of the circle :"))
area=math.pi*r*r
print("The area of the circle with radius",r,"is",area)

filename=input("Input the Filename:")
split=filename.split('.',1)
if split[1]=='py':
    print("The extension of the file is :'Python'")
elif split[1]=='java':
    print("The extension of the file is :'Java'")
elif split[1]=='c':
    print("The extension of the file is :'C'")
elif split[1]=='txt':
    print("The extension of the file is :'Text file'")
elif split[1]=='doc' or split[1]=='docx':
    print("The extension of the file is :'Word Document'")
elif split[1]=='xls' or split[1]=='xlsx':
    print("The extension of the file is :'Excel Spreadsheet'")
elif split[1]=='ppt' or split[1]=='pptx':
    print("The extension of the file is :'Powerpoint Presentation'")
else:#assuming there are no more types of files
    print("Invalid Input")