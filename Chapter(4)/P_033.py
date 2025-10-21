cars = ["audi", "kia"]

yourcar = input("차:")
if yourcar.lower().strip() in cars:
 print("있네 있어.") # kia나 audi가 있으면
else:
 print("가!") # 없으면