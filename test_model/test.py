import csv

# Đường dẫn file
input_file = "/home/tien/Câu hỏi Trả lời Bệnh nhân.txt"
output_file = "decision_making_test.csv"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Câu hỏi", "Trả lời"])  # Ghi tiêu đề cột
    
    for line in f_in:
        line = line.strip()
        if not line:
            continue  # bỏ qua dòng trống
        
        # Chỉ tách ở dấu phẩy đầu tiên
        parts = line.split(",", 1)
        if len(parts) == 2:
            cau_hoi, tra_loi = parts
        else:
            cau_hoi, tra_loi = parts[0], ""
        
        writer.writerow([cau_hoi.strip(), tra_loi.strip()])

print(f"✅ Đã chuyển xong: {output_file}")
