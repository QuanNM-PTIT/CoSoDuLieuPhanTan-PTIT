from pydantic import BaseModel

class Employee(BaseModel):
    MaNV: str
    TenNV: str
    GioiTinh: str
    SDT: str
    NamSinh: str
    ChucVu: str
    MaCN: str


class ShowEmployee(BaseModel):
    MaNV: str
    TenNV: str
    GioiTinh: str
    SDT: str
    NamSinh: str
    ChucVu: str
    MaCN: str
    SoGD: str

    class Config:
        orm_mode = True