from pytest import mark

# using decorator

@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

    