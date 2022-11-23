
# Parseador de arquivos CNAB

O Objetivo deste projeto é realizar o parseamento de um arquivo .txt através de um upload do arquivo através de uma interface web. 
O aquivo parseado é armazenado em um banco de dados.


## Funcionalidades

- Upload de arquivos
- Parseamento de .txt para postgreSQL



## Stack utilizada

**Back-end:** Django


## Pré-Requisitos

- Python 3.0+
## Rodando localmente

#### Clone o projeto

```bash
  git clone git@github.com:devigorgarcia/teste-2-python-backend.git
```

#### Entre no diretório do projeto

```bash
  cd teste-2-python-backend
```

#### Instale as dependências

```bash
  python -m venv venv
```

#### Iniciando o ambiente virtual

- Powershell
```bash
  venv/Scripts/activate
```

- bash
```bash
  source venv/Scripts/activate
```

- Linux
```bash
  source venv/bin/activate
```

#### Instale as dependencias pip
```bash
  pip install -r requirements.txt
```

#### Rodando localmente
```bash
  python manage.py runserver
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`DB`

`DB_UER`

`DB_PASSWRD`

`DB_HST`

`DB_PRT`

