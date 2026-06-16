import chromadb
import uuid
from datetime import datetime

# Initialize ChromaDB client (local persistent storage)
chroma_client = chromadb.PersistentClient(path="./memory_db")

# Use default embedding function (no sentence-transformers needed)
memory_collection = chroma_client.get_or_create_collection(
    name="apaaji_memories"
)

def save_memory(user_id: str, conversation: str):
    """Save a conversation summary to memory"""
    memory_collection.add(
        documents=[conversation],
        metadatas=[{
            "user_id": user_id,
            "timestamp": datetime.now().isoformat()
        }],
        ids=[str(uuid.uuid4())]
    )

def get_relevant_memories(user_id: str, current_message: str, n_results: int = 3) -> str:
    """Retrieve relevant past memories for a user"""
    try:
        results = memory_collection.query(
            query_texts=[current_message],
            n_results=n_results,
            where={"user_id": user_id}
        )
        if results and results["documents"] and results["documents"][0]:
            memories = results["documents"][0]
            return "\n".join([f"- {m}" for m in memories])
        return ""
    except Exception:
        return ""

def summarize_conversation(conversation_history: list) -> str:
    """Convert conversation history into a saveable memory string"""
    summary_parts = []
    for msg in conversation_history:
        role = "User" if msg["role"] == "user" else "Apaaji"
        summary_parts.append(f"{role}: {msg['content']}")
    return "\n".join(summary_parts)