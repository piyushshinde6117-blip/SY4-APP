class Printer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Printer object created")
        return cls._instance

    def print_document(self, user, document):
        print(f"{user} is printing: {document}")

user1_printer = Printer()
user2_printer = Printer()
user3_printer = Printer()

user1_printer.print_document("User 1", "Assignment.pdf")
user2_printer.print_document("User 2", "Report.pdf")
user3_printer.print_document("User 3", "Notes.pdf")

print("Same object:", user1_printer is user2_printer)
print("Same object:", user2_printer is user3_printer)