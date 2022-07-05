car = {"brand": "ford",
    "model": "Mustang",
    "year": 1964
}
print(car["brand"])
print(car)
x = car.keys()
print(x)
#เพิ่มค่าใน dic
car["color"] = "white"
print(car)
#แก้ค่าใน dic
car["color"] = "red"
print(car)
#การupdate dic
car.update({"light": "blue"})
print(car)
#การลบค่าใน dic
car.pop("light")
print(car)
del car["color"]
print(car)
#เพิ่มค่าใน dic แบบ list
car.update({"part": ["body","wheel","light"]})
print(car)
#เพิ่มค่าdicแบบ  Nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child3']['name'])




