subjects=["c","c++","Java","Python","Basic"]
#kono list er length ber korte chaile
print(len(subjects))
#kono kicu shesha jog korte chaile..
subjects.append("TOC")
print(subjects)
#j khane chibo shekhane jukto korte chaile...
subjects.insert(2,"OS")
print(subjects)
# kono kicu  remove korte chaile...
subjects.remove("Java")
print(subjects)
#list a kono kicu sajhaite hole
subjects.sort()
print(subjects)
# ##########################################subjects a ebar number nei....#############################
subjects1=[34,35,56,34,67,555]
# list ti sajaite chaile
subjects1.sort()
print(subjects1)
#list ti reverse shajaite chaile
subjects1.reverse()
print(subjects1)
# kono kicu pop korte chaile
subjects1.pop()
subjects1.pop()
print(subjects1)
# list clear korte chaele
subjects1.clear()
print(subjects1)
#ekti function r ekti function a copy kore rakhte chaile
subjects1=[34,35,56,34,67,555]
subjects2=subjects1.copy()
print(subjects2)
#kono kicur position jante chaile...
sub=[34,323,564,6546,456,45654,4456,54]
pos=sub.index(6546)
print(pos)
# kono ekta function oy list a kotobar ace ta jante chaile count function bebohar korte hobe
sub1=[34,323,564,6546,456,45654,4456,546546,6546,6546,6546,6546,]
pos=sub1.count(6546)
print(pos)

