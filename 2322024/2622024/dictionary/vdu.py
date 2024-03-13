tu_dien = {"ten":"Nhi","tuoi":"21","can_nang":"41"}
#câu 1
print(tu_dien["ten"])
#câu 2
print(tu_dien.get("tuoi"))
#câu 3
tu_dien.update({"so_thich":"makeup"})
#câu 4
tu_dien.pop("so_thich")
#câu 5
tu_dien["can_nang"] = "42"
#câu 6
tu_dien.pop("can_nang")
#câu 7 
tu_dien.clear()