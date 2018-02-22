# test-tikal
Desafio realizado para a vaga de Desenvolvedor Python.

### Como executar?

Para este projeto é necessário a instalação do Redis, para isso utilize o passo-a-passo descrito neste [link](https://redis.io/topics/quickstart)

* Faça download ou clone o repositório
* Acesse a pasta do projeto
* Crie e ative o virtualenv
* Instale as dependências
* Execute o redis
* Execute o celery
* Execute os testes
* Execute o projeto


```bash
git clone git@bitbucket.org:izaguerreiro/test-tikal.git
cd test-tikal
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd tikal

# Em outro terminal execute
redis-server

# Em outro terminal execute (não se esqueça usar o venv tem que estar ativo)
celery --app=tikal worker --beat --loglevel=info

# Por fim
./manage.py test
./manage.py runserver
```

