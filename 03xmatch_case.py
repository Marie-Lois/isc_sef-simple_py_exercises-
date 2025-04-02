status_code = 404

def match_case(status_code):
    match status_code:
        case 200:
            print("Ok: The request was successful.")
        case 3001:
            print("Moved permanently: The source has been permanently removed.")
        case 404:
            print("Not found: The requested resource was not found.")
        case 500:
            print("Internal server error: The server encountered and error.")
        case _:
            print("Unknown status code: {status_code}")
            
match_case(status_code)