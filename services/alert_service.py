import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

twilio_client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

TWILIO_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
FAMILY_NUMBER = os.getenv("FAMILY_WHATSAPP_NUMBER")

def send_family_alert(alert_type: str, detail: str):
    """Send a WhatsApp alert to the family member"""
    try:
        if alert_type == "medication":
            message = f"🙏 Apaaji Alert\n\nAapke ghar mein koi medication reminder hai:\n\n💊 {detail}\n\nKripya unhe yaad dilayein."
        elif alert_type == "concern":
            message = f"🙏 Apaaji Alert\n\nAapke ghar mein koi thoda upset lag rahe hain:\n\n💬 \"{detail}\"\n\nUnse baat karein, woh aapko miss kar rahe hain."
        else:
            message = f"🙏 Apaaji Alert\n\n{detail}"

        twilio_client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=FAMILY_NUMBER
        )
        return True
    except Exception as e:
        print(f"Alert failed: {e}")
        return False

def detect_alert_type(message: str, reply: str) -> tuple:
    """Detect if a conversation needs a family alert"""
    message_lower = message.lower()
    reply_lower = reply.lower()

    # Medication keywords
    med_keywords = ["medicine", "dawai", "tablet", "capsule", "injection", 
                   "doctor", "hospital", "dawa", "pill", "syrup"]
    
    # Concern keywords  
    concern_keywords = ["akela", "lonely", "sad", "dukhi", "ro raha", 
                       "bahut dard", "tabiyat", "beemar", "help", "emergency"]

    for keyword in med_keywords:
        if keyword in message_lower:
            return ("medication", message)
    
    for keyword in concern_keywords:
        if keyword in message_lower or keyword in reply_lower:
            return ("concern", message)
    
    return (None, None)