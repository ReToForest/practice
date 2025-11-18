a = [1,2,2,3,"hello",[1,2,3]]
b = (1,2,3,"a","a",1,2)
c = {'name1':'sakura','age1':'18','grade1':'72','name2':'light','age2':'17','grade2':'100'}
d1 = {1,2,3,4}
d2 = {3,4,5,6}

print(f"{a[4]}\n")    #查询

a[1] = "world"
print(f"{a[1]}\n")    #修改

a.insert (1,"hi")
print(f"{a[1]}\n")    #插入

a.remove ("hello")
print(f"{a}\n")       #删除

a.append (True)
print(f"{a}\n")       #添加

print(f"{b.count("a")}\n") #统计a出现次数

print(f"{b.index(3)}\n")   #查询下标

c.update({"name3":"L","age":"17","grade":"100"})
print(f"{c}\n")            #添加

c.update({"name3":"ryusaki"})
print(f"{c["name3"]}\n")   #修改

print(f"{c.pop("name3")}\n")
print(f"{c}\n")            #删除

print(f"{c}\n")        #遍历

print(f"{d1 | d2}\n")     #并集
print(f"{d1 & d2}\n")     #交集

