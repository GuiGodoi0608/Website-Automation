from Testes.loginTest import Login


def test_valid_login():
    login = Login()
    login.ValidLogin()
    assert "inventory.html" in login.driver.current_url
    login.closeBrowser()


def test_locked_out_user():
    login = Login()
    login.InvalidLogin()
    assert "inventory.html" not in login.driver.current_url
    login.closeBrowser()


def test_performance_user():
    login = Login()
    duration = login.performanceUser()
    assert duration > 2, "Page logged in in less than two seconds"
    assert duration <= 4, f"Page has problems in loggin-in it took {duration:6f}"
    login.closeBrowser()


