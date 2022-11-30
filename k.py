import zipfile
import time

folderpath = input("path to the files: ")

zipf = zipfile.ZipFile(folderpath)

if not zipf:
    print("zipped file or folder is not password protected you can successfully open it")

else:
    starttime = time.time()
    result = 0
    c = 0

    characters = ['0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z', '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

    print("brute force started")

    if result == 0:
        print("checking for four character pASSword")

        for b in characters:
            for o in characters:
                for a in characters:
                    for t in characters: 
                        guess = str(b) + str(o) + str(a) + str(t)
                        password = guess.encode("utf-8").strip()
                        c += 1

                        try:
                            with zipfile.ZipFile(folderpath, "r") as zf:
                                zf.extractall(pwd = password)
                                print("success. the password is " + guess)    
                                endtime = time.time()
                                result = 1
                                break   
                        except:
                            pass

                    if (result == 1):
                        break
                
                if (result == 1):
                    break

            if (result == 1):
                break
        
    if (result == 0):
        print("sorry u r dumb you tried and failed a grand total of " + str(c) + " possible combinations tried in " + str(time) + " seconds haha lol die")    
    else:
        duration = endtime - starttime
        print("you finally found the password after " + str(duration) + " seconds and now the whole world is not waiting anymore")
