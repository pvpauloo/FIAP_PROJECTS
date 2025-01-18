# FIAP Tech Challenge 1 - API EMBRAPA Vinicultura

A API foi desenvolvida como parte de um desafio técnico de Machine Learning Engineering, com o objetivo principal de fornecer uma interface pública para consulta de dados relacionados à vitivinicultura disponibilizados pela Embrapa. Esses dados abrangem informações sobre produção, processamento, comercialização, importação e exportação no setor.

Dentre os endpoints disponíveis temos os seguintes:

**Comercialização:** Está relacionado a informações sobre a venda e distribuição dos produtos de vitivinicultura. Possui detalhes sobre a quantidade de produtos vendidos e os valores associados.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Produto`   | `string`      | Nome do produto.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

**Exportação**: Está relacionado a dados sobre a exportação de produtos de vitivinicultura. Inclui informações sobre volumes exportados, países de destino, tipos de produtos enviados e os valores gerados pelas exportações.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `País`   | `string`      | País de destino da exportação.                 |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

**Importação**: Está relacionado a informações sobre a importação de produtos de vitivinicultura. Seus detalhes incluem os volumes importados, países de origem, tipos de produtos adquiridos e valores envolvidos nas transações.

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `País`   | `string`      | País de origem da importação.                 |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |
| `Valor`      | `int`      | Valor do produto vendido.         |

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

| Campo              | Tipo         | Descrição                                    |
|--------------------|--------------|--------------------------------------------|
| `Ano`             | `int`        | Ano da produção.                           |
| `Id`          | `int`     | Identificação do elemento.            |
| `Control`        | `string`     | Nome de controle do produto.                     |
| `Cultivar`   | `string`      | Espécie da uva.                 |
| `Tipo`      | `string`      | Tipo do produto.         |
| `Valor`      | `int`      | Valor do produto vendido.         |
| `Source`      | `string`      | Fonte de onde os dados foram retirados.         |


### Usando a API

```sh
GET api/data/comercializacao?query=Ano%3D2023 
```

Resposta em JSON

````json
{"results":53,"data":[{"Id":2,"Control":"vm_Tinto","Produto":"  Tinto","Tipo":"VINHO DE MESA","Ano":2023,"Valor":165097539},{"Id":3,"Control":"vm_Rosado","Produto":"  Rosado","Tipo":"VINHO DE MESA","Ano":2023,"Valor":2520748},{"Id":4,"Control":"vm_Branco","Produto":"  Branco","Tipo":"VINHO DE MESA","Ano":2023,"Valor":19398561},{"Id":6,"Control":"vm_Tinto","Produto":"  Tinto","Tipo":"VINHO  FINO DE MESA","Ano":2023,"Valor":12450606},{"Id":7,"Control":"vm_Rosado","Produto":"  Rosado","Tipo":"VINHO  FINO DE MESA","Ano":2023,"Valor":1214583},{"Id":8,"Control":"vm_Branco","Produto":"  Branco","Tipo":"VINHO  FINO DE MESA","Ano":2023,"Valor":4924121},{"Id":12,"Control":"ve_Tinto","Produto":"  Tinto","Tipo":"VINHO ESPECIAL","Ano":2023,"Valor":0},{"Id":13,"Control":"ve_Rosado","Produto":"  Rosado","Tipo":"VINHO ESPECIAL","Ano":2023,"Valor":0},{"Id":14,"Control":"ve_Branco","Produto":"  Branco","Tipo":"VINHO ESPECIAL","Ano":2023,"Valor":0},{"Id":16,"Control":"es_Espumante_Moscatel","Produto":"  Espumante  Moscatel","Tipo":"ESPUMANTES ","Ano":2023,"Valor":9771698},{"Id":17,"Control":"es_Espumante","Produto":"  Espumante","Tipo":"ESPUMANTES ","Ano":2023,"Valor":19609379},{"Id":18,"Control":"es_Espumante Orgânico","Produto":"  Espumante Orgânico","Tipo":"ESPUMANTES ","Ano":2023,"Valor":558},{"Id":20,"Control":"su_Suco_Natural","Produto":"  Suco Natural Integral","Tipo":"SUCO DE UVAS","Ano":2023,"Valor":129419407},{"Id":21,"Control":"su_Suco_Adoçado","Produto":"  Suco Adoçado","Tipo":"SUCO DE UVAS","Ano":2023,"Valor":128599},{"Id":22,"Control":"su_Suco_Reprocessado","Produto":"  Suco Reprocessado/reconstituido","Tipo":"SUCO DE UVAS","Ano":2023,"Valor":34402925},{"Id":23,"Control":"su_Suco_Orgânico","Produto":"  Suco Orgânico","Tipo":"SUCO DE UVAS","Ano":2023,"Valor":932154},{"Id":24,"Control":"su_Outros_sucos","Produto":"  Outros sucos de uvas","Tipo":"SUCO DE UVAS","Ano":2023,"Valor":1825635},{"Id":27,"Control":"ou_Outros vinhos (sem informdetalhada","Produto":"  Outros vinhos (sem informação detalhada)","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":8152},{"Id":28,"Control":"ou_Agrin","Produto":"  Agrin (fermentado, acetico misto)","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":29,"Control":"ou_Aguardente","Produto":"  Aguardente de vinho 50°gl","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":111},{"Id":30,"Control":"ou_Alcool_vinico","Produto":"  Alcool vinico","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":31,"Control":"ou_Bagaceira","Produto":"  Bagaceira (graspa)","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":32,"Control":"ou_Base_champenoise","Produto":"  Base champenoise champanha","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":66290},{"Id":33,"Control":"ou_Base_charmat","Produto":"  Base charmat champanha","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":184040},{"Id":34,"Control":"ou_Base_espumante","Produto":"  Base espumante moscatel","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":722984},{"Id":35,"Control":"ou_Bebida","Produto":"  Bebida de uva","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":16780},{"Id":36,"Control":"ou_Borra_liqwuida","Produto":"  Borra líquida","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":72600},{"Id":37,"Control":"ou_Borra_seca","Produto":"  Borra seca","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":53220},{"Id":38,"Control":"ou_Brandy","Produto":"  Brandy (conhaque)","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":4506},{"Id":39,"Control":"ou_Cooler","Produto":"  Cooler","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":4321881},{"Id":40,"Control":"ou_Coquetel","Produto":"  Coquetel com vinho","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":397156},{"Id":41,"Control":"ou_Destilado","Produto":"  Destilado de vinho","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":245},{"Id":43,"Control":"ou_Jeropiga","Produto":"  Jeropiga","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":346},{"Id":44,"Control":"ou_Mistelas","Produto":"  Mistelas","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":1668},{"Id":45,"Control":"ou_Mosto_concentrado","Produto":"  Mosto concentrado","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":46,"Control":"ou_Mosto_uva","Produto":"  Mosto de uva","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":359626},{"Id":47,"Control":"ou_Mosto_sulfitado","Produto":"  Mosto sulfitado","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":48,"Control":"ou_Nectar","Produto":"  Nectar de uva","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":3604413},{"Id":49,"Control":"ou_Outros_produtos","Produto":"  Outros produtos","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":7459271},{"Id":50,"Control":"ou_Polpa","Produto":"  Polpa de uva","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":1331651},{"Id":51,"Control":"ou_Preparado_líquido","Produto":"  Preparado líquido para refresco","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":17178},{"Id":52,"Control":"ou_Refrigerante","Produto":"  Refrigerante +50% suco","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":501876},{"Id":53,"Control":"ou_Sangria","Produto":"  Sangria","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":84157},{"Id":54,"Control":"ou_Vinagre_balsamico","Produto":"  Vinagre balsamico","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":338926},{"Id":55,"Control":"ou_Vinagre_duplo","Produto":"  Vinagre duplo","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":1769130},{"Id":56,"Control":"ou_Vinagre_simples","Produto":"  Vinagre simples","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":5047280},{"Id":57,"Control":"ou_Vinho_acetificado","Produto":"  Vinho acetificado","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":194020},{"Id":58,"Control":"ou_Vinho_base","Produto":"  Vinho base para espumantes","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":0},{"Id":59,"Control":"ou_Vinho_composto","Produto":"  Vinho composto","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":981},{"Id":60,"Control":"ou_Vinho_licoroso","Produto":"  Vinho licoroso","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":421974},{"Id":61,"Control":"ou_Vinho_leve","Produto":"  Vinho leve","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":132064},{"Id":62,"Control":"ou_Vinho_gaseificado","Produto":"  Vinho gaseificado","Tipo":"OUTROS PRODUTOS COMERCIALIZADOS","Ano":2023,"Valor":410215}]}
```