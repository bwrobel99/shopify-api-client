# shopify-api-client
A basic shopify API client capable of fetching info about the products &amp; editing and exporting it.

# Usage
Use the client by executing the file present in the `bin` folder:
```python
py .\bin\shopify_api_client.py --ACTION --ARGS
```
`--ACTION` can be:  
  1. `ui` - launches client's console window UI. Enables you to view and edit products.  
  2. `exp` - exports all products to a `products_{timestamp}` file - timestamp to avoid overwriting.  
    2.1. `--ARGS`: `host access_token extension`, `extension` can be `'json'` or `'yml'`
  3. `imp`  imports all products, looks for changes and pushes them to server:  
    3.1. `--ARGS`: `host access_token filename`, pass `filename` with extension  
    
## Examples
```python
# open ui
py .\bin\shopify_api_client.py ui 
```  
```python
# export to json
py .\bin\shopify_api_client.py exp yourshop.shopify.com actkn_02893123jjkd123sdsa json
```  
```python
# export to yml
py .\bin\shopify_api_client.py exp yourshop.shopify.com actkn_02893123jjkd123sdsa yml
```  
```python
# import json
py .\bin\shopify_api_client.py imp yourshop.shopify.com actkn_02893123jjkd123sdsa products_2020-09-10_14-10-20.json
```
```python
# import yml
py .\bin\shopify_api_client.py imp yourshop.shopify.com actkn_02893123jjkd123sdsa products_2020-09-10_14-10-20.yml
```
