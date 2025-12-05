import pandas as pd
import os

# สร้างข้อมูล employee
employees = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John Smith', 'Sarah Johnson', 'Mike Brown', 'Emily Davis', 'David Wilson'],
    'Department': ['IT', 'HR', 'Sales', 'IT', 'Finance'],
    'Position': ['Developer', 'Manager', 'Sales Rep', 'System Admin', 'Accountant'],
    'Salary': [50000, 60000, 45000, 55000, 52000]
}

# สร้าง DataFrame
df = pd.DataFrame(employees)

# สร้างโฟลเดอร์ _data ถ้ายังไม่มี
os.makedirs('_data', exist_ok=True)

# บันทึกลงไฟล์ Excel
df.to_excel('_data/1234.xlsx', index=False)

print("บันทึกข้อมูลสำเร็จ!")
print(f"\nข้อมูล Employee:\n{df}")