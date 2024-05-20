# 1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
import os
directory = "Example"

try:
    os.mkdir(directory)
    print(f"'{directory}' folderi yaradildi.")
except FileExistsError:
    print(f"'{directory}' adinda folder var. Basqa ad daxil edin.")

# 2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt kateqoriya(subdirectory) yaradırıq.
subdirectory = "Example/Subdirect"
try:
    os.makedirs(subdirectory)
    print(f"{subdirectory}' folderi '{directory}' folderinin icinde yaradildi.")
except FileExistsError:
    print(f"'{subdirectory}' adinda folder '{directory}' folderinin icinde var.")


# 3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
# (şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  
# daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
import shutil

image = 'fox.jpeg'  
path = os.getcwd()

image_path = os.path.join(path, image)
if os.path.exists(image_path):
    shutil.move(image_path, os.path.join(subdirectory, image))
else:
    print(f"sekil fayli tapilamdi: {image_path}")


text_path = os.path.join(subdirectory, 'text.txt')
with open(text_path, 'w', encoding='utf-8') as file:
    file.write("Qazananlar sadəcə biraz daha artıq cəhd edən uduzanlardır.")

print(f"'text.txt' fayli '{subdirectory}' qovluguna elave edildi.")


# 4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları
# subdirectorydən çıxarıb Example directory-sinə göndərirsiniz.
for i in os.listdir(subdirectory):
    if i.endswith('.txt'):
        shutil.move(os.path.join(subdirectory, i), os.path.join(directory,i))
