{
    "name": "force_invoice_purchase_button",
    "summary": "Agrega acción masiva para forzar estado facturado sin bucles prohibidos.",
    "description": """
        <p>Este módulo agrega un botón para cambiar manualmente el estado de facturación de una orden de compra a "Facturado", incluso si no tiene factura.</p>
        <ul>
            <li>No modifica la contabilidad.</li>
            <li>Sólo cambia el estado visual.</li>
            <li>Compatible con Odoo Online y Odoo.sh</li>
        </ul>
    """,
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
    "images": ["thumbnail.png","icon.png"],
}
