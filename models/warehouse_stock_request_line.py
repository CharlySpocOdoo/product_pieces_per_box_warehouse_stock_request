# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CustomWarehouseStockRequestLine(models.Model):
    _inherit = 'custom.warehouse.stock.request.line'

    # Campo propio de este módulo puente (no reutiliza el mixin del módulo
    # de Compras/Inventario a propósito: así este módulo solo depende de
    # 'product_pieces_per_box' y de 'warehouse_stock_request', sin arrastrar
    # 'purchase' ni 'stock' como dependencias adicionales).
    pieces_per_box_display = fields.Char(
        string='Caja',
        compute='_compute_pieces_per_box_display',
        help="Piezas por caja configuradas para este producto (ej. 'x 50'"
             "). Solo informativo: no afecta la cantidad ni la UoM de "
             "esta línea.",
    )

    @api.depends('product_id')
    def _compute_pieces_per_box_display(self):
        for line in self:
            qty = 0
            if line.product_id:
                qty = line.product_id.pieces_per_box_qty
            line.pieces_per_box_display = str(qty) if qty else ''
