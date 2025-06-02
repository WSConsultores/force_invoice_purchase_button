{
    "name": "force_invoice_purchase_button",
    "summary": "Agrega acción masiva para forzar estado facturado sin bucles prohibidos.",
    "description":"Este módulo agrega un botón para cambiar manualmente el estado de facturación de una orden de compra a 'Facturado', incluso si no tiene factura. No modifica la contabilidad, solo cambia el estado visual. Compatible con Odoo Online y Odoo.sh.",
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
