import pytest
import csv
import os
import tempfile
from unittest.mock import Mock, patch, mock_open, MagicMock
from Reports.median_coffee import MedianCoffee


class TestMedianCoffee:

    @pytest.fixture
    def sample_csv_data(self):
        return [
            {"student": "Имя Один", "coffee_spent": "100"},
            {"student": "Имя Два", "coffee_spent": "200"},
            {"student": "Имя Один", "coffee_spent": "150"},
            {"student": "Имя Два", "coffee_spent": "250"},
        ]

    @pytest.fixture
    def temp_csv_file(self, sample_csv_data):
        with tempfile.NamedTemporaryFile(
            mode="w", newline="", suffix=".csv", delete=False, encoding="UTF=8"
        ) as f:
            writer = csv.DictWriter(f, fieldnames=["student", "coffee_spent"])
            writer.writeheader()
            writer.writerows(sample_csv_data)
            temp_path = f.name

        yield temp_path
        os.unlink(temp_path)

    @pytest.fixture
    def median_coffee(self):
        return MedianCoffee([])

    def test_start(self, median_coffee, capsys):
        median_coffee.report_data = [["Имя Один", 150], ["Имя Два", 225]]
        median_coffee.start()
        captured = capsys.readouterr()
        assert "Имя Один" in captured.out
        assert "150" in captured.out
        assert "Имя Два" in captured.out
        assert "225" in captured.out

    def test_file_processing(self, temp_csv_file, median_coffee):
        median_coffee.file_processing(temp_csv_file)
        expected_data = {
            "Имя Один": [100, 150],
            "Имя Два": [200, 250],
        }
        assert dict(median_coffee.user_spent) == expected_data

    def test_median(self, median_coffee):
        median_coffee.user_spent = {
            "Имя Один": [100, 200, 300],
            "Имя Два": [50, 150],
        }
        median_coffee.median()
        expected_report = [["Имя Один", 200], ["Имя Два", 100]]
        assert median_coffee.report_data == expected_report

    def test_send_report(self, median_coffee, capsys):
        median_coffee.report_data = [["Имя Один", 150], ["Имя Два", 225]]
        median_coffee.send_report()
        captured = capsys.readouterr()
        assert "Имя Один" in captured.out
        assert "150" in captured.out
        assert "Имя Два" in captured.out
        assert "225" in captured.out
