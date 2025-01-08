from design.products import desing, tableProducts

match desing():
    case 1:
        tableProducts()
    case _:
        print("Esa opcion no existe")