import notes
import json
import scanner
from datetime import datetime
class File_Worker:
    all_notes = {}
    index = 0
        
    def __init__(self):
        self.load_notes(self)
        self.get_index(self)

    def add_note(self):
        title = scanner.Scanner.take_title() + " Time " + str(datetime.now())
        note = scanner.Scanner.take_notes()
        pre_note = notes.Note(title, note)
        self.all_notes[self.index] = pre_note.get_note()
        self.index += 1
        self.save_note(self)

    def save_note(self):
        with open('Notes.json', 'w') as n:
            json.dump(self.all_notes, n, skipkeys=True)

    def read_note(self):
        self.load_notes(self)
        print(self.all_notes)

    def edit_note(self):
        self.read_note(self)
        edit = scanner.Scanner.take_edit()
        edit_title = scanner.Scanner.take_title() + " Time " + str(datetime.now())
        edit_note = scanner.Scanner.take_notes()
        self.all_notes[edit] = {edit_title:edit_note}
        self.save_note(self)

    def delete_note(self):
        delete_note = scanner.Scanner.take_delete()
        self.load_notes(self)
        self.all_notes.pop(delete_note)
        self.save_note(self)

    def load_notes(self):
        with open('Notes.json') as n:
            try:
                self.all_notes = json.load(n)
            except:
                pass

    def get_index(self):
        self.load_notes(self)
        try:
            keys = [key for key in self.all_notes] 
            self.index = int(keys.pop()) + 1
        except:
            pass