import zipfile, rarfile, os, re

zip_files = []
rar_files = []
downloads_folder = re.findall(r'\w:\\Users\\\w+\\', os.getcwd())[0]+'downloads\\'

for file in os.listdir(downloads_folder):
    if file.endswith('.zip'):
        zip_files.append(file)
    if file.endswith('.rar'):
        rar_files.append(file)

if len(zip_files) > 0 or len(rar_files) > 0:
    print('\nExtracted {} .zip and {} .rar files:'.format(len(zip_files), len(rar_files)))
else:
    print('\nNo compressed files to extract.')

for file in zip_files:
    with zipfile.ZipFile(downloads_folder+file, 'r') as my_zip:
        my_zip.extractall(downloads_folder+file[:-4])

    os.remove(downloads_folder+file)
    print(file)

for file in rar_files:
    with rarfile.RarFile(downloads_folder+file, 'r') as my_rar:
        my_rar.extractall(downloads_folder+file[:-4])

    os.remove(downloads_folder+file)
    print(file)

input('\nPress Enter to exit.')