# Google Play Store Review Scraper

Folder ini berisi script dan notebook untuk melakukan scraping ulasan aplikasi dari Google Play Store menggunakan Playwright.

## File

### scrap_tiket_playstore.py
Script Python untuk:
- Membuka halaman aplikasi di Google Play Store.
- Mengklik tombol "See all reviews".
- Melakukan scrolling pada dialog ulasan untuk memuat lebih banyak review.
- Menyimpan hasil halaman HTML ke file `playstore_reviews2.html`.

### scrap.ipynb
Notebook Jupyter yang digunakan untuk eksperimen, pengembangan, atau analisis hasil scraping.

## Requirements

- Python 3.9+
- Playwright

Install dependency:

```bash
pip install playwright
playwright install
```
## Menjalankan Script

```bash
python scrap_tiket_playstore.py
```

Setelah proses selesai, file HTML hasil scraping akan tersimpan pada direktori yang sama.

## Catatan

* Script menggunakan browser Chromium melalui Playwright.
* Beberapa perubahan pada tampilan Google Play Store dapat menyebabkan selector perlu diperbarui.
* Proses scraping membutuhkan koneksi internet yang stabil.
