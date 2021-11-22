import boto3
from datetime import date

ec2 = boto3.resource("ec2")
hoje = date.today().strftime('%d-%m-%Y')

'''
Percorre todos os volumes atachados nas instancias EC2 (da conta autenticada) e faz o snapshot de cada um
'''
for vol in ec2.volumes.all():
    vol_id = vol.id # Variavel do volume id de cada instancia
    volume = ec2.Volume(vol_id)
    desc = 'Snapshot do Volume {} - Patch Manager {}'.format(vol_id,hoje) # Descrição do snapshot
    print("Criando snapshot do Volume: ", vol_id)
    volume.create_snapshot(Description=desc,
        TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            # Tag do snapshot
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'snapshot-poc-18-11-2021'
                },
            ]
        },
    ]
)
