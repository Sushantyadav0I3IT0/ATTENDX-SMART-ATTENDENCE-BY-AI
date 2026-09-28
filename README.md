# AttendX — Smart Attendance by AI

> An AI-powered attendance system that helps teachers and students manage attendance quickly using **face recognition** and **voice recognition**.

## ✨ Overview

AttendX is a Python and Streamlit application designed to make classroom attendance faster, simpler, and more secure.

### What it provides

- 👨‍🏫 **Teacher dashboard** for managing classes and subjects
- 👨‍🎓 **Student experience** for joining subjects and viewing attendance
- 📸 **Face-based attendance** using face recognition
- 🎙️ **Voice-based attendance** using voice recognition
- 🔗 **Join codes** for quick student enrollment
- 🧑‍💻 **Student enrollment** with photo and voice data
- 📊 **Attendance results** for reviewing attendance records
- 🔐 **Secure authentication** with password hashing
- 🗄️ **Cloud data storage** with Supabase
- 📱 **QR code generation** for sharing subject access

## 🛠️ Main Tech Stack

| Area | Technology / Tool |
| --- | --- |
| **Language** | Python |
| **Web app framework** | Streamlit |
| **Face recognition** | `face_recognition_models`, `dlib-bin`, `scikit-learn` |
| **Voice recognition** | `librosa`, `resemblyzer` |
| **Data processing** | NumPy, Pandas |
| **Database / backend** | Supabase |
| **Authentication** | bcrypt |
| **QR codes** | Segno |
| **Image processing** | Pillow |
| **Project structure** | Modular Python components, screens, and pipelines |

## 📁 Project Structure

```text
.
├── app.py                    # Streamlit application entry point
├── requirements.txt          # Python dependencies
└── src/
    ├── Components/           # Reusable UI dialogs and components
    ├── Ui/                   # UI helpers and styling
    ├── database/             # Database integration
    ├── pipelines/            # Face and voice recognition pipelines
    └── screens/              # Home, teacher, and student screens
```

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
venv\\Scripts\\activate
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
- Add the required Supabase configuration to the project using environment variables or the configuration method used by the database module.
- Keep credentials private and do not commit secrets to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit URL.

## 🔄 How It Works

1. A teacher creates a subject or class.
2. Students join using a subject code or QR code.
3. Students enroll their required photo and voice information.
4. AttendX uses AI pipelines to identify students through their face or voice.
5. Attendance results are stored and displayed for review.

## 🔒 Security Notes

- Use environment variables for Supabase URLs, keys, and other secrets.
- Never commit passwords, API keys, or private credentials.
- Use this system only with appropriate user consent for biometric data collection.

## 🤝 Contributing

Contributions are welcome. To contribute:

- Fork the repository.
- Create a feature branch.
- Make your changes.
- Test the application locally.
- Open a pull request with a clear description.

## 📄 License

No license has been specified yet. Add a license file if you plan to distribute or accept external contributions.
