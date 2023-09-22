#ใช้รวมข้อมูลต่างๆ
#ใช้ ,
print("Hello...",453,'Hi...',True,10+20,'Ola...')
#ใช้ + ต้องเป็น String ถ้าไม่ใช่ ให้คุมด้วย str() อยากให้เว้น ให้เว้นเอง ' ' แบบนี้ ไม่ก็เคาะ space ในข้อความเอา
print("Hello... "+str(453)+' Hi... '+str(True)+' '+str(10+20)+' Ola...')
# ใช้ method format ที่ไม่ใช่ str เขียนใน format ที่ไม่ใช่ str จะเอาไปไว้ในข้อความ str ให้ใส่ {} ตรงที่จะใส่
print("Hello... {} Hi... {} {} Ola...".format(456,True,10+20))
print("Hello... {2} Hi... {0} {1} Ola...".format(456,True,10+20)) #index number เริ่มจาก 0 สลับตำแหน่งได้
#ใช้ f-string ใส่ f ข้างหน้า str ใส่ในปีกกา
print(f"Hello... {456} Hi... {True} {10+20} Ola...")
#ใช้ modulas operater (%) -> %dจำนวนเต็ม, %f, %c, %sค่าTrueFalse,%iค่าTrueFalse แต่เป็น 1 กับ 0,%sใช้กับ str .....
print("Hello...%d Hi... %s %d Ola..." %(456,True,10+20) )