from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('message', 'stg')

    assert encrypt_message('message', 10) == 'egassem'
    assert encrypt_message('message', 3) == 'sem_egas'
    assert encrypt_message('message', 4) == 'ega_ssem'
