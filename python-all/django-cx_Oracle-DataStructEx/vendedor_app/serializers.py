from rest_framework import serializers


def validator_sim_nao(value):
    accepted = ['S', 'N']
    if str(value) not in accepted:
        raise serializers.ValidationError('Esse campo aceita S=Sim ou N=Não')

def validator_situacao(value):
    accepted = ['1', '9']
    if str(value) not in accepted:
        raise serializers.ValidationError('Esse campo aceita 1=ativo ou 9=inativo')

def validator_nivel_margem(value):
    accepted = ['1', '2', '3', '4']
    if str(value) not in accepted:
        raise serializers.ValidationError('Esse campo aceita 1=VENDEDOR, 2=GERENTE, 3=SUPERVISOR-REG ou 4=SUPERVISOR-COMERCIAL')

class VendedorSerializer(serializers.Serializer):
    id_unn = serializers.IntegerField()
    id_emp = serializers.IntegerField()
    id_ven = serializers.IntegerField(max_value=999999)
    id_cdi = serializers.IntegerField(max_value=99)
    cd_situacao = serializers.IntegerField(max_value=99, validators=[validator_situacao])
    nm_ven = serializers.CharField(max_length=50)
    id_ven_ven = serializers.IntegerField(max_value=999999)
    cd_tipo_ven = serializers.CharField(max_length=1)
    pc_comissao = serializers.DecimalField(max_digits=5, decimal_places=2)
    pc_desconto = serializers.DecimalField(max_digits=5, decimal_places=2)
    sn_senha = serializers.CharField(max_length=6)
    qt_ciclo_visita = serializers.CharField(max_length=2)
    cd_reenvia_mail = serializers.CharField(max_length=1)
    nr_cpf = serializers.IntegerField(max_value=99999999999)
    cd_equipe = serializers.CharField(max_length=10)
    id_matricula = serializers.IntegerField(max_value=999999999)
    dt_ult_mensagem = serializers.DateTimeField()
    st_seleciona_preco_orc = serializers.CharField(max_length=1)
    prct_margem_minima = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    id_ven_erp = serializers.CharField(max_length=30)
    id_nivel_margem = serializers.IntegerField(max_value=99999)
    nr_ddd = serializers.CharField(max_length=4)
    nr_telefone = serializers.IntegerField(max_value=999999999999)
    dt_ult_alt_senha = serializers.DateTimeField()
    cd_senha_bloq = serializers.CharField(max_length=1)
    id_usu = serializers.CharField(max_length=30)
    nm_email = serializers.CharField(max_length=60)

class VendedorSearchSerializer(serializers.Serializer):
    id_unn = serializers.IntegerField(required=True)
    id_emp = serializers.IntegerField(required=True)
    id_ven = serializers.IntegerField(required=False, max_value=999999, allow_null=True)
    id_cdi = serializers.IntegerField(required=False, max_value=99, allow_null=True)
    cd_situacao = serializers.IntegerField(required=False, max_value=99, validators=[validator_situacao], allow_null=True)
    nm_ven = serializers.CharField(required=False, max_length=50, allow_null=True)
    id_ven_ven = serializers.IntegerField(required=False, max_value=999999, allow_null=True)
    cd_tipo_ven = serializers.CharField(required=False, max_length=1, allow_null=True)
    id_matricula = serializers.IntegerField(required=False, max_value=999999999, allow_null=True)
    id_ven_erp = serializers.CharField(required=False, max_length=30, allow_null=True)
    nm_email = serializers.CharField(required=False, max_length=60, allow_null=True)
    
    
class VendedorCreateSerializer(serializers.Serializer):
    id_unn = serializers.IntegerField(required=True)
    id_emp = serializers.IntegerField(required=True)
    id_cdi = serializers.IntegerField(max_value=99)
    nm_ven = serializers.CharField(max_length=50)
    cd_tipo_ven = serializers.CharField(max_length=1)
    pc_comissao = serializers.DecimalField(max_digits=5, decimal_places=2)
    pc_desconto = serializers.DecimalField(max_digits=5, decimal_places=2)
    sn_senha = serializers.CharField(required=True, max_length=6)
    id_ven = serializers.IntegerField(max_value=999999, required=False)
    id_ven_ven = serializers.IntegerField(max_value=999999, required=False)
    qt_ciclo_visita = serializers.CharField(max_length=2, required=False)
    cd_reenvia_mail = serializers.CharField(max_length=1, required=False)
    nr_cpf = serializers.IntegerField(max_value=99999999999, required=False)
    cd_equipe = serializers.CharField(max_length=10, required=False)
    id_matricula = serializers.IntegerField(max_value=999999999, required=False)
    dt_ult_mensagem = serializers.DateTimeField(required=False)
    st_seleciona_preco_orc = serializers.CharField(max_length=1, required=False)
    prct_margem_minima = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    id_ven_erp = serializers.CharField(max_length=30, required=False)
    id_nivel_margem = serializers.IntegerField(max_value=99999, required=False, validators=[validator_nivel_margem])
    nr_ddd = serializers.CharField(max_length=4, required=False)
    nr_telefone = serializers.IntegerField(max_value=999999999999, required=False)
    dt_ult_alt_senha = serializers.DateTimeField(required=False)
    cd_senha_bloq = serializers.CharField(max_length=1, required=False)
    id_usu = serializers.CharField(max_length=30, required=False)
    cd_situacao = serializers.IntegerField(max_value=99, validators=[validator_situacao], required=False)
    nm_email = serializers.CharField(required=False, max_length=60, allow_null=True)
    

class VendedorUpdateSerializer(serializers.Serializer):
    id_unn = serializers.IntegerField(required=True)
    id_emp = serializers.IntegerField(required=True)
    id_ven = serializers.IntegerField(max_value=999999, required=True)
    id_cdi = serializers.IntegerField(max_value=99, required=False)
    cd_situacao = serializers.IntegerField(max_value=99, validators=[validator_situacao], required=False)
    nm_ven = serializers.CharField(max_length=50, required=False)
    id_ven_ven = serializers.IntegerField(max_value=999999, required=False)
    cd_tipo_ven = serializers.CharField(max_length=1, required=False)
    pc_comissao = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    pc_desconto = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    sn_senha = serializers.CharField(max_length=6, required=False)
    qt_ciclo_visita = serializers.CharField(max_length=2, required=False)
    cd_reenvia_mail = serializers.CharField(max_length=1, required=False)
    nr_cpf = serializers.IntegerField(max_value=99999999999, required=False)
    cd_equipe = serializers.CharField(max_length=10, required=False)
    id_matricula = serializers.IntegerField(max_value=999999999, required=False)
    dt_ult_mensagem = serializers.DateTimeField(required=False)
    st_seleciona_preco_orc = serializers.CharField(max_length=1, required=False)
    prct_margem_minima = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    id_ven_erp = serializers.CharField(max_length=30, required=False)
    id_nivel_margem = serializers.IntegerField(max_value=99999, required=False, validators=[validator_nivel_margem])
    nr_ddd = serializers.CharField(max_length=4, required=False)
    nr_telefone = serializers.IntegerField(max_value=999999999999, required=False)
    dt_ult_alt_senha = serializers.DateTimeField(required=False)
    cd_senha_bloq = serializers.CharField(max_length=1, required=False)
    id_usu = serializers.CharField(max_length=30, required=False)
    nm_email = serializers.CharField(required=False, max_length=60, allow_null=True)
    

class VendedorBriefSerializer(serializers.Serializer):
    id_cdi = serializers.IntegerField(max_value=99, required=False)
    nm_cdi = serializers.CharField(required=False)
    field_cdi = serializers.CharField(required=False)
    id_ven = serializers.IntegerField(max_value=999999, required=True)
    nm_ven = serializers.CharField(max_length=50, required=False)
    field_ven = serializers.CharField(required=False)
    id_matricula = serializers.IntegerField(max_value=999999999, required=False)
    id_ven_erp = serializers.CharField(max_length=30, required=False)
    cd_tipo_ven = serializers.CharField(max_length=1, required=False)
    cd_situacao = serializers.IntegerField(max_value=99, validators=[validator_situacao], required=False)
    field_situacao = serializers.CharField(required=False)
    id_nivel_margem = serializers.IntegerField(max_value=99999, required=False)
    field_nivel_margem = serializers.CharField(required=False)
    id_ven_ven = serializers.IntegerField(max_value=999999, required=False)
    supervisor = serializers.CharField(required=False)
    field_super = serializers.CharField(required=False)
    pc_comissao = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    pc_desconto = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    nm_email = serializers.CharField(max_length=60)
    

class VendedorListSerializer(serializers.Serializer):
    vendedores = VendedorBriefSerializer(many=True)