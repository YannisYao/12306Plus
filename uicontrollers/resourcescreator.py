import subprocess, os


if __name__ == '__main__':
    images = os.listdir('./resources/images')
    qss = os.listdir('./resources/qss')
    f = open('resources.qrc', 'w+')
    f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

    for item in images:
        f.write(u'<file alias="images/'+ item +'">resources/images/'+ item +'</file>\n')

    for item in qss:
        f.write(u'<file alias="qss/'+ item +'">resources/qss/'+ item +'</file>\n')

    f.write(u'</qresource>\n</RCC>')
    f.close()

    pipepipe = subprocess.Popen(r'pyrcc5 -o resources.py resources.qrc', stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, creationflags=0x08)