import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

           
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                   
                local_path = os.path.join(root, filename)

                   
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'wKUHa8pWbU4AAAAAAAAAAWw2UJT9hr60PygsTZOl9L0YDKYw3N8NYiyX9kokCqhY'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the path of the file to be transferred: "))
    file_to = input("enter the folder in dropbox where the file should be uploaded ")  

    transferData.upload_file(file_from,file_to)
    print("file is now uploaded to dropbox! Enjoy :)")

main()
