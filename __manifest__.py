# -*- coding: utf-8 -*-
{
    'name': 'Piezas por Caja - Warehouse Stock Request',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Columna informativa "Caja" en Warehouse Stock Request',
    'description': """
Piezas por Caja - Warehouse Stock Request
============================================
Agrega la columna informativa de solo lectura "Caja" en las líneas de
producto del módulo de terceros 'Warehouse Stock Request'
(custom.warehouse.stock.request.line), justo después de la columna UOM.

Este módulo es un puente: NO modifica ningún archivo del módulo
'Warehouse Stock Request' original, solo lo hereda. Si en algún momento
desinstalas Warehouse Stock Request, puedes desinstalar este módulo junto
con él sin afectar a 'product_pieces_per_box' ni a
'product_pieces_per_box_purchase_stock'.

Requiere los módulos 'product_pieces_per_box' y 'warehouse_stock_request'.
    """,
    'author': 'Tu Empresa',
    'license': 'LGPL-3',
    'depends': ['product_pieces_per_box', 'warehouse_stock_request'],
    'data': [
        'views/warehouse_stock_request_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
}
