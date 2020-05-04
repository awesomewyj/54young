import pytest
from homework.div import div
#\

#Int型测试
@pytest.mark.int_test
@pytest.mark.parametrize("num1,num2,expection", {
    (10, 2, 5),
    (0, 50, 0),
    (10000, 1, 10000),
    (55,5,12)
})
def test_div_intparam(num1, num2, expection):
    assert div(num1, num2) == expection

#float型测试
@pytest.mark.float_test
@pytest.mark.parametrize("num1,num2,expection", {
    (1.05, 1, 1.05),
    (100, 3, 33.333333333333336),
    (7, 4, 1.75)
})
def test_div_floatparam(num1, num2, expection):
    assert div(num1, num2) == expection


#string型测试
@pytest.mark.string_test
@pytest.mark.parametrize("num1,num2,expection", {
    ("abc", 1, TypeError),
    ("abc", "abc", TypeError),
    (7, "abc", TypeError)
})
def test_div_stringparam(num1, num2, expection):
    assert div(num1, num2) == expection

#
#除数是0
@pytest.mark.zero_test
@pytest.mark.parametrize("num1,num2,expection", {
    (5, 0, 'ZeroDivisionError')
})
def test_div_zeroparam(num1, num2, expection):
    with pytest.raises(eval(expection)):
        div(num1, num2)



@pytest.mark.kkk
def test_i():
    assert div(2,2) == 1