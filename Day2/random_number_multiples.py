#QUESTION: CREATE A DICTIONARY WITH KEYS- STATUS CODE, STATUS MESSAGE AND DATA
# IF MULTIPLES ARE FETCHED, STATUS CODE MUST PRINT 1 AND STATUS MESSAGE MUST BE "SUCCESSFULLY FETCHED"
# IF MULTIPLES ARE NOT FETCHED, STATUS CODE MUST PRINT 0 AND STATUS MESSAGE MUST BE "FAILED"

def multiples(number):
    multiples_list = []
    for i in range(1, 6):
        multiple = number * i
        multiples_list.append(multiple)
    return multiples_list  

def create_status_code(success):
    return int(success)

def create_status_message(success):
    messages = {True: "successfully fetched", False: "failed"}
    return messages[success]

def build_response(number):
    data = multiples(number)
    success = bool(data)

    return {
        "status_code": create_status_code(success),
        "status_message": create_status_message(success),
        "data": data
    }

def start():
    result = build_response(number=int(input("Enter the number:")))
    print(result)

start()

