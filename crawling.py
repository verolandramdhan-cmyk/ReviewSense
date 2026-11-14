from google_play_scraper import reviews, Sort
import pandas as pd
import os
import time

# ID aplikasi Tokopedia di Google Play Store
APP_ID = "com.tokopedia.tkpd"

def crawling_data(jumlah_data=1000):

    print("================================")
    print("   REVIEWSENSE AI - CRAWLING")
    print("================================")

    semua_ulasan = []
    token = None

    while len(semua_ulasan) < jumlah_data:

        try:
            hasil, token = reviews(
                APP_ID,
                lang="id",
                country="id",
                sort=Sort.NEWEST,
                count=min(200, jumlah_data - len(semua_ulasan)),
                continuation_token=token
            )

            if not hasil:
                break

            semua_ulasan.extend(hasil)

            print("Data terkumpul:", len(semua_ulasan))

            if token is None:
                break

            time.sleep(1)

        except Exception as e:
            print("Terjadi error:", e)
            break

    if not semua_ulasan:
        print("Crawling gagal atau tidak menghasilkan data.")
        return

    # Mengubah hasil crawling menjadi tabel
    df = pd.DataFrame(semua_ulasan)

    # Mengambil kolom yang diperlukan
    df = df[["content", "score", "at"]]

    # Mengubah nama kolom
    df.columns = ["ulasan", "rating", "tanggal"]

    # Menghapus data kosong dan duplikat
    df.dropna(subset=["ulasan"], inplace=True)
    df.drop_duplicates(subset=["ulasan"], inplace=True)

    # Membuat folder dataset jika belum tersedia
    os.makedirs("dataset", exist_ok=True)

    # Menyimpan hasil crawling
    df.to_csv(
        "dataset/reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\nCrawling berhasil!")
    print("Jumlah ulasan:", len(df))
    print("\nContoh dataset:")
    print(df.head())

if __name__ == "__main__":
    crawling_data(1000)