# 🏢 Dreamhome Riverside - Financial Analysis

Phân tích tài chính chi tiết và đề xuất tái cấu trúc dự án Dreamhome Riverside với 3 kịch bản.

## 📊 Tổng quan

Dự án bao gồm:
- **3 Kịch bản tái cấu trúc** (Conservative, Balanced, Aggressive)
- **Sensitivity Analysis** chi tiết với ma trận 2 chiều
- **Risk Mitigation Plan** với biện pháp phòng ngừa cụ thể
- **Financial Model** Excel đầy đủ

## 🚀 Hướng dẫn Deploy lên GitHub Pages

### Bước 1: Clone repository

```bash
git clone https://github.com/Khogao/DreamhomeProjects.git
cd DreamhomeProjects
```

### Bước 2: Copy files vào repository

Copy tất cả các files sau vào thư mục repository:
- `index.html` (Landing page)
- `scenario1_conservative.html`
- `scenario2_balanced.html`
- `scenario3_aggressive.html`
- `sensitivity_analysis.html`
- `risk_mitigation_plan.html`
- `dreamhome_riverside_analysis.xlsx`
- `README.md` (file này)

### Bước 3: Push lên GitHub

```bash
git add .
git commit -m "Add Dreamhome Riverside financial analysis"
git push origin main
```

**Lưu ý:** Nếu branch chính là `master` thay vì `main`, dùng lệnh:
```bash
git push origin master
```

### Bước 4: Enable GitHub Pages

1. Vào repository trên GitHub: https://github.com/Khogao/DreamhomeProjects
2. Click vào **Settings** (⚙️ icon)
3. Scroll xuống phần **Pages** ở sidebar bên trái
4. Trong phần **Source**, chọn:
   - Branch: `main` (hoặc `master`)
   - Folder: `/ (root)`
5. Click **Save**
6. Đợi 1-2 phút, GitHub sẽ build và deploy
7. URL sẽ là: **https://khogao.github.io/DreamhomeProjects/**

### Bước 5: Truy cập website

Sau khi deploy xong, anh có thể truy cập các pages:

- **Landing Page (Tổng quan):** https://khogao.github.io/DreamhomeProjects/
- **Kịch bản 1:** https://khogao.github.io/DreamhomeProjects/scenario1_conservative.html
- **Kịch bản 2 (Recommended):** https://khogao.github.io/DreamhomeProjects/scenario2_balanced.html
- **Kịch bản 3:** https://khogao.github.io/DreamhomeProjects/scenario3_aggressive.html
- **Sensitivity Analysis:** https://khogao.github.io/DreamhomeProjects/sensitivity_analysis.html
- **Risk Mitigation Plan:** https://khogao.github.io/DreamhomeProjects/risk_mitigation_plan.html
- **Excel File:** https://khogao.github.io/DreamhomeProjects/dreamhome_riverside_analysis.xlsx

## 📁 Cấu trúc Files

```
DreamhomeProjects/
├── index.html                          # Landing page - Tổng quan 3 kịch bản
├── scenario1_conservative.html         # Kịch bản 1: Conservative (NPV -96 tỷ)
├── scenario2_balanced.html             # Kịch bản 2: Balanced ✅ (NPV +305 tỷ)
├── scenario3_aggressive.html           # Kịch bản 3: Aggressive (NPV +164 tỷ)
├── sensitivity_analysis.html           # Phân tích độ nhạy chi tiết
├── risk_mitigation_plan.html           # Kế hoạch phòng ngừa rủi ro
├── dreamhome_riverside_analysis.xlsx   # Excel financial model
└── README.md                           # File này
```

## 💡 Nội dung Phân tích

### 🎯 3 Kịch bản Tái cấu trúc

| Kịch bản | NPV @ 12% | IRR | Vốn cần | Timeline | Rủi ro | Khuyến nghị |
|----------|-----------|-----|---------|----------|--------|-------------|
| **KB1: Conservative** | **-96 tỷ** | N/A | 280 tỷ | 30 tháng | Thấp | ❌ Không khả thi |
| **KB2: Balanced** | **+305 tỷ** | 22.3% | 440 tỷ | 24 tháng | Trung bình | ✅ **RECOMMENDED** |
| **KB3: Aggressive** | **+164 tỷ** | 29.4% | 400 tỷ + vay 500 | 21 tháng | Cao | ⚠️ High-risk |

### 📈 Key Findings

- **Kịch bản 2 (Balanced)** là lựa chọn tối ưu:
  - NPV cao nhất (+305 tỷ)
  - Downside protection tốt (worst case vẫn +43 tỷ)
  - ROE 88% trong 2 năm
  - Xác suất thành công >70%

- **Kịch bản 1** không khả thi do NPV âm
- **Kịch bản 3** có IRR cao nhất (29.4%) nhưng rủi ro lớn (worst case -220 tỷ)

### 🛡️ Risk Management

Top 5 rủi ro chính:
1. Giá bán không đạt kỳ vọng (35-50%)
2. Thanh lý HĐ gặp khó khăn pháp lý (40-60%)
3. Chi phí hoàn thiện vượt dự toán (50-70%)
4. Timeline chậm trễ (40-60%)
5. Tốc độ tiêu thụ thấp (30-50%)

Tổng budget dự phòng: **720 tỷ**

## 🔄 Cập nhật Content

Để cập nhật nội dung sau khi đã deploy:

1. Chỉnh sửa files HTML trong thư mục local
2. Commit và push changes:
```bash
git add .
git commit -m "Update analysis content"
git push origin main
```
3. GitHub Pages sẽ tự động rebuild và deploy trong 1-2 phút

## 📧 Liên hệ

Phân tích bởi **Charlie - Chuyên gia Tái cấu trúc Dự án**  
Ngày: October 24, 2025  
Dự án: Dreamhome Riverside

---

## 🛠️ Troubleshooting

### Lỗi "404 Not Found" sau khi enable Pages

- Đợi thêm 2-3 phút để GitHub build
- Kiểm tra branch và folder settings trong GitHub Pages
- Đảm bảo file `index.html` có trong root folder

### HTML hiển thị code thay vì render

- Đảm bảo extension là `.html` không phải `.txt`
- Xóa cache browser và refresh (Ctrl + Shift + R)

### Excel file không download được

- GitHub Pages có thể chặn một số file types
- Alternative: Upload lên Google Drive và share link

### Links giữa các pages bị broken

- Đảm bảo tất cả links dùng relative paths (ví dụ: `scenario1_conservative.html`)
- KHÔNG dùng absolute paths (ví dụ: `/scenario1_conservative.html`)

---

**🎉 Chúc anh deploy thành công!** Nếu có vấn đề gì, hãy cho tôi biết.
