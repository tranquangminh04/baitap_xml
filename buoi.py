from lxml import etree

# Parse các file XML từ đường dẫn
try:
    tree_sinhvien = etree.parse('sv.xml')
    tree_quanly = etree.parse('quanlybanan.xml')
except etree.XMLSyntaxError as e:
    print(f"Error parsing XML: {e}")
    exit(1)

# Danh sách các truy vấn XPath cho sv.xml
xpaths_sinhvien = [
    "//student",
    "//student/name",
    "//student/id",
    "//student[id='SV01']/date",
    "//student/enrollment/course",
    "//student[1]",
    "//student[enrollment/course='Vatly203']/id",
    "//student[enrollment/course='Toan101']/name",
    "//student[enrollment/course='Vatly203']/name",
    "//student[id='SV01']/date",
    "//student[starts-with(date,'1997')]/name | //student[starts-with(date,'1997')]/date",
    "//student[substring(date,1,4) < '1998']/name",
    "count(//student)",
    "//student[not(enrollment)]",
    "//student[id='SV01']/name/following-sibling::date",
    "//student[id='SV02']/name/preceding-sibling::id",
    "//student[id='SV03']/enrollment/course",
    "//student[starts-with(name,'Trần')]",
    "substring-before(//student[id='SV01']/date,'-')"
]

# Danh sách các truy vấn XPath cho quanlybanan.xml
xpaths_quanly = [
    "//BAN",
    "//NHANVIEN",
    "//MON/TENMON",
    "//NHANVIEN[MANV='NV02']/TENV",
    "//NHANVIEN[MANV='NV03']/TENV | //NHANVIEN[MANV='NV03']/SDT",
    "//MON[GIA>50000]/TENMON",
    "//HOADON[SOHD='HD03']/SOBAN",
    "//MON[MAMON='M02']/TENMON",
    "//HOADON[SOHD='HD03']/NGAYLAP",
    "//HOADON[SOHD='HD01']//MAMON",
    "//HOADON[SOHD='HD01']//MAMON/text()",
    "//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV]/TENV",
    "count(//BAN)",
    "count(//HOADON[MANV='NV01'])",
    "//MON[MAMON=//HOADON[SOBAN='2']//MAMON]/TENMON",
    "//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV]",
    "//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]",
    "//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV]",
    "//MON[MAMON=//CTHD[MAMON=//MON/MAMON and number(SOLUONG)>1]/MAMON]/TENMON",
    "//BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN | //HOADON[SOHD='HD02']/NGAYLAP"
]

# Hàm in kết quả các truy vấn XPath, chỉ lấy nội dung text
def print_xpath_results(tree, xpaths, xml_name):
    print(f"\n=== Kết quả cho {xml_name} ===")
    for i, xpath in enumerate(xpaths, 1):
        try:
            result = tree.xpath(xpath)
            print(f"\nCâu {i}")
            if isinstance(result, list):
                if not result:
                    print("Không có kết quả")
                for item in result:
                    if isinstance(item, etree._Element):
                        print(item.text.strip() if item.text else "Không có nội dung text")
                    else:
                        print(item)
            else:
                print(result)
        except etree.XPathEvalError as e:
            print(f"Lỗi khi thực thi XPath: {e}")

# Thực thi và in kết quả cho sv.xml
print_xpath_results(tree_sinhvien, xpaths_sinhvien, "sv.xml")

# Thực thi và in kết quả cho quanlybanan.xml
print_xpath_results(tree_quanly, xpaths_quanly, "quanlybanan.xml")