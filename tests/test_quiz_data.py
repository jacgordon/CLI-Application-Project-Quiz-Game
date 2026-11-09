from src.quiz_data import subject_changer

def test_subject_changer_prints_a_confirmation(capsys):
    subject_changer("1")

    assert capsys.readouterr().out == "Subject changed to Math."


