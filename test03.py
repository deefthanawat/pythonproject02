#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังก์ชัน input() โดยสิ่งที่ป้อนทั้งหมดถือเป็น str
#ตัวแปร variable เป็น identafier มีหน้าที่เก็บข้อมูลในโปรแกรม ข้อมูบที่เก็บจะอยู่ใน RAM 
#identifier คือ ชื่อที่ dev. ตั้งขึ้นเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ อย่าเว้น อย่าขึ้นต้นด้วยตัวเลข เป็นภาษาอังกฤษ
std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ') #สิ่งที่ป้อนทั้งหมดเป็น str
print('---------------------------')
stdAge = 2023 - int(stdYearBorn) #ต้องแปลง String เป็น number -> int( )จน.เต็ม, float( )จน.จริง(จน.เต็มไม่ก็ทศนิยมก็ได้)
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge}")
print('--------------------------')
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name)
print("คุณเกิดปี",stdYearBorn,"อายุ",stdAge)
print('-----------------------------------')
print("ยินดีต้อนรับ "+str(std_id)+' ชื่อ '+str(std_name))
print("คุณเกิดปี "+str(stdYearBorn)+" อายุ "+str(stdAge))
print('-------------------------------------')
print("ยินดีต้อนรับ {} ชื่อ {}".format(std_id,std_name))
print("คุณเกิดปี {} อายุ {}".format(stdYearBorn,stdAge))
print('---------------------------------')
print("ยินดีต้อนรับ %s ชื่อ %s" %(std_id,std_name))
print("คุณเกิดปี %s อายุ %d" %(stdYearBorn,stdAge))