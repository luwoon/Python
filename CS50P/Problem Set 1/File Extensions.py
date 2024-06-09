dict = {
  ".gif": "image/gif",
  ".jpg": "image/jpg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".txt": "text/plain",
  ".zip": "application/zip"
}

for extension, type in dict.items():
  if s.endswith(extension):
    print(type)
    break
else:
    print("application/octet-stream")
