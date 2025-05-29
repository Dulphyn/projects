# Nicolas Valdez Fri May  2 16:16:53 2025
# NicolasValdezEncryption
# Encrypts a text file with a given encryption method
# Input(s)
# A text file
# Output
# The text file after encryption
# For encryption, each character is converted into another using
# a specified dictionary

# File Names
fileName='text.txt'
outFileName='encryptedtext.txt'

# Exception List
zeroDivision='File is empty'
fileNotFound='File not found'
errors=(zeroDivision,fileNotFound)

# Welcoming Statement
print(f'Encrypts {fileName} using a code.')

# Encryption method
CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}

def empty(data):
    '''Test for empty file by the number of lines in the file.'''
    1/len(data)
    
def txtToList(fileName):
    ''''Validates file then puts data into a list'''
    error=False
    data=[]
    try:
        with open(fileName,'r') as infile:
            for line in infile:
                data.append(line.rstrip('\n'))
        empty(data)
    except ZeroDivisionError:
        print(errors[0])
        error=True
    except FileNotFoundError:
        print(errors[1])
        error=True
    finally:
        return(data,error)

data=txtToList(fileName)
if data[1]==False:
    tab=str.maketrans(CODE)
    encText=[]
    for line in data[0]:
        encText.append(line.translate(tab))

    with open(outFileName,'w') as outfile:
        for line in encText:
            outfile.write(f'{line}\n')
    
    print(f'{fileName} has been encrypted and saved as {outFileName}')

# Ending Note
print('Program Ends')