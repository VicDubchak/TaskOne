from pywinauto.application import Application
import time

# 1. Запускаем Блокнот
app = Application(backend="uia").start("notepad.exe")

# 2. Подключаемся к главному окну Блокнота
# Имя окна в Windows 11 обычно содержит "Блокнот" или "Untitled - Notepad"
main_window = app.window(title_re=".*Блокнот.*|.*Notepad.*")

# 3. Находим поле для ввода текста (его тип в UIA — Edit) и пишем текст
text_field = main_window.child_window(control_type="Edit")
text_field.type_keys("Привет! Этот текст написан автоматически через UI Automation.", with_spaces=True)

# 4. Небольшая пауза для наглядности
time.sleep(2)

# 5. Имитируем нажатие на верхнее меню "Файл" (или "File")
# Мы можем обращаться к элементам прямо по их названиям в интерфейсе
main_window.child_window(title="Файл", control_type="MenuItem").click_input()

print("Действие успешно выполнено!")