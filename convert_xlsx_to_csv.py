import pandas as pd
import os

# สร้าง folder csv ถ้ายังไม่มี
if not os.path.exists('_csv'):
    os.makedirs('_csv')

# อ่านไฟล์ Excel
excel_file = '_data/1234.xlsx'
df = pd.read_excel(excel_file)

# แปลงและบันทึกเป็น CSV
output_file = '_csv/1234.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"แปลงไฟล์สำเร็จ: {output_file}")