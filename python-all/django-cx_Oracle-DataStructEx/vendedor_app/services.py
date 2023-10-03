from stratex.oracle_db_config import provide_connection
from stratex.utils import SQLQueryGenerator
from datetime import date, datetime
import cx_Oracle


class VendedorService():
    @staticmethod
    def select_condicao_pagto():
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""SELECT 
                ID_CPG,
                NM_DESCRICAO
            FROM 
                COMMERCE.CONDICAO_PAGTO_VENDA
            ORDER BY 1
        """
        
        return cursor.execute(query).fetchall()
    
    @staticmethod
    def select_adm_credit_card():
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""SELECT 
                ID_ACC,
                NM_ACC
            FROM 
                COMMERCE.ADM_CARTAO_CREDITO
            ORDER BY 1
        """
        
        return cursor.execute(query).fetchall()
    
    @staticmethod
    def select_adm_debit_card():
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""SELECT 
                ID_ACD,
                NM_ACD
            FROM 
                COMMERCE.ADM_CARTAO_DEBITO
            ORDER BY 1
        """
        
        return cursor.execute(query).fetchall()
    
    @staticmethod
    def select_nm_tipo_ven():
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""SELECT 
                SUBSTR(RV_LOW_VALUE,1,2) RV_LOW_VALUE, 
                SUBSTR(RV_MEANING,1,10) RV_MEANING 
            FROM 
                COMMERCE.CG_REF_CODES 
            WHERE
                RV_DOMAIN = 'TIPO VENDEDOR' 
            ORDER BY RV_LOW_VALUE
        """
        
        return cursor.execute(query).fetchall()


    @staticmethod
    def search_vendor(data: dict):
        conn = provide_connection()
        cursor = conn.cursor()
        output = None
        condicao = " "

        id_unn = data.get('id_unn')
        id_emp = data.get('id_emp')
        id_ven = data.get('id_ven')
        id_cdi = data.get('id_cdi')
        cd_situacao = data.get('cd_situacao')
        nm_ven = data.get('nm_ven')
        id_ven_ven = data.get('id_ven_ven')
        cd_tipo_ven = data.get('cd_tipo_ven')
        id_matricula = data.get('id_matricula')
        id_ven_erp = data.get('id_ven_erp')
        nm_email = data.get('nm_email')
        if id_ven:
            condicao += f""" AND ID_VEN={id_ven}"""
        if id_cdi:
            condicao += f""" AND ID_CDI={id_cdi}"""
        if cd_situacao:
            condicao += f""" AND CD_SITUACAO={cd_situacao}"""
        if nm_ven:
            condicao += f""" AND UPPER (NM_VEN) LIKE UPPER('%{nm_ven}%') """
        if id_ven_ven:
            condicao += f""" AND ID_VEN_VEN={id_ven_ven}"""
        if cd_tipo_ven:
            condicao += f""" AND UPPER (CD_TIPO_VEN) = UPPER ('{cd_tipo_ven}') """
        if id_matricula:
            condicao += f""" AND ID_MATRICULA={id_matricula}"""
        if id_ven_erp:
            condicao += f""" AND ID_VEN_ERP = '{id_ven_erp}' """
        if nm_email:
            condicao += f""" AND UPPER (NM_EMAIL) = UPPER ('{nm_email}') """

        query = f"""SELECT 
                V.id_unn,
                V.id_emp,
                V.id_ven,
                V.id_cdi,
                V.cd_situacao,
                V.nm_ven,
                V.id_ven_ven,
                V.cd_tipo_ven,
                V.pc_comissao,
                V.pc_desconto,
                V.sn_senha,
                V.cd_reenvia_mail,
                nr_cpf,
                id_matricula,
                id_ven_erp,
                V.id_nivel_margem                
            FROM
                COMMERCE.VENDEDOR V
            WHERE
                V.ID_UNN = {id_unn}
            AND V.ID_EMP = {id_emp}

        """
        query += condicao
        print('query:', query)

        try:                
            output = cursor.execute(query).fetchall()
        except cx_Oracle.DatabaseError as e:
            error = e.args[0]
            raise Exception(f"""search_vendor  [{error.message}]""")
        
        return output

    
    @staticmethod
    def list_vendors(id_unn: int, id_emp: int):
        conn = provide_connection()
        cursor = conn.cursor()
        output = None
        query = f"""SELECT
                V.id_unn,
                V.id_emp,
                V.id_ven,
                V.id_cdi,
                V.cd_situacao,
                V.nm_ven,
                V.id_ven_ven,
                V.cd_tipo_ven,
                V.pc_comissao,
                V.pc_desconto,
                V.sn_senha,
                V.cd_reenvia_mail,
                nr_cpf,
                id_matricula,
                id_ven_erp,
                V.id_nivel_margem
            FROM
                COMMERCE.VENDEDOR V
            WHERE
                V.ID_UNN = {id_unn}
            AND V.ID_EMP = {id_emp}
        """      

        try:                
            output = cursor.execute(query).fetchall()
        except:
            pass
        
        return output


    @staticmethod
    def list_vendors_id(id_unn: int, id_emp: int, id_ven: int):
        conn = provide_connection()
        cursor = conn.cursor()
        output = None
        query = f"""SELECT
                V.id_unn,
                V.id_emp,
                V.id_ven,
                V.id_cdi,
                V.cd_situacao,
                V.nm_ven,
                V.id_ven_ven,
                V.cd_tipo_ven,
                V.pc_comissao,
                V.pc_desconto,
                V.sn_senha,
                V.cd_reenvia_mail,
                nr_cpf,
                id_matricula,
                id_ven_erp,
                V.id_nivel_margem 
            FROM
                COMMERCE.VENDEDOR V
            WHERE
                V.ID_UNN = {id_unn}
            AND V.ID_EMP = {id_emp}
            AND V.ID_VEN = {id_ven}
        """      

        try:                
            output = cursor.execute(query).fetchone()
        except:
            pass
        
        return output

    
    @classmethod
    def create(cls, data: dict):
        conn = provide_connection()
        cursor = conn.cursor()
        
        try:
            # id_ven = data.get('id_ven')
            # print('id_ven1:', id_ven)
            
            #if not id_ven:
            id_ven = cursor.execute("SELECT NVL(MAX(ID_VEN),0)+1 FROM COMMERCE.VENDEDOR").fetchone()[0]
            print('id_ven2:', id_ven)

            data.update({'id_ven': id_ven})
            print('id_ven3:', id_ven)
            
            keys = list(data.keys())
            values = list(data.values())
            query = SQLQueryGenerator.generateInsertQuery(
                table_name='VENDEDOR', keys=keys, values=values
            )
            print('query:', query)
            
            try:
                cursor.execute(query)
            except cx_Oracle.DatabaseError as e:
                conn.rollback()
                cursor.close
                error = e.args[0]
                cd_erro = error.code
                if cd_erro == 1:
                    mensagem = "Vendedor já cadastrado."
                else:
                    mensagem = f"""Problemas ao tentar inserir vendedor [{error.message}]"""
                raise Exception(mensagem)
                
            conn.commit()
            cursor.close()
            
            return cls.list_vendors_id(
                id_unn=data.get('id_unn'),
                id_emp=data.get('id_emp'),
                id_ven=id_ven
            )
        except:
            return None
    
    @classmethod
    def select_supervisors(cls, id_unn: int, id_emp: int):
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""SELECT 
                ID_VEN, NM_VEN 
            FROM 
                COMMERCE.VENDEDOR
            WHERE 
                ID_UNN = {id_unn}
            AND ID_EMP = {id_emp} 
            AND CD_TIPO_VEN = 'S'
            AND CD_SITUACAO = 1
        """
        
        return cursor.execute(query).fetchall()
    
    @classmethod
    def update(cls, data: dict):
        conn = provide_connection()
        cursor = conn.cursor()
        id_unn = data.pop('id_unn')
        id_emp = data.pop('id_emp')
        id_ven = data.pop('id_ven')
        keys = list(data.keys())
        values = list(data.values())
        query = SQLQueryGenerator.generateSetQuery(
            table_name='VENDEDOR', 
            keys=keys, 
            values=values, 
            where=f"WHERE ID_UNN = {id_unn} AND ID_EMP = {id_emp} AND ID_VEN = {id_ven}"
        )    
        try:
            cursor.execute(query)
            conn.commit()
            cursor.close()
            
            return cls.list_vendors_id(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven)
        except:
            return None
    
    @staticmethod
    def destroy(id_unn: int, id_emp: int, id_ven: int):
        conn = provide_connection()
        cursor = conn.cursor()
        query = f"""DELETE FROM COMMERCE.VENDEDOR
            WHERE ID_UNN = {id_unn} AND ID_EMP = {id_emp} AND ID_VEN = {id_ven}
        """
        try:
            cursor.execute(query)
            conn.commit()
            cursor.close()
            
            return True
        except:
            return False