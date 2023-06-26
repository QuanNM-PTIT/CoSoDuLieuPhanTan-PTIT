from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, NVARCHAR
from sqlalchemy.orm import relationship

from database import Base


class Employee(Base):
    __tablename__ = "NhanVien"

    MaNV = Column(NVARCHAR(1000), primary_key=True)
    TenNV = Column(NVARCHAR(1000))
    GioiTinh = Column(NVARCHAR(1000))
    SDT = Column(NVARCHAR(1000))
    NamSinh = Column(NVARCHAR(1000))
    ChucVu = Column(NVARCHAR(1000))
    MaCN = Column(NVARCHAR(1000))

    rowguid = Column(String(1000))


class GiaoDich(Base):
    __tablename__ = "GiaoDich"

    MaGD = Column(NVARCHAR(1000), primary_key=True)
    MaNV = Column(NVARCHAR(1000))
    MaKH = Column(NVARCHAR(1000))
    MaSP = Column(NVARCHAR(1000))
    SoLuong = Column(NVARCHAR(1000))

    rowguid = Column(String(1000))
