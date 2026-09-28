# AttendX — Smart Attendance by AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
  <img src="https://img.shields.io/badge/AI-Face%20%2B%20Voice-8A2BE2?style=for-the-badge" alt="AI Face + Voice" />
</p>

> An AI-powered attendance system that helps teachers and students manage classroom attendance faster, smarter, and more securely using face recognition and voice recognition.

## ✨ Overview

AttendX is a modern Python + Streamlit application designed to make classroom attendance simpler, quicker, and more secure for both teachers and students.

### What AttendX provides

- 👨‍🏫 **Teacher dashboard** for managing classes, subjects, and attendance records
- 👨‍🎓 **Student portal** for joining classes and viewing attendance
- 📸 **Face-based attendance** using AI recognition
- 🎙️ **Voice-based attendance** using speech recognition
- 🔗 **Join codes** for quick student access and enrollment
- 🧑‍💻 **Enrollment workflow** with student photo and voice data
- 📊 **Attendance summaries** and result tracking
- 🔐 **Secure authentication** with password hashing
- ☁️ **Cloud-backed storage** with Supabase
- 📱 **QR code generation** for subject access sharing

---

## 🚀 Why this project stands out

AttendX brings together AI, automation, and education in one lightweight platform:

- Fast attendance marking without long manual roll calls
- Secure biometric-based recognition for better verification
- Easy onboarding for teachers and students
- Cloud-first architecture for smooth data management
- Scalable design for future academic features

---

## 🛠️ Tech Stack

| Area | Technology / Tool |
| --- | --- |
| Language | Python |
| Web app framework | Streamlit |
| Face recognition | `face_recognition_models`, `dlib-bin`, `scikit-learn` |
| Voice recognition | `librosa`, `resemblyzer` |
| Data processing | NumPy, Pandas |
| Database / backend | Supabase |
| Authentication | bcrypt |
| QR codes | Segno |
| Image processing | Pillow |
| Architecture | Modular Python components, screens, and AI pipelines |

---

## 📁 Project Structure

```text
.
├── app.py                    # Streamlit application entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── src/
    ├── Components/           # Reusable UI dialogs and components
    ├── Ui/                   # UI helpers and styling
    ├── database/             # Database integration
    ├── pipelines/            # Face and voice recognition pipelines
    └── screens/              # Teacher and student screens
```

---

## 🔄 How It Works

1. A teacher creates a subject or class.
2. Students join using a subject code or QR code.
3. Students enroll their required photo and voice data.
4. AttendX identifies students using AI-based face or voice recognition.
5. Attendance is stored and displayed for review.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sushantyadav0I3IT/ATTENDX-SMART-ATTENDENCE-BY-AI.git
cd ATTENDX-SMART-ATTENDENCE-BY-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

- Create a Supabase project.
- Add your Supabase credentials using environment variables or the project configuration method used by the database module.
- Keep secrets private and never commit them to GitHub.

### 5. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at the local Streamlit URL.

---

## 🔒 Security Notes

- Use environment variables for Supabase URLs, keys, and other secrets.
- Never commit passwords, API keys, or private credentials.
- Handle biometric data responsibly and only with proper consent.
- Keep access control in place for teacher and student roles.

---

## 🤝 Contributing

Contributions are welcome. To contribute:

- Fork the repository
- Create a feature branch
- Make your changes
- Test locally
- Open a pull request with a clear description

---

## 📄 License

No license has been specified yet. If you plan to share or distribute this project publicly, add a proper license file.

---

<p align="center">
  <strong>Built for smarter classrooms 💡</strong>
</p>
