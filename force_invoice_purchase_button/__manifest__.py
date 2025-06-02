{
    "name": "force_invoice_purchase_button",
    "summary": "Agrega acción masiva para forzar estado facturado sin bucles prohibidos.",
    "description": "force invoice purchase order, force invoiced, odoo18, odoo purchase module, odoo invoicing, purchase status override, WS Consultores",
    "author": "WS Consultores SpA",
    "website": "https://github.com/WSConsultores",
    "license": "LGPL-3",
    "version": "1.0.1",
    "category": "Purchases",
    "depends": ["purchase"],
    "data": [
        "views/purchase_order_action.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["thumbnail.png", "icon.png"],
}
