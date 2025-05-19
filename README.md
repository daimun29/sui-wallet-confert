Berikut adalah skrip  untuk mengubah private key mentah (hex) dari file `wallet.txt` menjadi format Bech32 (`suiprivkey...`) dan menyimpan hasilnya ke `hasil.txt`.

---

### ✅ **Syarat**:

1. Semua private key di `wallet.txt` harus berformat **hex 64 karakter** (32-byte)
2. Menggunakan skema **Ed25519** (seperti di Sui)

---

### 💻 **Script Python: `convert_wallet.py`**


### 📦 **Cara Pakai**:

1. Install library `bech32` (sekali saja):

   ```bash
   pip install bech32
   ```

2. Simpan semua private key hex ke `wallet.txt` (satu per baris), contoh:

   ```
   fc5d86f2afaf7bc58a5a85f54303bc2a719aaad0ea0f86d21016c9db6ca36f8s
   410933b6f6093f61d0de1fce5648d8c672501ee5813b44bb25d17cda46f549a0
   ```

3. Jalankan:

   ```bash
   python convert_wallet.py
   ```

4. Hasil akan tersimpan di `hasil.txt`

---

Aman dijalankan **sepenuhnya offline** dan tidak mengirimkan data ke mana pun.

Perlu versi tanpa dependensi luar (tanpa `bech32`)?
# sui-wallet-confert
