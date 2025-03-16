import pytest
import sys
import os

# Tambahkan path root project ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.logic import calculate_disease_probability  # Impor absolut
def test_dermatitis_diagnosis():
    # Gejala: Kemerahan (id=1), Gatal (id=2)
    selected_symptoms = [1, 2]
    
    results = calculate_disease_probability(selected_symptoms)
    
    assert len(results) > 0
    assert results[0]['disease']['name'] == "Dermatitis"
    assert results[0]['probability'] == 100.0  # Karena memenuhi semua gejala wajib

def test_partial_symptoms():
    # Hanya gejala kemerahan (id=1)
    selected_symptoms = [1]
    
    results = calculate_disease_probability(selected_symptoms)
    
    assert len(results) == 0  # Seharusnya tidak memenuhi gejala wajib

    print(sys.path)  # Tambahkan ini di test_diagnosis.py