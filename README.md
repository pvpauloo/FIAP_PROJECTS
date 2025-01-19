# FIAP Tech Challenge 1 - API EMBRAPA Vinicultura

Este projeto foi desenvolvido como parte de um desafio técnico em Machine Learning Engineering e tem como objetivo disponibilizar, por meio de uma API pública, dados de viticultura divulgados pela EMBRAPA, acessíveis no site VitiBrasil.

Os dados fornecidos pela EMBRAPA abrangem diversas informações relacionadas à produção, processamento, comercialização, importação e exportação no setor vitivinícola, e atualmente estão disponíveis em arquivos CSV separados por categorias.

A API proposta visa consolidar essas informações e facilitar seu acesso, oferecendo uma interface eficiente para consultas públicas, possibilitando análises mais aprofundadas e casos de uso futuros.


# Endpoints

Abaixo estão listados e descritos os endpoints disponíveis. Para maiores detalhes de como realizar as requisições e obter exemplos de retorno, consulte o swagger em https://tech-challenge-service-ikrvqv7b6q-rj.a.run.app/docs

## POST `/user/register`

Destinado para o cadastro de usuário usando username e senha.

## POST `/user/login`

Utilizado para obter o token de acesso através do username e senha cadastrado anteriormente.

## GET `/data/comercializacao`

Está relacionado a informações sobre a venda e distribuição dos produtos de vitivinicultura. Possui detalhes sobre a quantidade de produtos vendidos e os valores associados.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Produto`   | `string`      | Nome do produto.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

## GET `/data/exportacao`

Está relacionado a dados sobre a exportação de produtos de vitivinicultura. Inclui informações sobre volumes exportados, países de destino, tipos de produtos enviados e os valores gerados pelas exportações.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `País`   | `string`      | País de destino da exportação.                 |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

## GET `/data/importacao`

Está relacionado a informações sobre a importação de produtos de vitivinicultura. Seus detalhes incluem os volumes importados, países de origem, tipos de produtos adquiridos e valores envolvidos nas transações.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `País`   | `string`      | País de origem da importação.                 |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |
| `Valor`      | `int`      | Valor do produto vendido.         |


## GET `/data/producao`

Está relacionado a informações sobre a produção de produtos de vitivinicultura. Inclui detalhes como áreas plantadas, tipos de uvas cultivadas, métodos de cultivo utilizados e volumes de produção em diferentes regiões e períodos.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Produto`   | `string`      | Nome do produto.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

## GET `/data/processamento`

Está relacionado aos dados sobre o processamento dos produtos da vitivinicultura. Inclui informações sobre os métodos de vinificação, volumes processados, tipos de produtos finais (como vinhos, sucos e destilados) e as etapas de produção envolvidas.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Cultivar`   | `string`      | Espécie da uva.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |


# Autenticação

A autenticação é requisito para todos os endpoints de consulta das categorias. Ela é dada da seguinte forma:
 
 1. Registro do usuário em `/user/register`
 2. login e geração do token de acesso em `/user/login`

Após gerado o token, ele deve ser passado no header da seguinte forma:

```json
{
	"Authorization": "Bearer <token>"
}
```

# Desenho da Arquitetura

![Untitled-2025-01-19-1650](https://github.com/user-attachments/assets/a6d1e2a1-079e-43d1-a587-7f616c585267)

