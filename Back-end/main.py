from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import schemas
import models
from database import engine, get_db, connectDB
from sqlalchemy.orm import Session
import uuid
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/all_employee')
def get_all():
    # Lấy dữ liệu
    cursor = connectDB.cursor()
    cursor.execute("SELECT * FROM dbo.NhanVien")
    result = []
    for row in cursor.fetchall():
        maNV = row[0]
        count_cursor = connectDB.cursor()
        count_cursor.execute(f"SELECT COUNT(*) as SoGD FROM dbo.GiaoDich WHERE MaNV='{maNV}'")
        count_result = count_cursor.fetchone()
        data = {
            'MaNV': maNV,
            'TenNV': row[1],
            'GioiTinh': row[2],
            'SDT': row[3],
            'NamSinh': row[4],
            'ChucVu': row[5],
            'MaCN': row[6],
            'SoGD': count_result[0]
        }
        result.append(data)
        count_cursor.close()
    cursor.close()
    return json.dumps(result, ensure_ascii=False, indent=4)


@app.post('/add_employee')
def add_employee(request: schemas.Employee):
    try:
        cursor = connectDB.cursor()
        sql_query = u"INSERT INTO NhanVien (MaNV, TenNV, GioiTinh, SDT, NamSinh, ChucVu, MaCN) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_query, (
        request.MaNV, request.TenNV, request.GioiTinh, request.SDT, request.NamSinh, request.ChucVu, request.MaCN))
        cursor.commit()
        return cursor.messages[-1][-1]
    except:
        return 'Cập nhật thông tin không thành công: Mã nhân viên đã tồn tại!'


@app.delete('/delete_employee/{id}')
def delete_employee(id: str, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.MaNV == id).first()
    db.delete(employee)
    db.commit()
    return {"message": f"Đã xóa nhân viên có MaNV là {id}."}


@app.put('/update_employee/{id}')
def update_employee(id: str, request: schemas.Employee):
    try:
        cursor = connectDB.cursor()
        sql_query = u"UPDATE dbo.NhanVien SET MaNV=?, TenNV=?, GioiTinh=?, SDT=?, NamSinh=?, ChucVu=?, MaCN=? WHERE MaNV=?"
        cursor.execute(sql_query, (
        request.MaNV, request.TenNV, request.GioiTinh, request.SDT, request.NamSinh, request.ChucVu, request.MaCN, id))
        cursor.commit()
        return cursor.messages[-1][1]
    except:
        return 'Cập nhật thông tin không thành công: Mã nhân viên đã tồn tại!'



@app.get('/get_employee/{id}')
def get_employee(id: str, db: Session = Depends(get_db)):
    return db.query(models.Employee).filter(models.Employee.MaNV == id).first()


@app.get('/search_employee')
def search_employee(s: str, db: Session = Depends(get_db)):
    cursor = connectDB.cursor()
    query = f"SELECT * FROM dbo.NhanVien WHERE MaNV LIKE '%{s}%'"
    cursor.execute(query)
    result = []
    for row in cursor.fetchall():
        maNV = row[0]
        count_cursor = connectDB.cursor()
        count_cursor.execute(f"SELECT COUNT(*) as SoGD FROM dbo.GiaoDich WHERE MaNV='{maNV}'")
        count_result = count_cursor.fetchone()
        data = {
            'MaNV': maNV,
            'TenNV': row[1],
            'GioiTinh': row[2],
            'SDT': row[3],
            'NamSinh': row[4],
            'ChucVu': row[5],
            'MaCN': row[6],
            'SoGD': count_result[0]
        }
        result.append(data)
        count_cursor.close()
    cursor.close()
    return json.dumps(result, ensure_ascii=False, indent=4)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
