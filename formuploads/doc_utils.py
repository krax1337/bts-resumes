from subprocess import Popen, PIPE
import os
import shutil

def doc_to_text(file_path):
    file_path = file_path[:-4]
    coding = "-mcp1251"
    cmd = 'antiword' + " " +coding + " " ' "./' + file_path + ".doc"+ '"' + " " + ">" + " ./upload/" + "new.txt"
    os.system(str(cmd))
    f = open('./upload/new.txt','r')
    result = []
    for line in f:
        if line != '\n':
            line = line.replace('\n', '')
            line = line.replace('|', '')
            line = " ".join(line.split())
            result.append(line)
    return result