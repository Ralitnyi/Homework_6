from pathlib import Path
import sys
import shutil
import os

p = Path(sys.argv[1])
path_to_python_file = Path()

def find_oll_file(paht, files = []):
    for element in paht.iterdir():
        
        if element.is_dir():
            find_oll_file(element)

        else:
            files.append(element)
            
    return files
# print(find_oll_file(p))

def normalize():
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    normalize_files = []
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    
    
    for file in find_oll_file(p):
        
        file_name = file.name
        new_name = file_name.translate(TRANS)
        path_to_file = os.path.dirname(file)
        
        for char in new_name:
            if char not in '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.':
                new_name = new_name.replace(char, '_')
            

        # rename file name 
        shutil.move(file, f'{path_to_file}\{new_name}')
        

        new_file = Path(f'{path_to_file}\{new_name}')
        normalize_files.append(new_file) 
    return normalize_files


def file_move():
    for file in normalize():
        file_name = file.name
        if file_name.endswith('.png') or file_name.endswith('.jpeg') or file_name.endswith('.jpg') or file_name.endswith('.svg'):                  
            try:
                os.makedirs(f'{p}\images')
            except FileExistsError:
                pass
            try:                     
                shutil.move(file, f'{p}\images' )
            except shutil.Error:
                continue
            
        elif file_name.endswith('.avi') or file_name.endswith('.mp4') or file_name.endswith('.mov') or file_name.endswith('.mkv'):
            try:
                os.makedirs(f'{p}\\video')
            except FileExistsError:
                pass
            try:                    
                shutil.move(file, f'{p}\\video' )
            except shutil.Error:
                continue
            

        elif file_name.endswith('.doc') or file_name.endswith('.docx') or file_name.endswith('.txt') or file_name.endswith('.pdf')\
            or file_name.endswith('.xlsx') or file_name.endswith('.pptx'):
            try:
                os.makedirs(f'{p}\documents')
            except FileExistsError:
                pass
            try:                               
                shutil.move(file, f'{p}\documents' )
            except shutil.Error:
                continue
            
        elif file_name.endswith('.mp3') or file_name.endswith('.ogg') or file_name.endswith('.wav') or file_name.endswith('.amr'):
            try:
                os.makedirs(f'{p}\\audio')
            except FileExistsError:
                pass
            try:                               
                shutil.move(file, f'{p}\\audio' )
            except shutil.Error:
                continue
            
        elif file_name.endswith('.zip') or file_name.endswith('.gz') or file_name.endswith('.tar'):
             
            shutil.unpack_archive(file, f'{p}\\archives')
            os.remove(file)
            

    for folder_in_dir in p.iterdir():
        if folder_in_dir.name != 'archives' and folder_in_dir.name != 'audio' and folder_in_dir.name != 'documents'\
            and folder_in_dir.name != 'video' and folder_in_dir.name != 'images':
            try:
                os.rmdir(folder_in_dir)
            except OSError:
                continue

       
if __name__ == '__main__':
    file_move()



