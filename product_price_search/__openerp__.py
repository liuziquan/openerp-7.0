# -*- coding: utf-8 -*-
# © 2014 Elico corp(www.elico-corp.com)
# Licence AGPL-3.0 or later(http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Product Price Category',
    'version': '7.0.1.0.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'description' : """
    User can quickly search the product price base on the quality.
    """,
    'depends': ['base','product',],
    'category': '',
    'sequence': 16,
    'data': [
             'security/price_search_security.xml',
             'security/ir.model.access.csv',
             'product_price.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}



