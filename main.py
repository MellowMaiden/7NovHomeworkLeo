#07 November 2023 Homework by Leo(Bofu Liu)
print("Hello Stephen")
def errorcode(number):
    match number:
        case 404:
            print("Page not found")
        case 403:
            print("Page is forbidden")
        case 402:
            print("Page need payment")
        case 401:
            print("Page is unauthorized")
        case 400:
            print("Bad request")

errorcode(402)
quit()


