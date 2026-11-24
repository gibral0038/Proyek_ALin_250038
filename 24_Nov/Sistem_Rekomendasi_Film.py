import math

# 1. Menggunakan Data Film dengan 7 Genre Utama: [Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller]
data_film = {

}

# =====================================================================
# FUNGSI ALJABAR LINEAR MURNI (TANPA NUMPY)
# =====================================================================

def dot_product(v1, v2):
    """Menghitung perkalian titik: sum(u_i * v_i)"""
    return sum(a * b for a, b in zip(v1, v2))

def vector_norm(v):
    """Menghitung panjang/magnitudo vektor (L2-Norm): sqrt(sum(v_i^2))"""
    return math.sqrt(sum(a ** 2 for a in v))

def cosine_similarity(v1, v2):
    """Menghitung keselarasan sudut antara dua vektor"""
    norm1 = vector_norm(v1)
    norm2 = vector_norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product(v1, v2) / (norm1 * norm2)

# =====================================================================
# FUNGSI PENCARI REKOMENDASI
# =====================================================================

def cari_rekomendasi(judul_target, top_n=3):
    if judul_target not in data_film:
        print(f"Film '{judul_target}' tidak ditemukan dalam dataset.")
        return

    vektor_target = data_film[judul_target]
    hasil_perbandingan = []

    for judul_kandidat, vektor_kandidat in data_film.items():
        if judul_kandidat == judul_target:
            continue  # Lewati perbandingan dengan diri sendiri

    # Urutkan dari skor akhir tertinggi ke terendah
    hasil_perbandingan.sort(key=lambda item: item[1], reverse=True)