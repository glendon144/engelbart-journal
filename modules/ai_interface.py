
from modules.logger import EventLogger

class AIInterface:
    def __init__(self):
        self.logger = EventLogger("storage/event_log.db")

    def ask(self, prompt):
        self.logger.log("user", "ask", "AI", prompt)
        return f"AI response to: {prompt}"
