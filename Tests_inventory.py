from Testes import Login_Inventory



def AddToCart():
    Inventory_test = Login_Inventory()
    Inventory_test.ValidLogin()
    assert "Remove" in Login_Inventory.add_to_cart.text
    Inventory_test.closeBrowser()

