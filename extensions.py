file = input("Name of the file: ")
file = file.lower().strip()
ext = file.split(".")
#for last element we use: list[-1]
match ext[-1]:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _ :
        print("application/octet-stream")


