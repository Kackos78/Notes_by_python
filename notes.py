from scanner import Scanner
import file_worker
class Note(object):

    def __init__(self, title, note):
        self.notes = {title:note}

    notes = {}

    def get_note(self):
        return self.notes
    
    def load_notes(self):
        self.notes = file_worker.load_notes()

