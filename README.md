### Information
Cài đặt các thư viện trong `requirements.txt`
```bash
pip install -r requirements.txt
```
Folder `data` được tổ chức như sau:  
```
data
    ├───raw/
    ├───V1/
    ├───V2/
    └───...
```
Tương ứng với folder `process_data`:
```
process_data
    ├───V1.*    (xử lí từ "data/raw/" --> "data/V1/")
    ├───V2.*    (xử lí từ "data/V1/ --> "data/V2/")
    └───...
```