# DocForense

Uma ferramenta que facilita a confecção de laudos periciais.

Desenvolvida por alunos da matéria Extensão 1 do curso de Sistemas para Internet do Instituto Federal do Tocantins, campus Palmas.

# 🚀 Instalação

Essas instruções permitirão que você execute a aplicação no seu computador.

# 📋 Pré-requisitos

Os seguintes requisitos devem estar instalados na sua máquina:

* **Python** - *3.13.0* - [Acessar](https://www.python.org/downloads/)
* **Django** - *5.1.2* - [Acessar](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release)
* **PIP** - *1.3* - [Acessar](https://pypi.org/project/pip/)

# 📦 Implantação

Primeiramente, deve ser instalado o módulo mysql correspondente

```
> pip install pymysql
```

Para inicar o tratamento de dados básicos do DB, deve ser gerado as migrations criadas no módulo mysite

```
> python manage.py migrate mysite
```

Após isso, as migrations devem ser executadas (lembrando que o banco de dados deve estar instalado e sendo executado conforme configurações do arquivo settings.py do módulo mysite)

```
> python manage.py migrate
```

Após isso, as seeds devem ser executadas (após a execução com sucesso das migrations)

```
> python manage.py migrate
```

Com isso, todas as tabelas devem ser devidamente criadas no banco de dados fornecido ao projeto. Logo em seguida, a aplicação deve ser executada na porta 8000 com o seguinte comando

```
> py manage.py runserver
```

Para instalar o módulo responsável por request a API externas

```
> pip install requests
```

Para instalar o módulo responsável por variaveis de ambiente

```
> pip install python-decouple
```

Para instalar o módulo responsável por gerar o arquivo word

```
> pip install python-docx
```

# Guia para o desenvolvedor

Este é o guia destinado aos desenvolvedores que estarão contribuindo com o desenvolvimento deste projeto.

## Sumário

1. [Workflow do Repositório](#workflow-do-repositório)
2. [Estratégia de Branching](#estratégia-de-branching)
3. [Criando uma Nova Branch](#criando-uma-nova-branch)
4. [Padronização de Commits](#padronização-de-commits)
5. [Criando um Merge Request](#criando-um-merge-request)
6. [Documentação](#documentação)

## Workflow do Repositório

Nosso repositório segue um fluxo baseado no Git flow com duas branches principais:
- **`main`**: A branch estável pronta para produção.
- **`develop`**: A branch de integração, onde as novas funcionalidades e correções são mescladas antes de serem lançadas.

Por favor, **sempre trabalhe na branch `develop`** e **nunca mescle diretamente em `main`**.

## Estratégia de Branching

1. **Branch Principal**: 
   - `main` deve sempre conter o código estável e pronto para produção.
   - O código em `main` deve ser testado, confiável e pronto para ser implantado.

2. **Branch de Desenvolvimento**: 
   - `develop` contém o trabalho de desenvolvimento em andamento.
   - Ao iniciar novas funcionalidades ou correções, sempre crie uma branch a partir de `develop`.

3. **Branches de Funcionalidade**: 
   - As branches de funcionalidade devem ser nomeadas como `feature/descrição-curta` ou `bugfix/descrição-curta`.
   - Exemplo: `feature/autenticacao-usuario`, `bugfix/corrigir-erro-login`.
   - Nunca trabalhe diretamente nas branches `main` ou `develop`.

## Criando uma Nova Branch

Ao trabalhar em novas funcionalidades ou correções:

1. Certifique-se de que seu repositório local está atualizado com a branch `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. Crie uma nova branch a partir de `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nome-da-sua-branch
   ```

3. Após concluir as alterações, faça o commit:
   ```bash
   git add .
   git commit -m "Descrição breve das suas alterações"
   ```

4. Faça o push da sua branch para o repositório remoto:
   ```bash
   git push origin feature/nome-da-sua-branch
   ```

## Padronização de Commits

- Use **mensagens de commit claras e concisas**.
- Siga o formato:
  ```
  [Tipo]: [Descrição curta da alteração]
  ```
  Exemplo:
  ```
  feat: adicionar formulário de login na homepage
  fix: resolver problema de tempo de sessão
  docs: atualizar README com novas instruções de configuração
  ```

- Mantenha a primeira linha da mensagem de commit com menos de 50 caracteres.
- Use o corpo da mensagem para explicações mais detalhadas (se necessário).

## Criando um Merge Request

1. **Sempre direcione o MR para a branch `develop`**, nunca para `main`.
2. Inclua uma descrição detalhada das alterações no campo de descrição do MR, seguindo o modelo apresentado.

## Revisões de Código

- As revisões de código são obrigatórias para todos os MRs antes de serem mesclados.
- Os revisores devem garantir que:
  - O código esteja bem documentado e siga as convenções de estilo do projeto.
  - Testes foram incluídos (se aplicável).
  - Não há erros óbvios ou problemas de desempenho.
  - A descrição do MR explique claramente as alterações e forneça links para problemas relacionados.
- Ao revisar um MR, adicione comentários ou aprove-o se tudo estiver correto.

## Documentação

- Todas as novas funcionalidades ou alterações devem ser devidamente documentadas.
- Atualize o `README.md` se necessário ou adicione nova documentação na pasta `docs/`.
- Sempre assegure-se de que sua documentação seja clara e fácil de entender para outros desenvolvedores.

Obrigado por contribuir para o DocForense!