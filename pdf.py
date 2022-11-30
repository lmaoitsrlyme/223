import PyPDF2 as pd
filename = input('path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not password protected! You can successfully open it!')

else:
    wordlistfile = open("wordlist.txt", "r", errors = "ignore")
    body = wordlistfile.read().lower() 
    words = body.split("\n")
    for i in range (len(words)):
        word = words[i]
        print("trying to decode the password " + str(word))
        result = pdfReader.decrypt(word)
        if (result == 1):
            print("sucecese the password is " + word)
            break
        elif (result == 0):
            tried += 1
            print("password tried: " + str(tried))
            