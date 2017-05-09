from ggplot import 

print("Single chart case")
g = GroupedData(mpg)
print("=> S1", None == g.getCategoriesByIndex())
print("=> S2", mpg.equals(g.getDataByIndex()["data"]))
print("=> S3", {} == g.getDataByIndex()["colCategories"])
print("=> S4", {} == g.getDataByIndex()["rowCategories"])
print("=> S5", mpg.equals(g.getDataByIndex(rowIndex=0)["data"]))
print("=> S6", mpg.equals(g.getDataByIndex(colIndex=0)["data"]))
print("=> S7", (1,1) == g.getShape())




print("Float row single dim chart case")
g = GroupedData(mpg, rowDims=["class"])

result = [[('class', '2seater')], [('class', 'compact')], [('class', 'midsize')],
         [('class', 'minivan')], [('class', 'pickup')], [('class', 'subcompact')], 
         [('class', 'suv')]]
print("=> FR1", all(x==y for x,y in zip(result, g.rowCategories)))
print("=> FR2", g.colCount is None)
print("=> FR3", 7 == g.rowCount)
print("=> FR4", 5 == g.getDataByIndex(rowIndex=0)["data"].shape[0])
try:
    5 == g.getDataByIndex(colIndex=0)["data"].shape[0]
    print("=> FR5", False)
except IndexError:
    print("=> FR5", True)
print("=> FR6", mpg.shape[0] == g.getDataByIndex()["data"].shape[0])
print("=> FR7", 62 == g.getDataByIndex(rowIndex=6)["data"].shape[0])
try:
    62 == g.getDataByIndex(rowIndex=7)["data"]
    print("=> FR8", False)
except IndexError:
    print("=> FR8", True)
print("=> FR9", (7,1) == g.getShape())




print("Float col single dim chart case")
g = GroupedData(mpg, colDims=["class"])

result = [[('class', '2seater')], [('class', 'compact')], [('class', 'midsize')],
         [('class', 'minivan')], [('class', 'pickup')], [('class', 'subcompact')], 
         [('class', 'suv')]]
print("=> FC1", all(x==y for x,y in zip(result, g.colCategories)))
print("=> FC2", g.rowCount is None)
print("=> FC3", 7 == g.colCount)
print("=> FC4", 5 == g.getDataByIndex(colIndex=0)["data"].shape[0])
try:
    5 == g.getDataByIndex(rowIndex=0)["data"].shape[0]
    print("=> FC5", False)
except IndexError:
    print("=> FC5", True)
print("=> FC6", mpg.shape[0] == g.getDataByIndex()["data"].shape[0])
print("=> FC7", 62 == g.getDataByIndex(colIndex=6)["data"].shape[0])
try:
    62 == g.getDataByIndex(colIndex=7)["data"]
    print("=> FC8", False)
except IndexError:
    print("=> FC8", True)
print("=> FC9", (1,7) == g.getShape())



print("Float row double dim chart case")

g = GroupedData(mpg, ["drv", "cyl"])
result = [[('drv', '4'), ('cyl', 4)], [('drv', '4'), ('cyl', 5)], [('drv', '4'), ('cyl', 6)],
          [('drv', '4'), ('cyl', 8)], [('drv', 'f'), ('cyl', 4)], [('drv', 'f'), ('cyl', 5)],
          [('drv', 'f'), ('cyl', 6)], [('drv', 'f'), ('cyl', 8)], [('drv', 'r'), ('cyl', 4)],
          [('drv', 'r'), ('cyl', 5)], [('drv', 'r'), ('cyl', 6)], [('drv', 'r'), ('cyl', 8)]]
print("=> FCM1", all(x==y for x,y in zip(result, g.rowCategories)))
print("=> FCM2", g.colCount is None)
print("=> FCM3", 12 == g.rowCount)
print("=> FCM4", 23 == g.getDataByIndex(rowIndex=0)["data"].shape[0])
try:
    5 == g.getDataByIndex(colIndex=0)["data"].shape[0]
    print("=> FCM5", False)
except IndexError:
    print("=> FCM5", True)
print("=> FCM6", mpg.shape[0] == g.getDataByIndex()["data"].shape[0])
print("=> FCM7", 21 == g.getDataByIndex(rowIndex=11)["data"].shape[0])
try:
    62 == g.getDataByIndex(rowIndex=12)["data"]
    print("=> FCM8", False)
except IndexError:
    print("=> FCM8", True)
print("=> FCM9", (12,1) == g.getShape())
