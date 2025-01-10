from formula.products import updateQuantityInventory
from tabulate import tabulate
import json

def findAll():
    with open("data/products.json", "r", encoding="utf-8") as file :
        data = file.read()
        convertedList = json.loads(data)
        return convertedList
    
def saveAll(data):
    with open("data/products.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "Se modifico el archivo products.json"

def addProduct(formulary):
    data = findAll()
    data.append(formulary)
    return saveAll(data)

def updateInventoryByCode(code_product):
    data = findAll()
    for product in data:
        if(product.get('codigo_producto') == code_product):
            quantity = int(input("Ingrese la cantidad de productos que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(f"Se actualizo el stock de {code_product} a {stock}")
    print(saveAll(data))
