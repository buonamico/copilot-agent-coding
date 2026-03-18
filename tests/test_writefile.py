from pathlib import Path
import subprocess
import sys


def _script_path() -> Path:
    return Path(__file__).resolve().parents[1] / "writefile.py"


def test_writefile_success(tmp_path):
    out = tmp_path / "out.txt"
    text = "hello world"
    proc = subprocess.run([sys.executable, str(_script_path()), "--output", str(out), "--text", text], capture_output=True, text=True)
    # script prints a success message and writes the file
    assert proc.returncode == 0
    assert out.read_text() == text + "\n"
    assert f'Wrote "{text}" to file "{out}"' in proc.stdout


def test_writefile_error_writing_directory(tmp_path):
    # attempting to open a directory for writing should cause an IOError handled by the script
    dirpath = tmp_path
    proc = subprocess.run([sys.executable, str(_script_path()), "-o", str(dirpath), "-t", "ignored"], capture_output=True, text=True)
    assert proc.returncode == 0
    assert "Error writing to file" in proc.stdout
    assert str(dirpath) in proc.stdout
