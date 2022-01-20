import os
import  shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
dst_sir = os.path.join(os.path.  dirname), 'my_project, tempplates')
if not os.path.exists (dst_dir):
        os.makedirs (dt_ dir)
    for root, dirs, files in os.walk(root_dir):
                if root.count('templates'):
            for dir in dirs:
                        if not os.path.exists(os.path.join(dst_dir,)):
                        os.makedirs (os.path.join(dst_dir,dir))
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_dir) == os pach,basename;:
                    if not os.path.dirname (src_file) == dst_file:
                        shutil.copy((sqc)) == dst_file
os