def fileMediateType():
    extension = input("Enter the file name: ").strip().lower()

    # Media Type reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types
    if(extension.endswith(".gif")):
        return "image/gif"
    elif(extension.endswith(".jpg")):
        return "image/jpg"
    elif(extension.endswith(".jpeg")):
        return "image/jpeg"
    elif(extension.endswith(".png")):
        return "image/png"
    elif(extension.endswith(".pdf")):
        return "application/pdf"
    elif(extension.endswith(".txt")):
        return "text/txt"
    elif(extension.endswith(".zip")):
        return "application/zip"
    else:
        return "application/octet-stream"
    
def main():
    print(fileMediateType())

main()
    

