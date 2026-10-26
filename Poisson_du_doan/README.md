# Dự đoán EPL bằng Poisson Regression (bản đơn giản)

```
data/EPL.db          <- database (đặt vào đây)
src/config.py        <- đường dẫn + tham số (sửa tham số ở đây)
src/doc_du_lieu.py   <- Bước 1: đọc + làm sạch
src/tao_feature.py   <- Bước 2: tạo feature (xG/xGA 5 trận gần nhất, Elo)
src/mo_hinh.py       <- Bước 3: mô hình Poisson + xác suất thắng/hòa/thua
src/danh_gia.py      <- Bước 4: đánh giá (Log loss, Brier)
src/du_doan.py       <- Bước 5: dự đoán trận chưa đá -> outputs/predictions.csv
src/main.py          <- chạy tất cả các bước
```
