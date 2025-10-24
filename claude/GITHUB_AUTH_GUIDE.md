# 🔐 Hướng dẫn Authentication với GitHub

## Phương pháp 1: HTTPS với Personal Access Token (Đơn giản nhất - KHUYẾN NGHỊ)

### Bước 1: Tạo Personal Access Token

1. Đăng nhập GitHub: https://github.com
2. Click vào Avatar (góc phải trên) → **Settings**
3. Scroll xuống dưới cùng sidebar → Click **Developer settings**
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Điền thông tin:
   - **Note:** "DreamhomeProjects Deployment" (hoặc tên gì đó dễ nhớ)
   - **Expiration:** 90 days (hoặc No expiration nếu muốn)
   - **Select scopes:** Tick vào `repo` (đủ rồi)
7. Click **Generate token** ở cuối trang
8. **QUAN TRỌNG:** Copy token ngay (chỉ hiện 1 lần duy nhất!)
   - Token có dạng: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Bước 2: Clone repository với Token

```bash
git clone https://github.com/Khogao/DreamhomeProjects.git
cd DreamhomeProjects
```

**Lưu ý:** Khi clone lần đầu có thể không cần authentication.

### Bước 3: Copy files vào repository

```bash
# Giả sử files đang ở /mnt/user-data/outputs/
cp /mnt/user-data/outputs/*.html .
cp /mnt/user-data/outputs/*.xlsx .
cp /mnt/user-data/outputs/README.md .
```

### Bước 4: Push với Token

```bash
git add .
git commit -m "Add Dreamhome Riverside financial analysis"
git push origin main
```

**Khi được hỏi username và password:**
- Username: `Khogao` (GitHub username của bạn)
- Password: Paste **TOKEN** vừa copy (KHÔNG phải password GitHub)

### Bước 5: Lưu credentials (để không phải nhập lại)

```bash
git config --global credential.helper store
```

Lần sau push sẽ không cần nhập lại.

---

## Phương pháp 2: SSH Keys (Bảo mật hơn nhưng phức tạp hơn)

### Bước 1: Tạo SSH key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Nhấn Enter 3 lần (không cần passphrase)
```

### Bước 2: Copy public key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy toàn bộ output (bắt đầu với `ssh-ed25519 ...`)

### Bước 3: Add SSH key vào GitHub

1. Vào https://github.com/settings/keys
2. Click **New SSH key**
3. Title: "DreamhomeProjects Server"
4. Key: Paste public key vừa copy
5. Click **Add SSH key**

### Bước 4: Clone với SSH

```bash
git clone git@github.com:Khogao/DreamhomeProjects.git
cd DreamhomeProjects
```

### Bước 5: Push (không cần username/password)

```bash
git add .
git commit -m "Add analysis"
git push origin main
```

---

## 🚀 Quick Start (Nếu đã setup authentication)

```bash
# 1. Clone repo
git clone https://github.com/Khogao/DreamhomeProjects.git
cd DreamhomeProjects

# 2. Copy files
cp /mnt/user-data/outputs/*.html .
cp /mnt/user-data/outputs/*.xlsx .
cp /mnt/user-data/outputs/README.md .

# 3. Commit và push
git add .
git commit -m "Add Dreamhome Riverside financial analysis"
git push origin main

# 4. Enable GitHub Pages (làm trên web)
# Settings → Pages → Source: main branch, / (root) → Save
```

---

## ⚠️ Troubleshooting

### "Authentication failed"
→ Đảm bảo dùng **Personal Access Token** chứ KHÔNG phải password GitHub

### "Permission denied (publickey)"
→ SSH key chưa được add vào GitHub hoặc setup sai

### "fatal: could not read Password"
→ Dùng lệnh:
```bash
git config --global credential.helper store
```
Rồi push lại và nhập token 1 lần

### Quên token rồi
→ Tạo token mới theo Bước 1 ở trên

---

## 📝 Notes

- **KHUYẾN NGHỊ:** Dùng phương pháp 1 (HTTPS + Token) vì đơn giản nhất
- Token nên set expiration 90 days và renew định kỳ
- Không share token với ai
- Nếu token bị lộ, vào GitHub revoke ngay

---

**Nếu anh đã sẵn sàng cung cấp authentication, có thể:**
1. Tạo Personal Access Token theo hướng dẫn trên
2. Share token với tôi (trong chat này - an toàn)
3. Tôi sẽ push files lên GitHub giúp anh luôn

Hoặc anh tự làm theo hướng dẫn trên cũng được! 👍
