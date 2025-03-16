SkinExpertSystem/
│
├── app.py                  # Main entry point
├── database.db             # Database SQLite
├── auth/                   
│   ├── authentication.py   # Logic login/logout
│   └── user_roles.py       # Role admin/user
│
├── config/
│   ├── db_config.py        # Konfigurasi database
│   └── session_state.py    # Inisialisasi session_state
│
├── models/
│   ├── database.py         # CRUD operations
│   ├── logic.py            # Forward Chaining + Weighted Symptoms
│   ├── rules.py            # Rules penyakit & gejala
│   └── history.py          # Riwayat diagnosa
│
├── pages/
│   ├── tabs/               
│   │   ├── manage_symptoms.py    
│   │   ├── manage_diseases.py    
│   │   ├── manage_skincare.py    
│   │   └── history.py      # Tab riwayat diagnosa
│   │
│   ├── home.py             # Halaman diagnosa (user)
│   └── dashboard.py        # Dashboard admin
│
├── assets/                 # Folder gambar
│   ├── symptoms/           # Ilustrasi gejala
│   ├── diseases/           # Gambar penyakit
│   └── skincare/           # Foto produk skincare
│
├── utils/
│   ├── styles.py           # CSS custom (tema dokter)
│   └── helpers.py          # Fungsi validasi/bantu
│
└── README.md               # Panduan instalasi