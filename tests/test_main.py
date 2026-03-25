import pytest
import sys
from unittest.mock import patch
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from main import start_script


class TestMain:

    def test_missing_report(self):
        with pytest.raises(Exception, match="Ошибка! Не заполнены название отчета"):
            with patch("sys.argv", ["main.py", "--files", "file1.txt"]):
                start_script()

    def test_missing_files(self):
        with pytest.raises(Exception, match="Ошибка! Не заполнены названия файлов"):
            with patch("sys.argv", ["main.py", "--report", "test_name"]):
                start_script()

    def test_missing_report_name(self):
        with pytest.raises(Exception, match="Ошибка! Не найден отчет"):
            with patch(
                "sys.argv",
                ["main.py", "--files", "file1.txt", "--report", "ERROR_NAME"],
            ):
                start_script()
