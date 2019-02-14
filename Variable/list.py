# variable type list
var_list = [ 'abcd', 123 , 1.23, 'Test Program', 20.2 ]
var_tinylist = [123, 'admin']
print (type(var_list))
print (var_list)          # แสดงค่าทั้งหมด var_list
print (var_list[0])       # แสดงแบบเจาะจงตำแหน่ง var_list[index]
print (var_list[:2])      # var_list[ไม่ระบุ:นับไปอีก] คือ ไม่ระบุเริ่มที่ 0 แสดงค่า 2 ตัว
print (var_list[1:3])     # var_list[index:นับไปอีก] แสดงเจาะจงตำแหน่งเริ่ม 1 แสดงค่า 3 ตัว
print (var_list[2:])      # var_list[index:ไม่ระบุ] แสดงเจาะจงตำแหน่งเริ่ม 2 ไปจนถึงตำแหน่งสุดท้าย
print (var_tinylist * 2)  # แสดงค่าทั้งหมด var_tinylist สองครั้ง สามารถคูณได้เลย
print (var_list + var_tinylist) # รวม var_list, var_tinylist ได้โดยการบวก

# เพิ่ม
var_list.append('Aphisit')
# แทรก
var_list.insert(1,'Khaithong')
print (var_list)
# ลบ
var_list.remove('Aphisit')
print (var_list)
# แก้ไข
var_list[1] = 'Aphisit Khaithong'
print (var_list)