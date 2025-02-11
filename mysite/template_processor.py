from bs4 import BeautifulSoup
import re
from mysite.models import Variavel
from .models import ModeloVestigio, Variavel
from django.shortcuts import get_object_or_404

class TemplateProcessor:
    def __init__(self, contexto):
        self.contexto = contexto

    def substituir_variaveis(self, texto):
        padrao_variavel = re.compile(r'@\{(.*?)\}@')

        def substituir(match):
            chave = match.group(1)
            return str(self.contexto.get(chave, f'@{{{chave}}}@'))

        texto_sem_span = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', texto)

        return padrao_variavel.sub(substituir, texto_sem_span)

    @staticmethod
    def carregar_variaveis():
        variaveis = Variavel.objects.all()
        return {var.variavel.strip('@{}'): var.descricao for var in variaveis}
    
    
    def processar_vestigios(self, html, data = {}):
        soup = BeautifulSoup(html, "html.parser")

        padrao = re.compile(r"@{vestigio\.(\d+)}@")
        
        vestigios = data.get('listaVestigio') or []

        for span in soup.find_all("span", class_="merge-tag-vestigio"):
            match = padrao.search(span.text)
            if match:
                
                modelo_vestigio = get_object_or_404(ModeloVestigio, id=match.group(1))
                
                novo_conteudo = ""
                
                if modelo_vestigio.type_vestigio == 1:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "ARMAMENTO"]
                    novo_conteudo = TemplateProcessor.vestigio_armamento(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 2:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "ARQUIVO"]
                    novo_conteudo = TemplateProcessor.vestigio_arquivo(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 3:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "DISPOSITIVO_TECNOLOGICO"] #conferido
                    novo_conteudo = TemplateProcessor.vestigio_dispositivo(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 4:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "DOCUMENTO"] #conferido
                    novo_conteudo = TemplateProcessor.vestigio_documento(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 5:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "IMPRESSAO"]
                    novo_conteudo = TemplateProcessor.vestigio_impressao(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 6:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"].startswith("MATERIAL")] #conferido
                    novo_conteudo = TemplateProcessor.vestigio_material(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 7:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "OBJETO"] #conferido
                    novo_conteudo = TemplateProcessor.vestigio_objeto(modelo_vestigio.value, dadosVestigios)
                    
                if modelo_vestigio.type_vestigio == 8:
                    dadosVestigios = [vestigio for vestigio in vestigios if vestigio["tipoEvidencia"] == "VEICULO"] #conferido
                    novo_conteudo = TemplateProcessor.vestigio_veiculo(modelo_vestigio.value, dadosVestigios)
                    

                span.replace_with(novo_conteudo)

        return str(soup)
    
    def vestigio_armamento(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()

    def vestigio_arquivo(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()
    
    def vestigio_dispositivo(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()
    
    def vestigio_documento(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()
    
    def vestigio_impressao(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()
    
    def vestigio_material(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result
    
    def vestigio_objeto(text, dadosVestigios):
        result = ""
    
        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()
    
    def vestigio_veiculo(text, dadosVestigios):
        result = ""

        for vestigio in dadosVestigios:
            result += text
    
        return result.strip()