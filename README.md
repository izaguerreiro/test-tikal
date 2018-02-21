# test-tikal
Desafio realizado para a vaga de Desenvolvedor Python.

### Como executar?

* Abra um terminal
* Instale o rabbitmq-server
* Execute o rabbitmq-server

```
sudo apt-get install rabbitmq-server
sudo rabbitmq-server deattach
```

* Em outro terminal
* Faça download ou clone o repositório
* Acesse a pasta do projeto
* Crie e ative o virtualenv
* Instale as dependências
* Execute os testes
* Execute o celery

```
git clone git@bitbucket.org:izaguerreiro/test-tikal.git
cd test-tikal
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sudo apt-get install rabbitmq-server
./manage.py test
celery 
celery --app=celerytest worker --beat --loglevel=info
```

* Abra outro terminal
* Acesse a pasta do projeto
* Ative o virtualenv
* Execute o projeto

```
cd test-tikal
python -m venv .venv
source .venv/bin/activate
./manage.py runserver
```

