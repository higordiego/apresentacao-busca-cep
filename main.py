import sys

import database.repository as rp_cep
import services.cep as http_cep

cep_digitado = input("Digite o cep: ")

cep_integracao_resultado = http_cep.get_cep(cep_digitado)

print("cep_integracao_resultado", cep_integracao_resultado)

rp_cep.insert_cep(
    cep_integracao_resultado['cep'],
    cep_integracao_resultado['logradouro'],
    cep_integracao_resultado['complemento'],
    cep_integracao_resultado['bairro'],
    cep_integracao_resultado['localidade'],
    cep_integracao_resultado['uf']
)


print("foi inserido com sucesso essa operação de consulta de cep.")






