

import os
# this function is used to check whether a given filename has allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# this function is used to save uploaded file in a specified directory
def save_uploaded_file(file):
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return filename
    else:
        return None