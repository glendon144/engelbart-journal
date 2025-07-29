import sys 
from modules.document_store import DocumentStore 
from modules.event_logger import EventLogger

class CommandProcessor: 
    def init(self, store: DocumentStore, logger: EventLogger = None): 
        self.store = store self.logger = logger or EventLogger() self.commands = { 'help': self.help, 'list': self.list_docs, 'show': self.show_doc, 'ask': self.ask, 'exit': self.exit, }

def run(self):
    print("DemoKit CLI Ready. Type 'help' for a list of commands.")
    while True:
        try:
            command = input(" >> ").strip()
            if not command:
                continue
            self.execute_command(command)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

def execute_command(self, command):
    cmd_parts = command.split(None, 1)
    cmd = cmd_parts[0].lower()
    args = cmd_parts[1] if len(cmd_parts) > 1 else ''

    if cmd in self.commands:
        self.commands[cmd](args)
    else:
        print(f"Unknown command: {cmd}. Type 'help' for available commands.")

def help(self, args=None):
    print("Available commands:")
    print("  help              Show this help message")
    print("  list              List document IDs")
    print("  show <id>         Display document by ID")
    print("  ask <question>    Ask a question (AI reply will be stored)")
    print("  exit              Exit the program")

def list_docs(self, args=None):
    docs = self.store.list_documents()
    for doc_id, preview in docs:
        print(f"[{doc_id}] {preview[:60].replace('\n', ' ')}")

def show_doc(self, args):
    if not args:
        print("Usage: show <doc_id>")
        return
    try:
        doc_id = int(args.strip())
        doc = self.store.get_document(doc_id)
        print(f"\n--- Document {doc_id} ---\n{doc}\n------------------------\n")
    except Exception as e:
        print(f"Error: {e}")

def ask(self, args):
    if not args:
        print("Usage: ask <question>")
        return
    from .ai import query_ai  # Lazy import to prevent startup delay
    prompt = args.strip()
    response = query_ai(prompt)
    doc_id = self.store.create_document(response)
    print(f"AI reply stored as document {doc_id}:")
    print(response)

def exit(self, args=None):
    raise EOFError

