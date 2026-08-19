# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def uninstall_hook(env):
    """Igual que en el módulo de Compras e Inventario: 'pieces_per_box_display'
    es un campo calculado, no almacenado (no store), así que no hay ningún
    valor guardado en la base de datos que limpiar.

    Este hook tampoco toca nada del módulo 'warehouse_stock_request' en sí
    (ni sus registros, ni su configuración): este módulo solo hereda su
    modelo y su vista, nunca modifica sus archivos originales.
    """
    _logger.info(
        "product_pieces_per_box_warehouse_stock_request: uninstall_hook "
        "ejecutado. No se eliminó ningún dato: 'pieces_per_box_display' "
        "no se almacena en base de datos. Ninguna solicitud de stock de "
        "almacén (custom.warehouse.stock.request) fue modificada."
    )
