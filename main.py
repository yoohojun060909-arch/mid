import tkinter as tk
from tkinter import font, filedialog

# 현재 열려있는 파일의 경로를 저장하기 위한 변수
current_file = None

# --- 메뉴 기능 함수들 ---

def new_file():
    """새 파일: 텍스트 영역을 비웁니다."""
    global current_file
    text_area.delete(1.0, tk.END)
    window.title("메모장 - 새 파일")
    current_file = None

def open_file():
    """파일 열기: 파일을 열어 내용을 텍스트 영역에 표시합니다."""
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        window.title(f"메모장 - {file_path}")
        text_area.delete(1.0, tk.END)
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.insert(tk.END, file.read())

def save_file():
    """파일 저장: 현재 파일에 저장하거나, 새 파일이면 다른 이름으로 저장을 호출합니다."""
    global current_file
    if current_file:
        try:
            content = text_area.get(1.0, tk.END)
            with open(current_file, "w", encoding="utf-8") as file:
                file.write(content)
            window.title(f"메모장 - {current_file}")
        except Exception as e:
            print(f"저장 중 오류 발생: {e}")
    else:
        save_as_file()

def save_as_file():
    """다른 이름으로 저장: 새 파일로 저장합니다."""
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        save_file()

def exit_app():
    """프로그램 종료"""
    window.destroy()


# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("500x400") # 시작 시 창 크기

# 메뉴바 생성
menu_bar = tk.Menu(window)

# 파일 메뉴 생성
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="다른 이름으로 저장", command=save_as_file)
file_menu.add_separator() # 구분선
file_menu.add_command(label="종료", command=exit_app)
menu_bar.add_cascade(label="파일", menu=file_menu)
window.config(menu=menu_bar)

# 텍스트 입력을 위한 위젯과 스크롤바 생성
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area = tk.Text(window, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Malgun Gothic", 12))
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_area.yview)

# 윈도우 실행
window.mainloop()
