# คล้ายกับ array ใน PHP คือมี key กับ value คู่กัน
var_dict = {}
var_dict['one'] = "This is one"
var_dict[2]     = "This is two"

var_tinydict = {'one': 'This is one ของ var_tinydict', 2:'This is two ของ var_tinydict', 'dept': 'sales'}

print (var_dict)            # แสดงค่าทั้งหมดของ var_dict
print (var_dict['one'])     # แสดงเฉพาะ key "one" ของ ตัวแปร var_dict
print (var_dict[2])         # แสดงเฉพาะ key "2" ของ ตัวแปร var_dict
print (var_dict.keys())     # แสดง key ทั้งหมดของ ตัวแปร var_dict
print (var_dict.values())   # แสดง values ทั้งหมดของ var_dict

print ('---------------------------')

print (var_tinydict)            # แสดงค่าทั้งหมดของ var_dict
print (var_tinydict['one'])     # แสดงเฉพาะ key "one" ของ ตัวแปร var_dict
print (var_tinydict[2])         # แสดงเฉพาะ key "2" ของ ตัวแปร var_dict
print (var_tinydict.keys())     # แสดง key ทั้งหมดของ ตัวแปร var_dict
print (var_tinydict.values())   # แสดง values ทั้งหมดของ var_dict 