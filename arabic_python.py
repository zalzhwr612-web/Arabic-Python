import sys
import tkinter as tk
from tkinter import messagebox

# قاموس الترجمة المطور للدعم الواجهات
ARABIC_TO_PYTHON = {
    # الكلمات المفتاحية والدوال الأساسية
    "إذا": "if",
    "وإلا_إذا": "elif",
    "وإلا": "else",
    "دالة": "def",
    "ارجع": "return",
    "لكل": "for",
    "طالما": "while",
    "في": "in",
    "اطبع": "print",
    "أدخل": "input",
    # عناصر التطبيقات والواجهات (GUI)
    "تطبيق": "tk.Tk",
    "عنوان_التطبيق": "title",
    "حجم_التطبيق": "geometry",
    "زر": "tk.Button",
    "نص_توضيحي": "tk.Label",
    "حقل_إدخال": "tk.Entry",
    "نافذة_رسالة": "messagebox.showinfo",
    "عرض": "pack",
    "تشغيل_التطبيق": "mainloop",
}


def تشغيل_كود_عربي(مسار_الملف):
    with open(مسار_الملف, "r", encoding="utf-8") as file:
        code = file.read()

    for عربية, إنجليزية in ARABIC_TO_PYTHON.items():
        code = code.replace(عربية, إنجليزية)

    exec(code)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        تشغيل_كود_عربي(sys.argv[1])

