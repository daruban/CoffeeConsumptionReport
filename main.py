import argparse
from config.reportlist import reportList
import os

def start_script():
    parser = argparse.ArgumentParser(description="Аргументы командной строки")
    parser.add_argument("--files", nargs="+", default=None, help="Название файлов")
    parser.add_argument("--report", default=None, help="Название отчета")

    args = parser.parse_args()

    if args.report is None:
        raise Exception("Ошибка! Не заполнены название отчета")

    if args.files is None:
        raise Exception("Ошибка! Не заполнены названия файлов")

    if reportList.get(args.report) is None:
        raise Exception("Ошибка! Не найден отчет")

    for file in args.files:
        if not os.path.exists(file):
            raise Exception(f"Ошибка! Файл {file} не найден")

    report = reportList.get(args.report)(args.files)
    report.start()


if __name__ == "__main__":
    start_script()
