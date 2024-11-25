import base64
import qrcode
from io import BytesIO
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    job_card = fields.Char(string="Job Card Number")
    lpo_number = fields.Char(string="LPO Number")
    qr_code = fields.Binary("QR Code", compute="_generate_qr_code", store=True)

    @api.depends('name')
    def _generate_qr_code(self):
        base_url = f"http://localhost"
        for record in self:
            if record.name:
                try:
                    qr_data = f"{base_url}/{record.name}"
                    qr_img = qrcode.make(qr_data)
                    buffer = BytesIO()
                    qr_img.save(buffer, format="PNG")
                    qr_code_base64 = base64.b64encode(buffer.getvalue())
                    record.qr_code = qr_code_base64
                except Exception as e:
                    _logger.error(f"Error generating QR code: {e}")

