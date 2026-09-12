import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from results import grade

def test_grades():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(75) == "B"
    assert grade(65) == "C"
    assert grade(55) == "D"
    assert grade(35) == "F"
