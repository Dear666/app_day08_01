import allure,pytest

class Test_01:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="第一个测试")
    def test_01(self):
        allure.attach("描述","这个是登录")
        allure.attach("描述","这个是注册")
        assert 0