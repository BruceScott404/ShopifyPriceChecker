import csv

shopify_products = {}
in_store_products = {}

with open("all_products_shopify.csv", mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        compare_at = row['Variant Compare At Price']
        sku = row['Variant SKU']
        price = row['Variant Price']
        if not(compare_at == ''):
                price = compare_at
        shopify_products[sku] = price

with open("total_inventory.csv", mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sku = row['Part Number']
        price = row['Price']
        in_store_products[sku] = price

with open("non_existant.csv", 'w') as non_ex:
    with open("output.csv", mode='w') as file:
        file.write("SKU,Shopify Price,In Store Price\n")
        for item in shopify_products:
            if item in in_store_products:
                if not(in_store_products[item] == shopify_products[item]):
                    if str(in_store_products[item]).replace(",", "") == str(shopify_products[item]):
                         continue
                    print("Mismatch ", item, shopify_products[item])
                    file.write(str(item) + "," + str(shopify_products[item]) + "," + str(in_store_products[item]).replace(",", "") + "\n")
            else:
                 non_ex.write(str(item) + "\n")