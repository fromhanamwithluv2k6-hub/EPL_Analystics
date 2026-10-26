
from config import OUTPUT_DIR
from doc_du_lieu import load_clean_data
from tao_feature import build_features
from danh_gia import evaluate
from du_doan import predict_future

print("===== BƯỚC 1: Đọc và làm sạch dữ liệu =====")
df = load_clean_data()
print("Tổng số trận:", len(df), "| đã đá:", (df["is_result"] == 1).sum())

print("\n===== BƯỚC 2: Tạo feature =====")
played, future = build_features(df)
print("Trận để học:", len(played), "| trận cần dự đoán:", len(future))

print("\n===== BƯỚC 3-4: Huấn luyện và đánh giá =====")
evaluate(played)

print("\n===== BƯỚC 5: Dự đoán các trận chưa đá =====")
result = predict_future(played, future)
result.to_csv(OUTPUT_DIR / "predictions.csv", index=False)
print("Đã lưu outputs/predictions.csv (%d trận). Trận kế tiếp:" % len(result))
print(result.head(1).to_string(index=False))
