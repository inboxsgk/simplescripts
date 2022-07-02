import os
import shutil
import ast
import json

def files(path=None):
    if path == None:
        return os.listdir()
    else:
        return os.listdir(path=path)
      
def cur_path():
    return os.getcwd()
  
def check(file =None, path = cur_path()):
    if file == None:
        return os.path.exists(path)
    else:
        return os.path.exists(os.path.join(path, file))
      
def copyfile( file=None, to_dir=None, from_dir=cur_path()):
    if to_dir == None:
        return "DestinationError"
    elif file == None:
        return "FileError"
    else:
        from_dir = os.path.join(from_dir, file)
        to_dir = os.path.join(to_dir, file)
        if check(file, to_dir) == True:
            return "FileExistError"
        else:
            try:
                shutil.copyfile(from_dir,to_dir)
            except FileNotFoundError:
                return "FilenotfoundError"
            else:
                return "Completed"
              
def overwritefile( file=None, to_dir=None, from_dir=cur_path()):
    if to_dir == None:
        return "DestinationError"
    elif file == None:
        return "FileError"
    else:
        from_dir = os.path.join(from_dir, file)
        to_dir = os.path.join(to_dir, file)
        if check(file, to_dir) == True:
            try:
                shutil.copyfile(from_dir,to_dir)
            except FileNotFoundError:
                return "FilenotfoundError"
            else:
                return "Completed"
        else:
            return "FileNotexistError"
          
def movefile( file=None, to_dir=None, from_dir=cur_path()):
    if to_dir == None:
        return "DestinationError"
    elif file == None:
        return "FileError"
    else:
        from_dir = os.path.join(from_dir, file)
        to_dir = os.path.join(to_dir, file)
        if check(file, to_dir) == True:
            return "FileExistError"
        else:
            try:
                shutil.move(from_dir,to_dir)
            except FileNotFoundError:
                return "FilenotfoundError"
            else:
                return "Completed"
              
def fileordir(object, path):
    if object == None:
        return "NameError"
    else:
        usage_path = os.path.join(path, object)
        if os.path.isdir(usage_path):
            return "directory"
        elif os.path.isfile(usage_path):
            return "file"
          
def filesize(file, path=cur_path(), raw=False):
    def decimal_org(val):
        l = []
        for i in str(val):
            l.append(i)
        dec = l.index(".")
        dec_part = l[dec:]
        new_ind = len(dec_part) - 3
        new_dec_part = dec_part[:-new_ind]
        r = ""
        for i in l[:dec]:
            r+=i
        for i in new_dec_part:
            r += i
        return r
    if raw == False:
        if check(file, path):
            x = os.stat(os.path.join(path, file)).st_size

            if x >= 1024:
                if (x /1024) < 1024:
                    x = x/1024
                    r = str(decimal_org(x)) + " Kb"
                    return r
                else:
                    f = float(x / (1024 ** 2))
                    if f <= 1024:
                        r = str(decimal_org(f)) + " Mb"
                        return r
                    elif f> 1024:
                        r = str(decimal_org(f/1024)) + " gb"
                        return r
            else:
                r = str(x) + " Bytes"
                return r
        else:
            return "FileNotFoundError"
    else:
        x = os.stat(os.path.join(path, file)).st_size
        return x
      
def create_path(path = None):
    if path == None:
        return "PathError"
    else:
        try:
            os.makedirs(path)
        except FileExistsError:
            return "FileExistsError"
          
def scan(path):
    files_list = []
    folders_list = []
    file_list = files(path)
    for i in file_list:
        filetype = fileordir(i, path)
        if filetype == "directory":
            folders_list.append(i)
        else:
            files_list.append(i)
    return [files_list, folders_list]

def file_ext(file):
    l = []
    for i in file:
        l.append(i)
    l = l[::-1]
    try:
        fstop_i = l.index(".")
    except ValueError:
        return None
    else:
        ext = l[:fstop_i][::-1]
        r = "."
        for i in ext:
            r+=i
        return r

      

def read_dict(file_path):
    file = open(file_path, "r")
    data = file.read()
    data = ast.literal_eval(data)
    file.close()
    return data
  
def write_dict(file_path, data):
    file = open(file_path, "w")
    file.write(json.dumps(data))
    file.close()
