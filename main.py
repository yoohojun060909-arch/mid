import tkinter as tk
from tkinter import font

# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("500x400") # 시작 시 창 크기

# 창 크기가 조절될 때도 위젯이 중앙에 오도록 Frame을 사용합니다.
# 이 Frame이 창 전체를 채우도록 설정합니다.
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

# 표시할 문구
message = "메모장을 만들어봐요"

# 폰트 설정 (조금 더 보기 좋게)
default_font = font.Font(family="Malgun Gothic", size=14)

# 라벨(Label) 위젯 생성
# main_frame 안에 라벨을 위치시킵니다.
label = tk.Label(main_frame, text=message, font=default_font)

# place를 사용하여 라벨을 Frame의 정중앙에 배치합니다.
# relx, rely는 부모 위젯(Frame) 내의 상대적 위치(0.0 ~ 1.0)를 의미합니다.
# anchor='center'는 위젯의 중앙을 기준으로 위치를 잡도록 합니다.
label.place(relx=0.5, rely=0.5, anchor='center')

# 윈도우 실행
window.mainloop()
