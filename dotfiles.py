import subprocess
import filecmp

def removeDot(name):
    if name[0] == '.':
        return name[1:]
    else:
        return name

dotfiles = { \
        '.alias':'/home/nico/',\
        '.bash_profile':'/home/nico/',\
        '.bashrc':'/home/nico/',\
        '.env':'/home/nico/',\
        '.functions':'/home/nico/',\
        '.gitconfig':'/home/nico/',\
        'config':'/home/nico/.config/i3/',\
        '.inputrc':'/home/nico/',\
        '.prompt':'/home/nico/',\
        'vimrc':'/home/nico/.vim/'}

dotDir = '/home/nico/.dotfiles/'

for name,path in dotfiles.items():
    print(f'Working on file {path+name}')

    if not filecmp.cmp(f'{dotDir + removeDot(name)}',f'{path + name}'):
        subprocess.run(f"cp {path+name} {removeDot(name)}", shell=True, cwd=dotDir)
        subprocess.run(f"git add {removeDot(name)}", shell=True, cwd=dotDir)
        subprocess.run(f"git commit -m 'Update'", shell=True, cwd=dotDir)
        subprocess.run(f"git push -u origin master", shell=True, cwd=dotDir)
    else:
        print("All files are equal to source")


