from design.products import desing as desingProducts, tableProducts, tableProductsByCategory, formularyAddProduct
from logic.products import updateInventoryByCode
from  design.customer import desing as desingCustomer, formularyTakeOrder

match desingCustomer():
    case 0:
        print("¡Hasta luego!")
    case 1:
        formularyTakeOrder()
    case _:
        print("Esa opcion no existe")

#match desingProducts():
    #case 0:
        #print("¡Hasta luego!")
    #case 1:
        #tableProducts()
    #case 2:
        #tableProductsByCategory(input("Ingrese la categoria a buscar, ejemplo (Panes, Pastel, Postres): "))
    #case 5:
        #updateInventoryByCode(input("Ingrese el codigo de producto, ejemplo (PN-001): "))
    #case 6: 
        #formularyAddProduct()
    #case _:
        #print("Esa opcion no existe")