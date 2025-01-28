from django.http import JsonResponse
from .services import GalileuAPIService
from .services import WordFileGenerator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Modelo
from django.contrib.auth.models import User

def procedimento_pericial(request, id):
    if request.method == 'GET':
        service = GalileuAPIService()
        response_data = service.get_procedimento_pericial(id)

        if 'error' in response_data:
            return JsonResponse({'status': 'error', 'message': response_data['error']}, status=500)
        
        return JsonResponse({'status': 'success', 'data': response_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
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

from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'GET':
        if 'logged_in' in request.session and request.session['logged_in']:
            return redirect('/')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # TODO Por enquanto temos somente esse admin hardcode até recebemos a comunicação do Galileu
        if username == 'admin' and password == 'admin':
            request.session['logged_in'] = True
            request.session['login'] = request.POST.get('username')
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'login.html')

def index(request):
    if request.method == 'GET':
        if not request.session.get('logged_in', False):
            messages.error(request, "É necessário realizar o login.")
            return redirect('/login')
    
    return render(request, 'index.html')

def logout(request):
    request.session.pop('logged_in', None)
    request.session.pop('login', None)
    return redirect('/login')

def create_modelo(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        value = request.POST.get('value')
        #user_id = request.POST.get('user_id')

        if not all([name, value]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('/modelo/criar')
        
        try:
            #user = User.objects.get(id=user_id)
            
            #criando usuário ao vivo enquanto não tem sessao
            user, created = User.objects.get_or_create(
                username='usuario_teste',
                defaults={
                    'password': 'senha123',
                    'email': 'teste@exemplo.com',
                    'first_name': 'Teste',
                    'last_name': 'Usuário',
                }
            )

            Modelo.objects.create(
                name=name,
                value=value,
                user_inclusion=user
            )

            messages.success(request, "Modelo criado com sucesso!")
            return redirect('/modelo/listagem')
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado")
            return redirect('/modelo/criar')
        except Exception as e:
            messages.error(request, f"Erro: {str(e)}")
            return redirect('/modelo/criar')
        
    return render(request, 'modelo.html')

def listagem(request):
    if request.method == 'GET':
        if not request.session.get('logged_in', False):
            messages.error(request, "É necessário realizar o login.")
            return redirect('/login')
    
    modelos = Modelo.objects.all()

    return render(request, 'listagem.html', {'modelos': modelos})

def editar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')

        if not all([name, value]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect(f'/modelo/editar/{modelo_id}')

        try:
            modelo.name = name
            modelo.value = value
            modelo.save()

            messages.success(request, "Modelo atualizado com sucesso!")
            return redirect('/modelo/listagem')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar o modelo: {str(e)}")
            return redirect(f'/modelo/editar/{modelo_id}')
    
    return render(request, 'modelo_edicao.html', {'modelo': modelo, 'readonly': False})

def visualizar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)
    return render(request, 'modelo_edicao.html', {'modelo': modelo, 'readonly': True})

def deletar_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, id=modelo_id)
    
    try:
        modelo.delete()
        messages.success(request, "Modelo deletado com sucesso!")
    except Exception as e:
        messages.error(request, f"Erro ao deletar o modelo: {str(e)}")
    
    return redirect('/modelo/listagem')