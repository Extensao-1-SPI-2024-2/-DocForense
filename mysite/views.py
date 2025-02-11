import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .services import GalileuAPIService
from .services import WordFileGenerator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Modelo, ModeloVestigio, Variavel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .template_processor import TemplateProcessor
from .contexto_procedimento_pericial import ContextoProcedimentoPericial
from datetime import datetime

@login_required(login_url='/login')
def procedimento_pericial(request, id):
    if request.method == 'GET':
        service = GalileuAPIService()
        response_data = service.get_procedimento_pericial(id)

        if 'error' in response_data:
            return JsonResponse({'status': 'error', 'message': response_data['error']}, status=500)
        
        return JsonResponse({'status': 'success', 'data': response_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@login_required(login_url='/login')
def gerar_arquivo_word_teste(request):
    
    data = {
        'title': 'Laudo Exemplo',
        'sections': {
            'Seção 1': 'Texto da seção 1.',
            'Seção 2': 'Texto da seção 2.',
        },
    }

    file_buffer = WordFileGenerator.generate_word_file_test(data)

    response = HttpResponse(
        file_buffer,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename="relatorio.docx"'

    return response


def logininternal(request):
    if request.method == 'GET':
        if 'logged_in' in request.session and request.session['logged_in']:
            return redirect('/')
        
    if request.method == 'POST':
        user, created = User.objects.get_or_create(
            username='admindoc1',
            defaults={
                'email': 'admin@docforense.com.br',
                'first_name': 'Master',
                'last_name': 'Administrador',
            }
        )

        if created:
            user.set_password('admindoc1')
            user.save()

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['logged_in'] = True
            request.session['login'] = username
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'login.html')

@login_required(login_url='/login')
def index(request):
    if request.method == 'GET':
        if not request.session.get('logged_in', False):
            messages.error(request, "É necessário realizar o login.")
            return redirect('/login')
    
    return render(request, 'index.html')

@login_required(login_url='/login')
def logoutinternal(request):
    request.session.pop('logged_in', None)
    request.session.pop('login', None)
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def create_modelo(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        value = request.POST.get('value')
        type =  request.POST.get('type')

        if not all([name, value, type]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('/modelo/laudo/criar')
        
        try:
            Modelo.objects.create(
                name=name,
                value=value,
                type=type,
                user_inclusion=request.user
            )

            messages.success(request, "Modelo criado com sucesso!")
            return redirect('/modelo/laudo/listagem')
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado")
            return redirect('/modelo/laudo/criar')
        except Exception as e:
            messages.error(request, f"Erro: {str(e)}")
            return redirect('/modelo/laudo/criar')
        
    variaveis = Variavel.objects.filter(tipo=0).values('variavel', 'descricao')
    
    return render(request, 'modelo.html', {
        'type_choices': ModeloVestigio.TYPE_CHOICES,
        'variaveis': json.dumps(list(variaveis)),
    })

@login_required(login_url='/login')
def create_modelo_vestigio(request, type):
    tipo_descricao = next((desc for value, desc in Variavel.TIPO_CHOICES if value == type), None)

    if not tipo_descricao:
        messages.error(request, "Esse tipo de vestígio não foi encontrado.")
        return redirect('/modelo/vestigio/listagem')
    
    if request.method == 'POST':
        
        name = request.POST.get('name')
        value = request.POST.get('value')
        type_view =  request.POST.get('type')

        if not all([name, value, type_view]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('/modelo/vestigio/criar')
        
        try:
            ModeloVestigio.objects.create(
                name=name,
                value=value,
                type=type_view,
                type_vestigio=type,
                user_inclusion=request.user
            )

            messages.success(request, "Modelo de vestígio criado com sucesso!")
            return redirect('/modelo/vestigio/listagem')
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado")
            return redirect('/modelo/vestigio/criar')
        except Exception as e:
            messages.error(request, f"Erro: {str(e)}")
            return redirect('/modelo/vestigio/criar')
    
    variaveis = Variavel.objects.filter(tipo=type).values('variavel', 'descricao')
        
    return render(request, 'modelo_vestigio.html', {
        'variaveis': json.dumps(list(variaveis)),
        'tipo': type,
        'tipo_descricao': tipo_descricao,
        'type_choices': ModeloVestigio.TYPE_CHOICES
    })

@login_required(login_url='/login')
def listagem(request):
    if request.method == 'GET':
        if not request.session.get('logged_in', False):
            messages.error(request, "É necessário realizar o login.")
            return redirect('/login')
    
    modelos = Modelo.objects.all()

    return render(request, 'listagem.html', {'modelos': modelos})

@login_required(login_url='/login')
def listagemVestigio(request):
    if request.method == 'GET':
        if not request.session.get('logged_in', False):
            messages.error(request, "É necessário realizar o login.")
            return redirect('/login')
    
    modelos = ModeloVestigio.objects.all()

    return render(request, 'listagem_vestigio.html', {
        'modelos': modelos
    })

@login_required(login_url='/login')
def editar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        type_view =  request.POST.get('type')

        if not all([name, value, type_view]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect(f'/modelo/laudo/editar/{modelo_id}')

        try:
            modelo.name = name
            modelo.value = value
            modelo.type = type_view
            modelo.save()

            messages.success(request, "Modelo atualizado com sucesso!")
            return redirect('/modelo/laudo/listagem')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar o modelo: {str(e)}")
            return redirect(f'/modelo/laudo/editar/{modelo_id}')
    
    variaveis = Variavel.objects.filter(tipo=0).values('variavel', 'descricao')
    return render(request, 'modelo_edicao.html', {
        'variaveis': json.dumps(list(variaveis)),
        'modelo': modelo, 
        'readonly': False,
        'type_choices': ModeloVestigio.TYPE_CHOICES,
    })

@login_required(login_url='/login')
def editar_modelo_vestigio(request, modelo_id):
    modelo = get_object_or_404(ModeloVestigio, id=modelo_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        type_view =  request.POST.get('type')

        if not all([name, value, type_view]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect(f'/modelo/vestigio/editar/{modelo_id}')

        try:
            modelo.name = name
            modelo.value = value
            modelo.type = type_view
            modelo.save()

            messages.success(request, "Modelo de Vestígio atualizado com sucesso!")
            return redirect('/modelo/vestigio/listagem')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar o modelo de vestígio: {str(e)}")
            return redirect(f'/modelo/vestigio/editar/{modelo_id}')
        
    variaveis = Variavel.objects.filter(tipo=modelo.type_vestigio).values('variavel', 'descricao')
    
    return render(request, 'modelo_vestigio_edicao.html', {
        'modelo': modelo, 
        'readonly': False,
        'variaveis': json.dumps(list(variaveis)),
        'tipo': modelo.type_vestigio,
        'type_choices': ModeloVestigio.TYPE_CHOICES,
        'tipo_descricao': modelo.get_type_vestigio_display()
    })

@login_required(login_url='/login')
def visualizar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)
    return render(request, 'modelo_edicao.html', {
        'modelo': modelo, 
        'readonly': True,
        'type_choices': ModeloVestigio.TYPE_CHOICES,
    })
    
@login_required(login_url='/login')
def visualizar_modelo_vestigio(request, modelo_id):
    modelo = get_object_or_404(ModeloVestigio, id=modelo_id)
    return render(request, 'modelo_vestigio_edicao.html', {
        'modelo': modelo, 
        'readonly': True,
        'type_choices': ModeloVestigio.TYPE_CHOICES,
        'tipo_descricao': modelo.get_type_vestigio_display()
    })

@login_required(login_url='/login')
def deletar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)
    
    try:
        modelo.delete()
        messages.success(request, "Modelo deletado com sucesso!")
    except Exception as e:
        messages.error(request, f"Erro ao deletar o modelo: {str(e)}")
    
    return redirect('/modelo/laudo/listagem')

@login_required(login_url='/login')
def deletar_modelo_vestigio(request, modelo_id):
    modelo = get_object_or_404(ModeloVestigio, id=modelo_id)
    
    try:
        modelo.delete()
        messages.success(request, "Modelo de Vestígio deletado com sucesso!")
    except Exception as e:
        messages.error(request, f"Erro ao deletar o modelo de vestígio: {str(e)}")
    
    return redirect('/modelo/vestigio/listagem')

@login_required(login_url='/login')
def gerar_laudo(request):
    modelos = Modelo.objects.all()
    return render(request, 'gerar_laudo.html', {'modelos': modelos})

def converter_timestamp_para_data_brasileira(timestamp_ms):
    if timestamp_ms is None:
        return None
    
    timestamp = timestamp_ms / 1000
    
    dt = datetime.fromtimestamp(timestamp)
    
    return dt.strftime('%d/%m/%Y %H:%M:%S')

@login_required(login_url='/login')
def gerar_modelo_formatado(request, galileu_id, modelo_id):
    if request.method == 'GET':
        
        service = GalileuAPIService()
        response_data = service.get_procedimento_pericial(galileu_id)

        if 'error' in response_data:
            return JsonResponse({'status': 'error', 'message': response_data['error']}, status=500)
        
        contexto = ContextoProcedimentoPericial(response_data).gerar_contexto()
        
        modelo = get_object_or_404(Modelo, id=modelo_id)
        
        processor = TemplateProcessor(contexto)
        text = processor.substituir_variaveis(modelo.value)
        
        return JsonResponse({'status': 'success', 'data': {
            "text": text
        }})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)