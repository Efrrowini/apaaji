# 🙏 Apaaji — Voice-First AI Companion for Elderly Indians

> "Aapka apna saathi — always here for you"

**Samsung Solve for Tomorrow 2026 | AI Living for India**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-apaaji.onrender.com-764ba2)](https://apaaji.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)](https://fastapi.tiangolo.com)

---

## 🧓 The Problem

India has **140M+ citizens aged 60+**. Many live alone as nuclear families and urban migration separate them from their children. They face:

- 🔇 Loneliness and isolation
- 💊 Missed medications and forgotten appointments
- 📵 Digital exclusion — most can't type or navigate apps
- 😟 No affordable, accessible companionship solution

Existing technology assumes digital literacy they simply don't have.

---

## 💡 The Solution

**Apaaji** is a voice-first AI companion that elderly Indians can simply *talk to* — no typing, no apps to learn.

- 🗣️ **Just speak** — voice input in Hindi/Hinglish
- 🧠 **Remembers** past conversations ("How did Rahul's exams go?")
- 💊 **Medication reminders** via voice alerts
- 📱 **WhatsApp alerts** to family when something seems wrong
- 📞 Works on **any existing Android smartphone** — zero new hardware

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎤 Voice Input | Speak naturally in Hindi or Hinglish |
| 🧠 Memory | Remembers past conversations across sessions |
| 💬 Hinglish Responses | Warm, natural, never robotic |
| 💊 Medication Detection | Auto-detects medicine mentions |
| 📱 WhatsApp Alerts | Notifies family members instantly |
| 🌐 Any Device | Works on any smartphone browser |

---

## 🏗️ Tech Stack
| Layer | Technology |
|---|---|
| Backend | FastAPI + Uvicorn |
| AI Model | Llama 3.3 70B via Groq API |
| Memory | JSON-based persistent storage |
| Alerts | Twilio WhatsApp Business API |
| Frontend | Vanilla HTML/CSS/JS + Web Speech API |
| Deployment | Render (Free tier) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Groq API key (free at console.groq.com)
- Twilio account (free trial)

### Installation

```bash
git clone https://github.com/Efrrowini/apaaji.git
cd apaaji
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file:
```env
GROQ_API_KEY=your_groq_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
FAMILY_WHATSAPP_NUMBER=whatsapp:+your_number
```

### Run

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000` 🙏

---

## 📱 Demo

🌐 **Live:** https://apaaji.onrender.com

### Sample Conversation

> **User:** Aaj mera dil nahi lag raha kuch karne mein
>
> **Apaaji:** Arey, koi baat nahi ji. Kabhi kabhi aisa hota hai. Aapko kuch khaas pareshan kar raha hai, ya bas aaj ka din thoda off lag raha hai? Main sun raha hoon... 🙏

---

## 🎯 Impact

- **140M+** elderly Indians who could benefit
- **Zero** new hardware required
- **Free** to use on any smartphone
- **Scalable** to regional languages (Hindi, Tamil, Telugu, Bengali)

---

## 👨‍💻 Built By

**Efrrowini** — 2nd Year BTech CSE, Presidency University Bangalore

Samsung Solve for Tomorrow 2026 | Solo Submission

[![GitHub](https://img.shields.io/badge/GitHub-Efrrowini-black)](https://github.com/Efrrowini)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-efrrowini-blue)](https://linkedin.com/in/efrrowini)
