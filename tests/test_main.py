from ucv_lab1_si.main import suma, es_mayor_que_cinco, multiplicacion


def test_suma():
    assert suma(5, 3) == 8


def test_es_mayor_que_cinco_true():
    assert es_mayor_que_cinco(8) is True


def test_es_mayor_que_cinco_false():
    assert es_mayor_que_cinco(5) is False


def test_multiplicacion():
    assert multiplicacion(5, 3) == 15