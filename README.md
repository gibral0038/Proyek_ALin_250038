# SISTEM REKOMENDASI FILM

merupakan rancangan sistem rekomendasi film menggunakan konsep aljabar linear.

- `data_film` merupakan penyimpanan data film dalam bentuk vektor berdimensi tujuh untuk genre Action, Comedy, Drama, Horror, Romance, Sci-Fi, dan Thriller.
- `dot_product(v1, v2)` menghitung perkalian titik dua vektor.
- `vector_norm(v)` menghitung panjang atau norm suatu vektor dengan rumus akar jumlah kuadrat komponennya.
- `cosine_similarity(v1, v2)` menghitung tingkat kesamaan dua film berdasarkan sudut antar-vektor, serta mengembalikan `0.0` jika salah satu vektor memiliki panjang nol.
- `cari_rekomendasi(judul_target, top_n=3)` memeriksa ketersediaan judul target dan menyiapkan hasil perbandingan dengan film lain.

Implementasi saat ini belum berisi data pada `data_film`, perhitungan kandidat pada fungsi pencarian, pencetakan rekomendasi, dan pemanggilan program utama. Karena itu kode belum dapat menghasilkan daftar rekomendasi film yang lengkap.