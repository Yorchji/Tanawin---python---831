unit_used = 350 #หน่วย
rate_per_unit = 4.5 #บาทต่อหน่วย
service_charge = 50 #บาท
#คำนวนค่าไฟฟ้า
electricity_cost = unit_used * rate_per_unit
#คำนวณรวมทั้งหมด
total = electricity_cost + service_charge
#เเสดงผล
print("Electricity Bill Calculator")
print("Unit used:{unit_used}")
print("Rate per unit:{rete_per_unit} THB")
print("Service charge:{service_charge} THB")
print("Total cost:{int(total)} THB")
print("Summary: used {unit_used} unit equals {int(total)} THB")