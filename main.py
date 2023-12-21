import file_worker, scanner

while True:
    command = scanner.Scanner.input_command()
    note_pad = file_worker.File_Worker
    note_pad.__init__(note_pad)
    if command == "add":
        file_worker.File_Worker.add_note(note_pad)

    if command == "read":
        file_worker.File_Worker.read_note(note_pad)

    if command == "edit":
        file_worker.File_Worker.edit_note(note_pad)

    if command == "delete":
        file_worker.File_Worker.delete_note(note_pad)
    