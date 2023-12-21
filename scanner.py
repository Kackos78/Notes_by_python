class Scanner:
    def input_command():
        return input("Введите команду (add, save, read, edit, delete): ")
    
    def take_title():
        return input("Введите заголовок: ")
    
    def take_notes():
        return input("Введите заметку: ")

    def take_edit():
        return input("Введите номер заметки для её изменения: ")
    
    def take_delete():
        return input("Введите номер заметки для удаления: ")