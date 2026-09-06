from ucv_lab1_si.main import suma, es_mayor_que_cinco


def test_suma():
    assert suma(5, 3) == 8


def test_es_mayor_que_cinco():
    assert es_mayor_que_cinco(8) is True
    assert es_mayor_que_cinco(3) is False