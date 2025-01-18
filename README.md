# FIAP Tech Challenge 1 - API EMBRAPA Vinicultura

A API foi desenvolvida como parte de um desafio técnico de Machine Learning Engineering, com o objetivo principal de fornecer uma interface pública para consulta de dados relacionados à vitivinicultura disponibilizados pela Embrapa. Esses dados abrangem informações sobre produção, processamento, comercialização, importação e exportação no setor.

Dentre os endpoints disponíveis temos os seguintes:

**Comercialização:** Está relacionado a informações sobre a venda e distribuição dos produtos de vitivinicultura. Possui detalhes sobre a quantidade de produtos vendidos e os valores associados.

**Exportação**: Está relacionado a dados sobre a exportação de produtos de vitivinicultura. Inclui informações sobre volumes exportados, países de destino, tipos de produtos enviados e os valores gerados pelas exportações.

**Importação**: Está relacionado a informações sobre a importação de produtos de vitivinicultura. Seus detalhes incluem os volumes importados, países de origem, tipos de produtos adquiridos e valores envolvidos nas transações.

**Produção**: Está relacionado a informações sobre a produção de produtos de vitivinicultura. Inclui detalhes como áreas plantadas, tipos de uvas cultivadas, métodos de cultivo utilizados e volumes de produção em diferentes regiões e períodos.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Produto`   | `string`      | Nome do produto.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

**Processamento**: Está relacionado aos dados sobre o processamento dos produtos da vitivinicultura. Inclui informações sobre os métodos de vinificação, volumes processados, tipos de produtos finais (como vinhos, sucos e destilados) e as etapas de produção envolvidas.