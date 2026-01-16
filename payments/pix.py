import uuid
import qrcode
class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # Criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        #gerar o copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'

        #gerar o qr_code
        img = qrcode.make(hash_payment)        
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png") #salva imagem no repositorio

        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}