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