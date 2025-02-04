from django.core.management.base import BaseCommand
from mysite.models import Variavel

class Command(BaseCommand):
    help = "Popula o banco de dados com valores padrão para a tabela Variavel."

    def handle(self, *args, **kwargs):
        valores_padrao = [
            {"variavel": "@{armamento.tipo}@", "descricao": "Tipo de Armamento", "tipo": 1},
            {"variavel": "@{armamento.modelo}@", "descricao": "Modelo de Armamento", "tipo": 1},
            {"variavel": "@{armamento.marca}@", "descricao": "Marca de Armamento", "tipo": 1},
            {"variavel": "@{armamento.calibre}@", "descricao": "Calibre de Armamento", "tipo": 1},
            {"variavel": "@{armamento.tipo.arma}@", "descricao": "Tipo da Arma", "tipo": 1},
            {"variavel": "@{armamento.modelo.armamento}@", "descricao": "Modelo do Armamento", "tipo": 1},
            {"variavel": "@{armamento.quantidade}@", "descricao": "Quantidade ", "tipo": 1},
            {"variavel": "@{armamento.numero.serie}@", "descricao": "Número de Serie", "tipo": 1},
            {"variavel": "@{armamento.raspado}@", "descricao": "Raspado?", "tipo": 1},
            {"variavel": "@{armamento.institucional}@", "descricao": "Institucional?", "tipo": 1},
            {"variavel": "@{veiculo.tipo}@", "descricao": "Tipo de Veiculo", "tipo": 8},
            {"variavel": "@{veiculo.marca}@", "descricao": "Marca de Veiculo", "tipo": 8},
            {"variavel": "@{veiculo.modelo}@", "descricao": "Modelo de Veiculo", "tipo": 8},
            {"variavel": "@{veiculo.ano}@", "descricao": "Ano", "tipo": 8},
            {"variavel": "@{veiculo.placa.original}@", "descricao": "Placa Original", "tipo": 8},
            {"variavel": "@{veiculo.placa}@", "descricao": "Placa", "tipo": 8},
            {"variavel": "@{veiculo.proprietario}@", "descricao": "Proprietario", "tipo": 8},
            {"variavel": "@{veiculo.conduto}@", "descricao": "Condutor", "tipo": 8},
            {"variavel": "@{veiculo.categoria}@", "descricao": "Categoria", "tipo": 8},
            {"variavel": "@{veiculo.proprietario.cpf}@", "descricao": "Cpf do Proprietario", "tipo": 8},
            {"variavel": "@{veiculo.proprietario.rg}@", "descricao": "Rg do Proprietario", "tipo": 8},
            {"variavel": "@{veiculo.condutor.cpf}@", "descricao": "Cpf do Condutor", "tipo": 8},
            {"variavel": "@{veiculo.condutor.rg}@", "descricao": "Rg do Condutor", "tipo": 8},
            {"variavel": "@{veiculo.chassi}@", "descricao": "Chassi", "tipo": 8},
            {"variavel": "@{veiculo.numero.motor}@", "descricao": "Numero dr Motor", "tipo": 8},
            {"variavel": "@{veiculo.origem}@", "descricao": "Origem", "tipo": 8},
            {"variavel": "@{veiculo.orgao}@", "descricao": "Orgao", "tipo": 8},
            {"variavel": "@{veiculo.proprietario.condutor}@", "descricao": "Proprietario é Condutor?", "tipo": 8},
            {"variavel": "@{veiculo.modelo}@", "descricao": "Modelo", "tipo": 8},
            {"variavel": "@{veiculo.cor}@", "descricao": "Cor", "tipo": 8},
            {"variavel": "@{arquivo.descricao}@", "descricao": "Descrição", "tipo": 2},
            {"variavel": "@{arquivo.hash.tipo}@", "descricao": "Tipo de Hash", "tipo": 2},
            {"variavel": "@{arquivo.hash}@", "descricao": "Hash", "tipo": 2},
            {"variavel": "@{arquivo.quantidade}@", "descricao": "Quantidade", "tipo": 2},
            {"variavel": "@{arquivo.tamanho}@", "descricao": "Tamanho", "tipo": 2},
            {"variavel": "@{arquivo.capacidade.unidade}@", "descricao": "Unidade da Capacidade ", "tipo": 2},
            {"variavel": "@{arquivo.suporte.tipo}@", "descricao": "Tipo de Suporte", "tipo": 2},
            {"variavel": "@{arquivo.suporte.descricao}@", "descricao": "Descricao de Suporte", "tipo": 2},
            {"variavel": "@{imprepapilospica.impressao.tipo}@", "descricao": "Tipo de Impressão", "tipo": 5},
            {"variavel": "@{imprepapilospica.vucetich.classificacao}@", "descricao": "Classificação Vucetich", "tipo": 5},
            {"variavel": "@{imprepapilospica.origem.tipo}@", "descricao": "Tipo de Origem", "tipo": 5},
            {"variavel": "@{imprepapilospica.suporte.tipo}@", "descricao": "Tipo de Suporte", "tipo": 5},
            {"variavel": "@{imprepapilospica.hash.tipo}@", "descricao": "Tipo de Hash", "tipo": 5},
            {"variavel": "@{imprepapilospica.hash}@", "descricao": "Hash", "tipo": 5},
            {"variavel": "@{imprepapilospica.descricao}@", "descricao": "Descrição", "tipo": 5},
            {"variavel": "@{dispositivotec.tipo}@", "descricao": "Tipo de Dispositivo", "tipo": 3},
            {"variavel": "@{dispositivotec.fabricante}@", "descricao": "Fabricante do Dispositivo", "tipo": 3},
            {"variavel": "@{dispositivotec.modelo}@", "descricao": "Modelo do Dispositivo", "tipo": 3},
            {"variavel": "@{dispositivotec.imei}@", "descricao": "Imei do Dispositivo", "tipo": 3},
            {"variavel": "@{dispositivotec.unidade.capacidade}@", "descricao": "Unidade da Capacidade ", "tipo": 3},
            {"variavel": "@{dispositivotec.capacidade}@", "descricao": "Capacidade", "tipo": 3},
            {"variavel": "@{dispositivotec.numero.serie}@", "descricao": "Número de Serie", "tipo": 3},
            {"variavel": "@{dispositivotec.modelo}@", "descricao": "Modelo", "tipo": 3},
            {"variavel": "@{dispositivotec.cor}@", "descricao": "Cor", "tipo": 3},
            {"variavel": "@{material.tipo}@", "descricao": "Tipo de Material", "tipo": 6},
            {"variavel": "@{material.apresentacao}@", "descricao": "Apresentação", "tipo": 6},
            {"variavel": "@{material.cor}@", "descricao": "Cor", "tipo": 6},
            {"variavel": "@{material.quantidade}@", "descricao": "Quantidade", "tipo": 6},
            {"variavel": "@{material.unidade.medida}@", "descricao": "Unidade de Medida", "tipo": 6},
            {"variavel": "@{material.exame.quantidade.utilizada}@", "descricao": "Quantidade Utilizada no Exame", "tipo": 6},
            {"variavel": "@{material.exame.unidade.medida.utilizada}@", "descricao": "Unidade de Exame", "tipo": 6},
            {"variavel": "@{material.aliquotagem.quantidade.utilizada}@", "descricao": "Aliquotagem Utilizada", "tipo": 6},
            {"variavel": "@{material.aliquotagem.unidade.medida.utilizada}@", "descricao": "Unidade de Medida da Aliquotagem Utilizada", "tipo": 6},
            {"variavel": "@{material.proscrita.substancia}@", "descricao": "Substancia Proscrita", "tipo": 6},
            {"variavel": "@{documento.documento.tipo}@", "descricao": "Tipo de Documento", "tipo": 4},
            {"variavel": "@{documento.paginas}@", "descricao": "Paginas", "tipo": 4},
            {"variavel": "@{documento.folhas}@", "descricao": "Folhas", "tipo": 4},
            {"variavel": "@{documento.punho.flg.grafismo.original}@", "descricao": "Grafismo de Original Punho?", "tipo": 4},
            {"variavel": "@{documento.punho.paginas.grafismo.original}@", "descricao": "Paginas do Punho", "tipo": 4},
            {"variavel": "@{documento.observação}@", "descricao": "Observação", "tipo": 4},
            {"variavel": "@{objeto.descricao}@", "descricao": "Descrição", "tipo": 7}
        ]

        for dado in valores_padrao:
            obj, created = Variavel.objects.get_or_create(
                variavel=dado["variavel"],
                defaults={
                    "descricao": dado["descricao"],
                    "tipo": dado["tipo"]
                }
            )
                
        self.stdout.write(self.style.SUCCESS(f'Modelo Variável preenchido com sucesso.'))