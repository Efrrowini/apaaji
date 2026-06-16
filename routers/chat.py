from fastapi import APIRouter
from pydantic import BaseModel
from services.claude_service import get_apaaji_response
from services.memory_service import save_memory, get_relevant_memories, summarize_conversation
from services.alert_service import send_family_alert, detect_alert_type

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_history: list = []

class ChatResponse(BaseModel):
    reply: str
    updated_history: list
    alert_sent: bool = False

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Fetch relevant memories for this user
    memory_context = get_relevant_memories(request.user_id, request.message)

    # Add new user message to history
    history = request.conversation_history + [
        {"role": "user", "content": request.message}
    ]

    # Get Apaaji response with memory context
    reply = get_apaaji_response(history, memory_context)

    # Append assistant reply to history
    updated_history = history + [
        {"role": "assistant", "content": reply}
    ]

    # Save this conversation to memory
    conversation_summary = summarize_conversation(updated_history)
    save_memory(request.user_id, conversation_summary)

    # Detect if family alert needed
    alert_type, alert_detail = detect_alert_type(request.message, reply)
    alert_sent = False
    if alert_type:
        alert_sent = send_family_alert(alert_type, alert_detail)

    return ChatResponse(
        reply=reply,
        updated_history=updated_history,
        alert_sent=alert_sent
    )