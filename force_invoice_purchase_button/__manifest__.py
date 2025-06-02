{
    "name": "force_invoice_purchase_button",
    "summary": "Agrega acción masiva para forzar estado facturado sin bucles prohibidos.",
    "description":"force invoice purchase order, purchase order invoicing, odoo18 force invoice, manual invoice status, set purchase order to invoiced, odoo purchase customization, invoice status override, odoo purchase order status fix, odoo force invoice state, WS Consultores, odoo18, odoo apps, force invoice button, purchase workflow fix",
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
