"""
Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara 
görə neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci',
'4-cu','5-ci'] Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya 
uyğun sıralanacaq və nəticə  düzgün olmayacaq. (taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif
olacaq. Eyni xala sahib 2 şəxs olabilməz) Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.
"""

points = []

def Olympics():
    for i in range(5):
        point = int(input("Yarisda qazandiginiz xali daxil edin: "))
        points.append(point)

Olympics()

index_points = list(enumerate(points))

sorted_points = sorted(index_points, key=lambda x: x[1], reverse=True)

ranking = [0] * len(points)
for place, (index, point) in enumerate(sorted_points, start=1):
    ranking[index] = place


print("Yaris siralamasi: ", ranking)
