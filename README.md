# Study.Async
Desenvolvido na Pystack Week 9.0, lecionado por Caio Sampaio.

## Descrição
O Study.Async é uma aplicação projetada para auxiliar usuários a estudar diferentes matérias e assuntos de forma interativa, utilizando flashcards. Os usuários podem criar, revisar e testar seus conhecimentos em diversos tópicos, enquanto o aplicativo monitora seu progresso.

## Funcionalidades Principais

1. **Adição de Flashcards**:
- Os usuários podem criar flashcards personalizados, incluindo uma pergunta e uma resposta associada.
2. **Desafios de Estudo**:
- Inicie desafios para testar seus conhecimentos em uma matéria específica, respondendo aos flashcards.
3. **Contador de Acertos e Erros**:
- Um contador na interface do desafio registra quantas respostas corretas e incorretas o usuário teve.
4. **Relatório de Desempenho**:
- Visualize um relatório gráfico que destaca o desempenho do usuário, mostrando a porcentagem de acertos e erros por matéria.

## Como Usar

Criar ambiente virtual
```Python
# Linux
python3 -m venv venv
```
```Python
# Windows
python -m venv venv
```

Após a criação do venv vamos ativa-lo:
```Python
# Linux
source venv/bin/activate
```
```Python
# Windows
venv\Scripts\Activate
```
Caso algum comando retorne um erro de permissão execute o código e tente novamente:
```Python
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Agora vamos fazer a instalação do Django e as demais bibliotecas:
```Python
pip install django
pip install pillow
```

Rode o servidor para testar:
```Python
python manage.py runserver
```

## Acessar as URLs e a área admin
Crie um super usuário:
```Python
python manage.py createsuperuser
```

Faça as migrações da tabela pro banco de dados:
```Python
python manage.py migrate
```

Com o servidor rodando, entre na área admin:

localhost:8000/**admin** <- adicionando

Agora você tem acesso as tabelas!


⚠ Em desenvolvimento
