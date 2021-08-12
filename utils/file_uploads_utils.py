from werkzeug.utils import secure_filename
from datetime import datetime
import os
UPLOAD_FOLDER = 'public/files'


def save_uploaded_file(file):
    filename = secure_filename(file.filename)
    current_time = datetime.now()
    time_str = datetime.strftime(current_time, '%Y%m%d%H%M%S%f_')
    file_location = os.path.join(UPLOAD_FOLDER, time_str+filename).replace(os.sep, '/')
    file.save(file_location)
    return file_location[7:]
