import json
import os
from datetime import datetime

MEMORY_FILE = "memory_store.json"

def _load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def save_memory(user_id: str, conversation: str):
    data = _load_memory()
    if user_id not in data:
        data[user_id] = []
    data[user_id].append({
        "conversation": conversation,
        "timestamp": datetime.now().isoformat()
    })
    # Keep only last 10 conversations per user
    data[user_id] = data[user_id][-10:]
    _save_memory(data)

def get_relevant_memories(user_id: str, current_message: str, n_results: int = 3) -> str:
    data = _load_memory()
    if user_id not in data or not data[user_id]:
        return ""
    # Return last few conversations
    recent = data[user_id][-n_results:]
    return "\n".join([f"- {m['conversation']}" for m in recent])

def summarize_conversation(conversation_history: list) -> str:
    summary_parts = []
    for msg in conversation_history:
        role = "User" if msg["role"] == "user" else "Apaaji"
        summary_parts.append(f"{role}: {msg['content']}")
    return "\n".join(summary_parts)