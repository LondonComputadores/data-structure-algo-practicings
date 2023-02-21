from sys import int_info
from shared_app.controllers import EmpresaController as SharedController
from .services import VendedorService


class VendedorController():
    # @classmethod
    # def list_condicao_pagto(cls):
    #     try:
    #         cond_pagto = PlanoPagamentoService.select_condicao_pagto()
            
    #         return [{'id': line[0], 'name': line[1], 'field': f"{line[0]} - {line[1]}"} for line in cond_pagto]
    #     except:
    #         return None
    
    # @classmethod
    # def list_adm_credit_card(cls):
    #     try:
    #         adms = PlanoPagamentoService.select_adm_credit_card()
            
    #         return [{'id': line[0], 'name': line[1], 'field': f"{line[0]} - {line[1]}"} for line in adms]
    #     except:
    #         return None
    
    @staticmethod
    def list_supervisors(id_unn: int, id_emp: int):
        try:
            print('oi')
            supers = VendedorService.select_supervisors(id_unn=id_unn, id_emp=id_emp)
            
            return [{'id': line[0], 'name': line[1], 'field': f"{line[0]} - {line[1]}"} for line in supers]
        except:
            return None
        
    @staticmethod
    def list_vendor_type():
        try:
            type = VendedorService.select_nm_tipo_ven()
            
            return [{'id': line[0], 'name': line[1], 'field': f"{line[0]} - {line[1]}"} for line in type]
        except:
            return None

    @classmethod
    def list_vendors(cls, id_unn: int, id_emp: int):

        try:
            vendors = VendedorService.list_vendors(id_unn=id_unn, id_emp=id_emp)
            vendors_out = [cls.format_list_vendors(vendor=vendor)for vendor in vendors]
            return vendors_out
        except:
            return None

    @classmethod
    def search_ven(cls, serialized_data: dict):
        try:
            vendors = VendedorService.search_vendor(data=serialized_data)
            vendors_output = [cls.format_list_vendors(vendor=vendor)for vendor in vendors]
            return vendors_output
        except:
            return None
    
    @classmethod
    def create(cls, serialized_data: dict):
        try:
            cd_situacao = serialized_data.get('cd_situacao')
            print('cd_situacao:', cd_situacao)
            
            if not cd_situacao:
                serialized_data.update({'cd_situacao': 1})
            
            vendor_data = VendedorService.create(data=serialized_data)
            vendor = cls.format_list_vendors(vendor=vendor_data)
            id_ven_ven = vendor.get('id_ven_ven')
            
            if id_ven_ven:
                supervisor = cls.retrieve_one(
                    id_unn=serialized_data.get('id_unn'), 
                    id_emp=serialized_data.get('id_emp'), 
                    id_ven=id_ven_ven
                )
                vendor.update({
                    'supervisor': supervisor['nm_ven']
                })

            return vendor
        except:
            return False

    @classmethod
    def retrieve_one(cls, id_unn: int, id_emp: int, id_ven: int):
        try:
            if id_ven:
                vendor = VendedorService.list_vendors_id(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven)
            
            return cls.format_list_vendors(vendor=vendor)
        except:
            return None
        
    @classmethod
    def retrieve_many(cls, id_unn: int, id_emp: int, id_ven: int):
        try:
            # print(limit, 'controller')
            vendors = VendedorService.list_vendors(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven)
            vendors_output = [cls.format_vendor(vendor=vendor) for vendor in vendors]
            
            for vendor in vendors_output:
                id_ven_ven = vendor.get('id_ven_ven')
                
                if id_ven_ven:
                    supervisor = cls.retrieve_one(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven_ven)
                    
                    vendor.update({
                        'supervisor': supervisor['nm_ven'], 
                        'field_super': f"{supervisor['id_ven']} - {supervisor['nm_ven']}"
                    })
            
            return vendors_output
        except:
            return None

    @classmethod
    def update(cls, serialized_data: dict):
        try:
            id_unn = serialized_data.get('id_unn')
            id_emp = serialized_data.get('id_emp')
            vendor_data = VendedorService.update(data=serialized_data)
            vendor = cls.format_list_vendors(vendor=vendor_data)
            id_ven_ven = vendor.get('id_ven_ven')
            
            if id_ven_ven:
                supervisor = cls.retrieve_one(
                    id_unn=id_unn, 
                    id_emp=id_emp, 
                    id_ven=id_ven_ven
                )
                vendor.update({
                    'supervisor': supervisor['nm_ven']
                })

            return vendor
        except:
            return False

    @classmethod
    def destroy(cls, id_unn: int, id_emp: int, id_ven: int):
        try:
            return VendedorService.destroy(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven)
        except:
            return False
        
    @staticmethod
    def format_vendor(vendor: tuple):
        nm_situacao = 'Ativo' if vendor[7] == 1 else 'Inativo'
        id_nivel_margem = vendor[8]
        nm_nivel_margem = ""
        
        if id_nivel_margem == 1:
            nm_nivel_margem = "Vendedor"
        elif id_nivel_margem == 2:
            nm_nivel_margem = "Gerente"
        elif id_nivel_margem == 3:
            nm_nivel_margem = "Supervisor Regional"
        elif id_nivel_margem == 4:
            nm_nivel_margem = "Supervisor Comercial"
        
        field_nivel_margem = f"{id_nivel_margem} - {nm_nivel_margem}" if id_nivel_margem else None
        
        return {
            'id_cdi': vendor[0],
            'nm_cdi': vendor[1],
            'field_cdi': f"{vendor[0]} - {vendor[1]}",
            'id_ven': vendor[2],
            'nm_ven': vendor[3],
            'field_ven': f"{vendor[2]} - {vendor[3]}",
            'id_matricula': vendor[4],
            'id_ven_erp': vendor[5],
            'cd_tipo_ven': vendor[6],
            'cd_situacao': vendor[7],
            'field_situacao': f"{vendor[7]} - {nm_situacao}",
            'id_nivel_margem': id_nivel_margem,
            'field_nivel_margem': field_nivel_margem,
            'id_ven_ven': vendor[9],
            'supervisor': None,
            'field_super': None,
            'pc_comissao': vendor[10],
            'pc_desconto': vendor[11],
        }

    @staticmethod
    def format_list_vendors(vendor: tuple):
        nm_situacao = 'Ativo' if vendor[4] == 1 else 'Inativo'
        id_nivel_margem = vendor[15]
        nm_nivel_margem = ""
        
        if id_nivel_margem == 1:
            nm_nivel_margem = "Vendedor"
        elif id_nivel_margem == 2:
            nm_nivel_margem = "Gerente"
        elif id_nivel_margem == 3:
            nm_nivel_margem = "Supervisor Regional"
        elif id_nivel_margem == 4:
            nm_nivel_margem = "Supervisor Comercial"
        
        return {
            'id_unn': vendor[0],
            'id_emp': vendor[1],
            'id_ven': vendor[2],
            'id_cdi': vendor[3],
            'cd_situacao': vendor[4],
            'nm_situacao': nm_situacao,
            'nm_ven': vendor[5],
            'id_ven_ven': vendor[6],
            'supervisor': None, 
            'cd_tipo_ven': vendor[7],
            'pc_comissao': vendor[8],
            'pc_desconto': vendor[9],
            'sn_senha': vendor[10],
            'cd_reenvia_mail': vendor[11],
            'nr_cpf': vendor[12],
            'id_matricula': vendor[13],
            'id_ven_erp': vendor[14],
            'id_nivel_margem': vendor[15],
            'nm_nivel_margem': nm_nivel_margem
        }