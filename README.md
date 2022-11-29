
# MPPL KELOMPOK 1

| Nama | NIM     | Role                |
| :-------- | :------- | :------------------------- |
| `Aldinur Syahdin Halim Simbolon` | `G64190003` | `Frontend` |
| `Alvina Maharani Hasibuan` | `G64190004` | `Backend` |
| `Annisa Dwi Quintho` | `G64190006` | `UI/UX` |
| `Daffa Muhammad Subhan` | `G64190013` | `Project Manager` |
| `Siti Magfiroh` | `G64190042` | `QA` |
| `Muhammad Alfarizhi` | `G64190087` | `Frontend` |

# Background
**Gaji** adalah suatu bentuk jasa yang diberikan secara teratur 
kepada seorang pegawai atas jasa dan hasil kerjanya. Masih banyak 
usahaan yang proses pengolahan data yang masih manual dengan menggunakan program bantu Ms.Excel sehingga menyebabkan terjadinya kesalahan perhitungan gaji karyawan, dan proses cetak slip gaji yang memakan waktu yang lama sehingga menghambat proses kinerja di perusahaan. 
Contohnya adalah sistem penggajian karyawan yang ada pada PT. Inti Mitra Bersama Jakarta.  Perusahaan ini masih menggunakan sistem manual yang kurang efektif, sehingga dapat menimbulkan kesalahan-kesalahan dalam pengelolaan gaji karyawan dan pembuatan laporan.

Sebagai sarana yang penting dalam perusahaan, sistem yang 
terkomputerisasi sangat berperan dalam meningkatkan produktivitas kerja. Untuk itu sistem informasi diciptakan agar berbagai macam proses manual dapat dikerjakan secara komputerisasi sehingga lebih efektif dan efisien. Dengan melihat kondisi diatas tim kami tertarik untuk membuat suatu perancangan sistem penggajian perusahaan yang terkomputerisasi dan datanya disimpan dalam suatu database yang mampu membantu permasalahan terutama pada penggajian karyawan, yang dilakukan oleh pihak HRD untuk melakukan pengelolaan data penggajian.

Adapun salah satu perusahaan yang sudah mulai menggunakan 
aplikasi untuk mempermudah pihak HR dalam mengelola data 
penggajian adalah Perusahaan Kisel Group dengan aplikasi Marissa. 
Aplikasi Marissa digunakan untuk karyawan dalam mengisi presensi 
kehadiran, jumlah waktu lembur, dan perizinan selama bekerja. 
Melalui data ini akan mempermudah HR dalam menentukan jumlah 
gaji yang diterima oleh karyawan.  Berdasarkan fitur yang tersedia 
pada aplikasi tersebut, kelompok kami memutuskan untuk menambahkan 
fitur baru berupa fitur ‘reimbursement’ agar mempermudah karyawan 
dalam proses pengembalian uang yang telah mereka bayarkan sebelumnya untuk kepentingan perusahaan. 


# Tujuan iMployee
**iMployee** adalah aplikasi berbasis web untuk mengelola proses 
penggajian pegawai perusahaan. Aplikasi ini memberikan kemudahan 
kepada karyawan untuk melakukan transaksi yang berhubungan dengan 
perusahaan dan memudahkan pihak perusahaan memberikan invoice gaji. 
Aplikasi ini dibuat menggunakan framework Laravel. Pengguna dari 
iMployee merupakan HR dan karyawan dalam sebuah perusahaan. 
HR dapat menggunakan aplikasi ini untuk melakukan cross-check 
terhadap data karyawan sehingga dapat di acc untuk pengiriman gaji. 
Sedangkan karyawan dapat menggunakan aplikasi ini untuk mengisi 
presensi, jumlah jam lembur, perizinan, dan jumlah reimbursement. 
Adapun fitur-fitur yang ada dalam aplikasi iMployee ini antara lain 
pengisian, presensi, reimbursement karyawan, perizinan, dan overtime

# Our Features 
### (for Employee)
- Presensi kehadiran
- *Reimbursement*
- Perizinan
- *Overtime*
- Menunjukkan gaji

### (for HR)
- Menambah *employee*
- Menerima atau menolak *request employee* 
- Mengirimkan gaji *employee*

# User Story
- Sebagai user, pegawai ingin melakukan perizinan secara mudah sehingga tidak perlu menemui dan menunggu orang terkait dalam melakukan perizinan
- Sebagai user, pegawai ingin melakukan presensi kehadiran secara mudah sehingga tidak perlu menunggu giliran untuk melakukan presensi
- Sebagai user, pegawai  ingin mengetahui total waktu lembur secara mudah sehingga bukti melakukan lembur terekam jejak
- Sebagai user, pegawai  ingin mengetahui jumlah gaji yang mereka peroleh sehingga mengetahui bahwa gaji sudah mereka dapatkan
- Sebagai user, pegawai  ingin mengajukan reimbursement secara mudah sehingga sesuai dengan tipe reimburse dan tidak terjadi multiple reimbursement
- Sebagai user, HR ingin menerima request pegawai yang terintegrasi sehingga hal-hal mulai dari perizinan, gaji, lembur, reimbursement, dapat di cek dengan mudah
- Sebagai user, HR ingin mengirimkan gaji ke pegawai dengan efektif sehingga pemberian slip gaji dapat langsung diterima oleh pegawai

# Scope
- Sistem tidak mencakup perizinan berupa cuti
- Sistem tidak menampilkan kontak semua pegawai perusahaan
- Sistem tidak menampilkan informasi mengenai asuransi
- Aplikasi berbasis web

# Kebutuhan Sistem
## User
Pengguna pada aplikasi ini adalah pegawai dan HR (Admin)
## Fitur utama
Pegawai bisa mengetahui total gaji yang mereka terima berdasarkan presensi kehadiran dan jam lembur yang dilakukan. 
## Lingkungan Pengembangan
### Perangkat keras dengan spesifikasi (`Backend`)
- `Processor AMD Athlon Gold 3150U with Radeon Graphics (4 CPUs), ~2.4GHz`
- `RAM 8 GB`
- `SSD 512 GB`

### Perangkat keras dengan spesifikasi (`Frontend`)
- `Prosesor Intel Core i3-6006U CPU @2.00GHz`
- `RAM 12 GB`
- `SSD 256 GB`

# Risiko
| High | Medium     | Low                |
| :-------- | :------- | :------------------------- |
| Projek tidak selesai tepat waktu | Error pada code | Terdapat masalah saat deploy |
| Projek menjadi lebih kompleks dari perkiraan | Terjadi miskomunikasi 

# Metodologi
 
![Logo](https://www.guru99.com/images/1/051719_0618_Prototyping1.png)
- **Requirements**: Sudah mendefinisikan kebutuhan sistem dan hal apa saja yang diinginkan oleh klien. Dalam hal ini  klien membutuhkan sistem penggajian pegawai lebih efisien dan praktis 
- **Quick design**: Tim kita membuat desain sistem yang mencakup semua kebutuhan klien. Rancangan desain yang dibangunberupa desain med-fi terkait gambaran besar  fitur sistem yang sudah dijelaskan seperti dashboard, reimbursement, kehadiran, dll
- **Build prototype**: Rancangan desain yang sudah dibangun tadi akan dikembangkan menjadi desain yang lebih rinci dan ditampilkan ke dalam bentuk hi-fi yang merupakan pengembangan dari desain med-fi dimana fitur fitur tersebut dibuat lebih detail
- **User evaluation**: Pada tahap ini akan direpresentasikan hasil prototype yang telah dibuat kepada klien untuk memastikan apakah sudah sesuai
- **Refining prototype**: Feedback dari klien akan menjadi pertimbangan kita untuk memperbaiki aplikasi iMployee dan kemudian dipresentasikan ulang kepada klien kita. Jika tidak ada kita akan lanjut ke dalam tahap terakhir
- **Implement and maintain**: Tahap ini akan dialihkan kepada tim engineering untuk membangun sistem sesuai dari prototype yang dibutuhkan. Front-End dan Back-End akan bekerja sama dalam membangun iMployee sehingga dilakukan testing aplikasi dan kemudian bisa di deploy

# Use Case Diagram
![Image](https://drive.google.com/uc?export=view&id=1PZlSAdldvpur3OgfDzIuxV15A6CD7Gwg)

# Activity Diagram 
![Image](https://drive.google.com/uc?export=view&id=161lzo-nUOn-ovqk2u8eqvx5gWtkVwV2x)

# ERD
![Image](https://drive.google.com/uc?export=view&id=1dydGLDq9O4x9mVEVmvmKocVAWYutkOyO)

# Link
- [Sheet Test Case](https://docs.google.com/spreadsheets/d/1ZpjJNU-vJX181iDHhJXaAiMMs_-hJv4GXdVn6OAvcaQ/edit#gid=0)
- [Demo](https://drive.google.com/drive/folders/1NL9SCwVu-N4iguzNb_BFTjoJcuImMiJF?usp=share_link)
- [Web App](https://docs.google.com/spreadsheets/d/1ZpjJNU-vJX181iDHhJXaAiMMs_-hJv4GXdVn6OAvcaQ/edit#gid=0)
- [Figma](https://www.figma.com/file/Vg4BQjRC3nC9TKfsbaLvE7/imployee?node-id=547%3A5672&t=R3qTyswuZLGupGem-1)

# Kendala
- Waktu
- Penggunaan framework 
- Terdapat kesulitan dalam mengintegrasikan sistem pada Frontend dan Backend
