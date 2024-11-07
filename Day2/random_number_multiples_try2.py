#QUESTION: CREATE A DICTIONARY WITH KEYS- STATUS CODE, STATUS MESSAGE AND DATA
# IF MULTIPLES ARE FETCHED, STATUS CODE MUST PRINT 1 AND STATUS MESSAGE MUST BE "SUCCESSFULLY FETCHED"
# IF MULTIPLES ARE NOT FETCHED, STATUS CODE MUST PRINT 0 AND STATUS MESSAGE MUST BE "FAILED"

def display(n):
    x= {
        "code":0,
        "msg":"Failed",
        "data" : None
    }
    if n!=0:
        x["code"]=1
        x["msg"]='Successfully fetched'
        x["data"]= [n*i for i in range(1,6)]
    return x
 
def start():      
    num=int(input("Enter a number"))    
    print(display(num))
 
start()