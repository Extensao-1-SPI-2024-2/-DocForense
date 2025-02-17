from datetime import datetime

def converter_timestamp_para_data_brasileira(timestamp_ms):
    if not timestamp_ms or timestamp_ms in ["xxxxx", ""]:
        return "xxxxx"

    try:
        timestamp_ms = int(timestamp_ms)
        return datetime.fromtimestamp(timestamp_ms / 1000).strftime('%d/%m/%Y %H:%M:%S')
    except (ValueError, TypeError):
        return "xxxxx" 


class ContextoProcedimentoPericial:
    def __init__(self, dados):
        self.dados = dados or {}
        self.solicitacao = self.dados.get('solicitacaoOcorrencia') or {}
        self.perito = self.solicitacao.get('peritoResponsavelLocal') or {}
        self.setor = self.dados.get('setor') or {}
        self.documento = self.dados.get('documentoProcedimentoPericial') or {}
        self.documento_setor = self.documento.get('setor') or {}
        self.tipo_documento = self.documento.get('tipoDocumento') or {}
        self.laudo = self.dados.get('laudo') or {}
        self.solicitacao_setor_acionamento = self.solicitacao.get('setorAcionamento') or {}
        self.solicitacao_municipio = self.solicitacao.get('municipio') or {}
        self.solicitacao_perito = self.solicitacao.get('peritoResponsavelLocal') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        return {
            'protocolo': self.obter_valor(self.dados.get('protocolo')),
            'perito.nome': self.obter_valor(self.perito.get('nome')),
            'perito.cpf': self.obter_valor(self.perito.get('cpf')),
            'perito.matricula': self.obter_valor(self.perito.get('matricula')),
            'perito.cargo': self.obter_valor(self.perito.get('cargo')),
            'dataEntrada': self.obter_timestamp(self.dados.get('dataEntrada')),
            'setorId': self.obter_valor(self.setor.get('id')),
            'setorDescricao': self.obter_valor(self.setor.get('descricao')),
            'setorDescricaoCompleta': self.obter_valor(self.setor.get('descricaoCompleta')),
            'documentoProcedimentoPericialId': self.obter_valor(self.documento.get('id')),
            'documentoProcedimentoPericialDataInclusao': self.obter_timestamp(self.documento.get('dataInclusao')),
            'documentoProcedimentoPericialNumero': self.obter_valor(self.documento.get('numero')),
            'documentoProcedimentoPericialAno': self.obter_valor(self.documento.get('ano')),
            'documentoProcedimentoPericialTipoDocumentoId': self.obter_valor(self.tipo_documento.get('id')),
            'documentoProcedimentoPericialTipoDocumentoDescricao': self.obter_valor(self.tipo_documento.get('descricao')),
            'documentoProcedimentoPericialTipoDocumentoAbreviatura': self.obter_valor(self.tipo_documento.get('abreviatura')),
            'laudo.dataInclusao': self.obter_timestamp(self.laudo.get('dataInclusao')),
            'laudo.numeroCompleto': self.obter_valor(self.laudo.get('numeroCompleto')),
            'solicitacaoOcorrenciaId': self.obter_valor(self.solicitacao.get('id')),
            'solicitacaoOcorrenciaSetorAcionamentoId': self.obter_valor(self.solicitacao_setor_acionamento.get('id')),
            'solicitacaoOcorrenciaSetorAcionamentoDescricao': self.obter_valor(self.solicitacao_setor_acionamento.get('descricao')),
            'solicitacaoOcorrenciaMunicipioDescricao': self.obter_valor(self.solicitacao_municipio.get('descricao')),
            'solicitacaoOcorrenciaDataInclusao': self.obter_timestamp(self.solicitacao.get('dataInclusao')),
            'solicitacaoOcorrenciaDataFinalizacao': self.obter_timestamp(self.solicitacao.get('dataFinalizacao')),
            'solicitacaoOcorrenciaLatitude': self.obter_valor(self.solicitacao.get('latitude')),
            'solicitacaoOcorrenciaLongitude': self.obter_valor(self.solicitacao.get('longitude')),
            'solicitacaoOcorrenciaDataHoraOcorrencia': self.obter_timestamp(self.solicitacao.get('dataHoraOcorrencia')),
            'solicitacaoOcorrenciaDataHoraAtendimentoPerito': self.obter_timestamp(self.solicitacao.get('dataHoraAtendimentoPerito')),
            'solicitacaoOcorrenciaDataHoraLiberacaoLocal': self.obter_timestamp(self.solicitacao.get('dataHoraLiberacaoLocal')),
            'solicitacaoOcorrenciaDataHoraMorte': self.obter_timestamp(self.solicitacao.get('dataHoraMorte')),
            'solicitacaoOcorrenciaLocalMorte': self.obter_valor(self.solicitacao.get('localMorte')),
            'solicitacaoPeritoNome': self.obter_valor(self.solicitacao_perito.get('nome')),
            'solicitacaoPeritoCpf': self.obter_valor(self.solicitacao_perito.get('cpf')),
            'solicitacaoPeritoMatricula': self.obter_valor(self.solicitacao_perito.get('matricula')),
            'solicitacaoPeritoCargo': self.obter_valor(self.solicitacao_perito.get('cargo')),
            'solicitacaoOcorrenciaDataAcionamento': self.obter_timestamp(self.solicitacao.get('dataAcionamento')),
            'solicitacaoOcorrenciaBairro': self.obter_valor(self.solicitacao.get('bairro')),
            'solicitacaoOcorrenciaDescricaoLogradouro': self.obter_valor(self.solicitacao.get('descricaoLogradouro')),
            'solicitacaoOcorrenciaObservacao': self.obter_valor(self.solicitacao.get('observacao')),
            'solicitacaoOcorrenciaTipoAcionamento': self.obter_valor(self.solicitacao.get('tipoAcionamento')),
            'documentoProcedimentoPericialAutoridadeRequisitante': self.documento.get('autoridadeRequisitante'),
            'documentoProcedimentoPericialSgd': self.obter_valor(self.documento.get('sgd')),
            'documentoProcedimentoPericialSetorId': self.obter_valor(self.documento_setor.get('id', "xxxxx")),
            'documentoProcedimentoPericialSetorDesc': self.obter_valor(self.documento_setor.get('descricao', "xxxxx")),
            'documentoProcedimentoPericialSetorDescComplet': self.documento_setor.get('descricaoCompleta', "xxxxx"),
            'laudo.dataEntrega': self.obter_valor(self.obter_timestamp(self.laudo.get('dataEntrega', "xxxxx"))),
            'laudo.sgdEntrega': self.obter_valor(self.laudo.get('sgdEntrega', "xxxxx")),
            'solicitacaoOcorrenciaSetorAcionamentoDescComplet': self.obter_valor(self.solicitacao_setor_acionamento.get('descricaoCompleta', "xxxxx")),
            'solicitacaoOcorrenciaMunicipioId': self.obter_valor(self.solicitacao_setor_acionamento.get('id', "xxxxx")),
            'solicitacaoOcorrenciaNumeroLogradouro': self.obter_valor(self.solicitacao.get('numeroLogradouro')),
            'solicitacaoOcorrenciaComplementoLogradouro': self.obter_valor(self.solicitacao.get('complementoLogradouro')),
        }
    
class ContextoProcedimentoPericialMateria:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'material.tipo': self.obter_valor(self.dados.get('evidenciaMaterialTipo')),
            'material.apresentacao': self.obter_valor(self.dados.get('evidenciaMaterialApresentacao')),
            'material.cor': self.obter_valor(self.dados.get('cor')),
            'material.quantidade': self.obter_valor(self.dados.get('quantidade')),
            'material.unidade.medida': self.obter_valor(self.dados.get('unidadeMedida')),
            'material.exame.quantidade.utilizada': self.obter_valor(self.dados.get('quantidadeUtilizadaExame')),
            'material.exame.unidade.medida.utilizada': self.obter_valor(self.dados.get('unidadeMedidaUtilizadaExame')),
            'material.aliquotagem.quantidade.utilizada': self.obter_valor(self.dados.get('quantidadeUtilizadaAliquotagem')),
            'material.aliquotagem.unidade.medida.utilizada': self.obter_valor(self.dados.get('unidadeMedidaUtilizadaAliquotagem')),
            'material.proscrita.substancia': self.obter_valor(self.dados.get('substanciaProscrita'))
        }
    
class ContextoProcedimentoPericialArmamento:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'armamento.tipo': self.obter_valor(self.dados.get('evidenciaArmamentoTipo')),
            'armamento.modelo': self.obter_valor(self.dados.get('evidenciaArmamentoModelo')),
            'armamento.marca': self.obter_valor(self.dados.get('evidenciaArmamentoMarca')),
            'armamento.calibre': self.obter_valor(self.dados.get('evidenciaArmamentoCalibre')),
            'armamento.tipo.arma': self.obter_valor(self.dados.get('unidadeMedida')),
            'armamento.modelo.armamento': self.obter_valor(self.dados.get('modeloArmamento')),
            'armamento.quantidade': self.obter_valor(self.dados.get('quantidade')),
            'armamento.numero.serie': self.obter_valor(self.dados.get('numeroSerie')),
            'armamento.raspado': self.obter_valor(self.dados.get('raspado')),
            'armamento.institucional': self.obter_valor(self.dados.get('institucional'))
        }
    
class ContextoProcedimentoPericialObjeto:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'objeto.descricao': self.obter_valor(self.dados.get('descricao')),
        }
    
class ContextoProcedimentoPericialDispositivo:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'dispositivotec.tipo': self.obter_valor(self.dados.get('evidenciaDispositivoTecnologicoTipo')),
            'dispositivotec.fabricante': self.obter_valor(self.dados.get('evidenciaDispositivoTecnologicoFabricante')),
            'dispositivotec.modelo': self.obter_valor(self.dados.get('evidenciaDispositivoTecnologicoModelo')),
            'dispositivotec.imei': self.obter_valor(self.dados.get('xxxxxxx')), #TODO ver esse caso aqui, é um array
            'dispositivotec.unidade.capacidade': self.obter_valor(self.dados.get('capacidadeUnidade')),
            'dispositivotec.capacidade': self.obter_valor(self.dados.get('capacidade')),
            'dispositivotec.numero.serie': self.obter_valor(self.dados.get('numeroSerie')),
            'dispositivotec.modelo': self.obter_valor(self.dados.get('modelo')),
            'dispositivotec.cor': self.obter_valor(self.dados.get('cor'))
        }
    
class ContextoProcedimentoPericialDocumento:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'documento.documento.tipo': self.obter_valor(self.dados.get('evidenciaDocumentoTipo')),
            'documento.paginas': self.obter_valor(self.dados.get('paginas')),
            'documento.folhas': self.obter_valor(self.dados.get('folhas')),
            'documento.punho.flg.grafismo.original': self.obter_valor(self.dados.get('flgGrafismoOriginalPunho')),
            'documento.punho.paginas.grafismo.original': self.obter_valor(self.dados.get('paginasGrafismoOriginalPunho')),
            'documento.observação': self.obter_valor(self.dados.get('observacao'))
        }
    
class ContextoProcedimentoPericialVeiculo:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'veiculo.tipo': self.obter_valor(self.dados.get('evidenciaVeiculoTipo')),
            'veiculo.marca': self.obter_valor(self.dados.get('evidenciaVeiculoMarca')),
            'veiculo.modelo': self.obter_valor(self.dados.get('evidenciaVeiculoModelo')),
            'veiculo.ano': self.obter_valor(self.dados.get('ano')),
            'veiculo.placa.original': self.obter_valor(self.dados.get('placaOriginal')),
            'veiculo.placa': self.obter_valor(self.dados.get('placa')),
            'veiculo.proprietario': self.obter_valor(self.dados.get('proprietario')),
            'veiculo.conduto': self.obter_valor(self.dados.get('condutor')),
            'veiculo.categoria': self.obter_valor(self.dados.get('categoria')),
            'veiculo.proprietario.cpf': self.obter_valor(self.dados.get('proprietarioCpf')),
            'veiculo.proprietario.rg': self.obter_valor(self.dados.get('proprietarioRg')),
            'veiculo.condutor.cpf': self.obter_valor(self.dados.get('condutorCpf')),
            'veiculo.condutor.rg': self.obter_valor(self.dados.get('condutorRg')),
            'veiculo.chassi': self.obter_valor(self.dados.get('chassi')),
            'veiculo.numero.motor': self.obter_valor(self.dados.get('numeroMotor')),
            'veiculo.origem': self.obter_valor(self.dados.get('origem')),
            'veiculo.orgao': self.obter_valor(self.dados.get('orgao')),
            'veiculo.proprietario.condutor': self.obter_valor(self.dados.get('proprietarioCondutor')),
            'veiculo.modelo.gerar': self.obter_valor(self.dados.get('modelo')),
            'veiculo.cor': self.obter_valor(self.dados.get('cor'))
        }
    
class ContextoProcedimentoPericialArquivo:
    def __init__(self, dados):
        self.dados = dados.get('dadosVestigio') or {}

    def obter_valor(self, caminho, padrao="xxxxx"):
        return caminho if caminho not in [None, ""] else padrao

    def obter_timestamp(self, caminho, padrao="xxxxx"):
        return converter_timestamp_para_data_brasileira(caminho) if caminho not in [None, ""] else padrao

    def gerar_contexto(self):
        
        print(self.dados)
        return {
            'arquivo.descricao': self.obter_valor(self.dados.get('descricaoArquivo')),
            'arquivo.hash.tipo': self.obter_valor(self.dados.get('funcaoHash')),
            'arquivo.hash': self.obter_valor(self.dados.get('hash')),
            'arquivo.quantidade': self.obter_valor(self.dados.get('quantidadeArquivo')),
            'arquivo.tamanho': self.obter_valor(self.dados.get('tamanhoArquivo')),
            'arquivo.capacidade.unidade': self.obter_valor(self.dados.get('capacidadeUnidade')),
            'arquivo.suporte.tipo': self.obter_valor(self.dados.get('tipoSuporte')),
            'arquivo.suporte.descricao': self.obter_valor(self.dados.get('descricaoSuporte'))
        }