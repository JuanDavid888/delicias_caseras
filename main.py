from design.products import desing, tableProducts, tableProductsByCategory
from logic.products import updateInventoryByCode

match desing():
    case 0:
        print("¡Hasta luego!")
    case 1:
        tableProducts()
    case 2:
        tableProductsByCategory(input("Ingrese la categoria a buscar, ejemplo (Panes, Pastel, Postres): "))
    case 3:
        updateInventoryByCode(input("Ingrese el codigo de producto, ejemplo (PN-001): "))
    case _:
        print("Esa opcion no existe")