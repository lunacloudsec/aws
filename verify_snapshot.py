import boto3

# Variaveis
region='us-east-1' # Regiao onde se conectará. Precisa ser a mesma onde está os snapshots
session=boto3.session.Session()
ec2client = boto3.client('ec2', region_name=region)
ec2resource = boto3.resource('ec2', region_name=region)
sts_client=session.client('sts')
ownaccountid=sts_client.get_caller_identity().get('Account')
qnt_completed = qnt_pendig = qnt_error = qnt_total = 0


# Verificar o status de todos os snapshots
for snapshot in ec2client.describe_snapshots(OwnerIds=[ownaccountid])['Snapshots']:
   qnt_total+=1
   if snapshot['State'] == 'completed':
       qnt_completed+=1
   elif snapshot['State'] == 'pending':
       qnt_pendig+=1
   elif snapshot['State'] == 'error':
       qnt_error+=1

print('Status Snapshots\n Total: {}\n Completos: {}\n Pendentes: {}\n Erros: {}\n'.format(qnt_total,qnt_completed,qnt_pendig,qnt_error))

# Resultado da analise dos snapshots
if (qnt_completed == qnt_total):
    print('Atualização de patches liberada, todos os snapshots foram executados.')
else:
    print('Existem snapshots pendentes ou com erros.')
