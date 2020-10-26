from shopify.session import Session
from shopify.shop_facade import ShopFacade
import click

@click.group()
def main():
    pass


@main.command()
@click.argument('host')
@click.argument('access_token')
@click.argument('extension')
def exp(host, access_token, extension):
    s = Session(host, access_token)
    if extension == 'json':
        print('Exporting all products to JSON...')
        sf = ShopFacade(s)
        filename = sf.export_json()
        print('Done! Filename: ' + filename)
    elif extension == 'yml':
        print('Exporting all products to YML...')
        sf = ShopFacade(s)
        filename = sf.export_yml()
        print('Done! Filename: ' + filename)


@main.command()
@click.argument('host')
@click.argument('access_token')
@click.argument('filename')
def imp(host, access_token, filename):
    s = Session(host, access_token)
    if filename[-4:] == 'json':
        print('Importing products from JSON file...')
        sf = ShopFacade(s)
        sf.import_json(filename)
        print('Pushing changes to server...')
        changed_products = sf.save_imported_changes_to_server()
        print('Done! Products that changed: ')
        print(*changed_products)
    elif filename[-3:] == 'yml':
        print('Importing products from YML file...')
        sf = ShopFacade(s)
        sf.import_yml(filename)
        print('Pushing changes to server...')
        changed_products = sf.save_imported_changes_to_server()
        print('Done! Products that changed: ')
        print(*changed_products)

@main.command()
def ui():
    print('--- Shopify API Client --- ')
    host = input('Host: ')
    access_token = input('access_token: ')
    session = Session(host, access_token)
    print('Downloading all products...')
    shop = ShopFacade(session)
    choice = 1
    while choice != 0:
        print('1 - view all products')
        print('2 - edit a product')
        print('3 - get fresh data from server')
        print('0 - exit')
        choice = int(input('Choose action by inputting index: '))
        if choice == 1:
            shop.view_all_products()
        if choice == 2:
            shop.view_all_products()
            ui_edit(shop)
        if choice == 3:
            shop.refresh_product_list()


def ui_edit(shop: ShopFacade):
    product_index = int(input('Enter index of product to edit: '))
    print('What do you want to change?')
    print('1 - edit basic product attributes')
    print('2 - clear product images')
    print('3 - add a new product image')
    print('4 - reorder product images')
    print('5 - reorder product variants')
    print('6 - update product and one of its variants')
    action = int(input('Enter index of action to take: '))
    if action == 1:
        shop.edit_product_attributes(product_index)
    if action == 2:
        shop.clear_product_images(product_index)
    if action == 3:
        image_src = input('Enter image source: ')
        shop.add_product_image(product_index, image_src)
    if action == 4:
        shop.reorder_product_images(product_index)
    if action == 5:
        shop.reorder_product_variants(product_index)
    if action == 6:
        shop.update_product_and_variant(product_index)
    print('Done!\n')


if __name__ == "__main__":
    main()
