from shopify.session import Session
from shopify.shop_facade import ShopFacade
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()

# main script to execute

# sf=ShopFacade(s)
# sf.view_all_products()
# sf.edit_product()
# sf.view_all_products()
# filename = sf.export_json()
# sf.import_json(filename)
# sf.view_all_products()
# sf.save_changes_to_server()

''' 
TODO:
1. Importing ALL products (pagination)
2. More advanced editing - only fields specified in API docs.
3. CLI - commang arguments.
4. Print info when changes are committing.
'''
