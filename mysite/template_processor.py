import re
from mysite.models import Variavel

class TemplateProcessor:
    def __init__(self, contexto):
        """
        :param contexto: Dicionário com os valores das variáveis para substituição
        """
        self.contexto = contexto

    def substituir_variaveis(self, texto):
        """
        Substitui variáveis no texto com base no contexto e remove a tag <span>.
        """
        padrao_variavel = re.compile(r'@\{(.*?)\}@')

        def substituir(match):
            chave = match.group(1)
            return str(self.contexto.get(chave, f'@{{{chave}}}@'))

        texto_sem_span = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', texto)

        return padrao_variavel.sub(substituir, texto_sem_span)

    @staticmethod
    def carregar_variaveis():
        """
        Carrega as variáveis do banco de dados (opcional, se quiser fazer substituições dinâmicas).
        """
        variaveis = Variavel.objects.all()
        return {var.variavel.strip('@{}'): var.descricao for var in variaveis}
