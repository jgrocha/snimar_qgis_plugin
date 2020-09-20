# Extensão para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar

<img src="http://193.136.227.146/manual_images/Screenshot_20200825_135238.png">

Índice
======

   * [Ficha Técnica e Contactos](#ficha-técnica-e-contactos)
   * [Intervenientes e parceiros](#intervenientes-e-parceiros)
   * [Introdução](#introdução)
   * [Instalação](#instalação)
   * [Usar a extensão](#usar-a-extensão)
      * [Ambiente de Trabalho](#ambiente-de-trabalho)
      * [Gestão de Contactos](#gestão-de-contactos)
      * [Edição de Metadados](#edição-de-metadados)
         * [Identificação](#identificação)
         * [Operações](#operações)
         * [Informação Geográfica](#informação-geográfica)
         * [Informação Temporal](#informação-temporal)
         * [Qualidade](#qualidade)
         * [Elementos referentes ao Relatório](#elementos-referentes-ao-relatório)
         * [Restrições](#restrições)
         * [Distribuição](#distribuição)
         * [Metadados](#metadados)
   * [Anexo - Classificação dos Serviços](#anexo---classificação-dos-serviços)
   

Ficha Técnica e Contactos
=========================

**FICHA TÉCNICA VERSÃO PARA QGIS 3.x**

TÍTULO: Manual de Utilizador da extensão para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar

AUTORIA: Projectos MARSW e INFORBIOMARES

EMAIL: jgoncal@ualg.pt

DATA: Julho 2020

VERSÃO DA EXTENSÂO: 3.x


**CONTACTOS VERSÃO PARA QGIS 3.x**

Projecto **MARSW**

Telefone: +351 289 800 051 | E-mail: jgoncal@ualg.pt | Site: https://marsw.pt

Projecto **INFORBIOMARES**

Telefone: +351 289 800 051 | E-mail: ccmar@ualg.pt | Site: https://www.ccmar.ualg.pt/en/project/inforbiomares


**FICHA TÉCNICA ORIGINAL**

TÍTULO: Manual de Utilizador/Instalação do Editor de Metadados SNIMar

AUTORIA: Grupo de Trabalho WP4 SNIMar

EMAIL: suporte.snimar@ipma.pt

DATA: dezembro de 2015

LOCAL: Lisboa

VERSÃO DA EXTENSÂO: 2.0.0


**CONTACTOS ORIGINAIS**

IPMA - INSTITUTO PORTUGUÊS DO MAR E DA ATMOSFERA

Rua C do Aeroporto | 1749-077 Lisboa - Portugal

Telefone: +351 218 477 000 | Fax: +351 218 402 468 | E-mail:info@ipma.pt


EMEPC - Estrutura de Missão para a Extensão da Plataforma Continental

Rua Costa Pinto nº165 | 2770-047 Paço de Arcos - Portugal

Telefone: +351 213 004 165 | Fax: +351 213 905 225 | E-mail: info@emepc.mam.gov.pt



Intervenientes e parceiros
==========================

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/MARSW-01.png" height="100">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/Inforbiomares-01.png" height="100">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/ICNF-01.png" height="75">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/LPN-01.png" height="75">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/CCMAR_UAlg-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/MARE-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/UEvora-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/ULisboa_Fac_Ciencias-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/ualg_logo_transparent.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/UniaoEuropeia-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/Rep_Portuguesa-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/Portugal2020-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/POSEUR-01.png" height="50">

<img src="https://inforbiomares.ualg.pt/lizmap/www/themes/default/css/img/Fundo%20Ambiental-01.png" height="50">



Introdução
==========

A “**extensão para criação e edição de metadados segundo o perfil SNIMar**”
é o "*porting*" para a versão 3.x do *software* SIG "QGIS" (Quantum GIS) (https://www.qgis.org) do editor de Metadados desenvolvido no âmbito do Projecto SNIMar com o objectivo de ser a ferramenta destinada à criação dos metadados em conformidade com o Perfil de Metadados SNIMar. **O trabalho de migração do código para QGIS 3.x foi realizado no âmbito dos projectos MARSW e INFORBIOMARES**.

**Editor de Metadados SNIMar**
foi desenvolvido no âmbito do Projeto SNIMar (http://editor.snimar.pt/)  com o objetivo de ser a ferramenta destinada à criação de metadados em conformidade com o Perfil de Metadados SNIMar. O Editor consiste numa extensão para a aplicação QGIS, permitindo que a criação de metadados seja feita em paralelo e em simultâneo com a criação e edição de Conjuntos de Dados Geográficos (CDG).

O SNIMar é um projeto nacional, financiado pelo Mecanismo Financeiro do Espaço Económico Europeu 2009-2014 no âmbito dos European Economic Area Grants (EEA Grants), que tem por objetivo o desenvolvimento de uma infraestrutura de dados espaciais marinhos para o aumento da capacidade de avaliação e previsão do estado ambiental das águas marinhas. Esta infraestrutura traduz-se num Geoportal que irá potenciar a interação do público com a informação disponibilizada pelos parceiros e entidades participantes do projeto e constituirá um ponto central de agregação, pesquisa e distribuição de informação geográfica sobre o ambiente marinho em Portugal.

Os metadados de informação geográfica não são mais do que uma descrição textual, de forma normalizada, da informação geográfica. A sua documentação é indispensável para a identificação e avaliação técnica (escala, sistema de referência, qualidade, extensão geográfica e temporal, contactos dos responsáveis) dos CDG, assim como aspetos ligados ao acesso e utilização de serviços de informação geográfica. Pesquisas feitas em sistemas de informação, infraestruturas de dados espaciais (IDE) ou sistemas de comércio eletrónico, são suportadas pelos metadados, que funcionam como o “combustível” para encontrar os recursos desejados.

O Perfil de Metadados SNIMar, definido no âmbito do referido projeto, respeita os requisitos da
Diretiva INSPIRE (Diretiva n.º 2007/2/CE, do Parlamento Europeu e do Conselho, de 14 de março) e as respetivas disposições de execução definidas no Regulamento (CE) n.º 1205/2008 da Comissão, de 3 de dezembro, que estabelece os requisitos aplicáveis à criação e manutenção de metadados para conjuntos de dados geográficos (CDG), séries de conjuntos de dados geográficos e serviços de dados geográficos correspondentes aos temas enumerados nos anexos I, II e III da Diretiva 2007/2/CE. É também importante realçar que o Perfil de Metadados SNIMar teve por base o Perfil Nacional de Metadados de Informação Geográfica (Perfil MIG), que “tem como objetivo principal clarificar aspetos ligados à implementação da produção, gestão e disseminação dos metadados em Portugal, de forma a assegurar a correta caracterização dos recursos geográficos e a sua harmonização com a infraestrutura de informação geográfica portuguesa (SNIG) e europeia (INSPIRE).” [Perfil MIG, 2010], ajustando-se este perfil à realidade nacional dos dados relativos ao ambiente marinho.



Instalação
==========

A extensão **EditorMetadadosMarswInforbiomares** foi desenvolvida para operar nos sistemas operativos Linux, Windows e macOS e pode ser instalado na aplicação QGIS da seguinte forma:

*   Abrir a aplicação QGIS, recomenda-se a utilização da versão 3.10.x

*   No Menu Principal selecionar **Módulos > Gerir e Instalar Módulos**

*   Selecionar o separador **Configurações**

*   Adicionar um novo repositório de módulos, premindo o botão “Adicionar...”, e preencher os campos do formulário com os seguintes parâmetros:

    *   *Nome*: Editor Metadados MarSW/Inforbiomares
    
    *   *URL*: https://marsw.ualg.pt/static/qgis/editormetadadosmarswinforbiomares.xml

    *   *Parâmetros*: manter pré-definições
    
    *   *Ativado*: manter pré-definições

*   Fazer “Ok” e atualizar os repositórios premindo o botão “Atualizar todos os repositórios”.

*   Selecionar o separador **Não instalado** e pesquisar por “MarSW” ou “Inforbiomares” ou “SNIMar”

*   Instalar a extensão através do botão “Instalar módulo”

A extensão **EditorMetadadosMarswInforbiomares** ficará ativa e disponível no menu de ferramentas através do ícone <img src="http://193.136.227.146/manual_images/100000000000004000000040A7A1CB042E5963C1.png" width="25">



Usar a extensão
===============

Ao premir o ícone do **EditorMetadadosMarswInforbiomares** terá acesso a uma janela que, para além de um Menu Principal, terá um Separador com o seu ambiente de trabalho (Lista de Ficheiros), ou seja, uma Lista dos documentos de metadados (ficheiros XML) trabalhados a partir deste Editor. Atenção que enquanto não criar novos metadados ou abrir outros já existentes, a partir do editor, esta Lista aparecerá vazia no seu ambiente de trabalho.

**Nota**: Ao fazer duplo *click* em ficheiros da Lista estes são abertos como novos Separadores em modo de edição.


Ambiente de Trabalho
--------------------

Nesta área poderá gerir os seus documentos de metadados e consultar alguma da sua informação base (Tipo de Recurso, Título, Localização (do ficheiro), Identificador Único do Ficheiro, Conformidade com o Perfil SNIMar.

O botão <img src="http://193.136.227.146/manual_images/100002010000002100000021EFB2E74358139587.png"> permite validar automaticamente o documento quanto à sua conformidade com o Perfil SNIMar.

Ao selecionar um documento de metadados da Lista e abrindo o *Menu de Contexto* (*click* com o botão do lado direito do rato) tem acesso às seguintes funcionalidades:

*   **Editar Metadado**: abrir o documento XML na extensão em modo de edição;

*   **Remover Metadado(s) da Lista**: remover o(s) documento(s) XML selecionado(s) da Lista;

*   **Visualizar Metadado Externamente**: abrir o documento XML no *software* pré-definido para ficheiros XML.

Na parte inferior da janela (lado direito) tem dois botões com as seguintes funcionalidades:

*   **Verificar Conformidade (Todos)**: validar todos os documentos da Lista quanto à sua conformidade com o Perfil SNIMar. Esta ação pode demorar consoante o número de itens na Lista, pode a qualquer momento terminar o processo premindo o botão “Cancelar” da janela de progresso.

*   **Apagar Lista de Ficheiros**: remover todos os documentos XML da Lista (apenas).

Na parte inferior da janela (lado esquerdo) poderá ainda consultar qual a última *versão do Thesaurus SNIMar* carregada na extensão e poderá descarregar novas atualizações, se existirem, premindo o botão “Atualizar”.

É possível também *ordenar a Lista de ficheiros de metadados* por: Tipo de Recurso, Título, Localização (do ficheiro) e pela sua Conformidade com o Perfil SNIMar; basta premir o título correspondente e alternar a ordem.

A partir do **Menu Principal** poderá:

*   **Ficheiro > Novo**: criar um novo documento de metadados XML dos seguintes tipos: Conjunto de Dados Geográficos, Serviço e Série.

*   **Ficheiro > Abrir**: abrir um documento XML, a partir do sistema de arquivo de ficheiros, na extensão em modo de edição. Este documento de metadados aberto será também adicionado à Lista de ficheiros.

*   **Ficheiro > Abrir Pasta**: carregar para o seu ambiente de trabalho os ficheiros XML que se encontrarem na pasta selecionada a partir do sistema de arquivo de ficheiros.

*   **Ficheiro > Guardar**: guardar as alterações efetuadas ao documento XML a partir da extensão de edição.

*   **Ficheiro > Guardar como**: guardar o ficheiro com outro nome ou noutro diretório.

*   **Ficheiro > Guardar Todos**: guardar todos os ficheiros de metadados abertos no editor.

*   **Ficheiro > Fechar**: fechar a extensão **EditorMetadadosMarswInforbiomares**.

*   **Ficheiro > Atualizar codelists**:atualiza os campos do tipo Lista de Valores dos vários formulários.

*   **Lista de Contactos**: gerir (adicionar / editar / remover) os contactos e respetivos detalhes usados frequentemente nos seus documentos de metadados.

*   **Sobre** : abrir uma janela com informações sobre a extensão **EditorMetadadosMarswInforbiomares**.


Gestão de Contactos
-------------------

Ao selecionar a opção “Lista de Contactos” do Menu Principal abrirá uma janela que apresenta na parte lateral esquerda uma Lista de contactos já criados e na parte lateral direita o formulário de edição dos contactos.

Ao criar um novo contacto deverá preencher obrigatoriamente os campos “Nome da Organização” e “Endereço Eletrónico” (pelo menos um), os
restantes campos são opcionais mas aconselha-se o seu preenchimento.

**Criar um Novo Contacto**

*   prima o botão “Novo”;

*   preencha os campos;

*   prima o botão “Guardar Alterações”.


**Editar um Contacto**

*   selecione da Lista o contacto em questão;

*   efetue as alterações a partir do formulário agora preenchido com os detalhes do contacto selecionado;

*   prima o botão “Guardar Alterações”.


**Apagar um Contacto**

*   selecione da Lista o contacto em questão;

*   prima o botão “Apagar”.

*   Receberá uma mensagem a pedir confirmação da eliminação do contacto dado que é uma operação irreversível. Para confirmar a eliminação prima o botão “Remover”.


**Notas:** Alguns campos permitem a introdução de *múltiplos valores*, como é o caso do “Telefone”, “Fax”, “Endereço Eletrónico” e “Informação Online”. Para preencher estes campos deverá preencher o campo de texto posicionado em baixo da Lista respetiva a cada um deles (com textos exemplo) e premir o botão
<img src="http://193.136.227.146/manual_images/100002010000019300000193BC9FD78E936508CD.png" width="25">.

Para remover da Lista terá de selecionar a opção que pretende eliminar e primir o botão <img src="http://193.136.227.146/manual_images/10000201000001930000019328914E2E388B62C5.png" width="25">.


Edição de Metadados
-------------------

Ao criar ou abrir um documento de metadados será criada, na janela da extensão, um novo Separador com o formulário de preenchimento de metadados. Ao abrir um documento de metadados os campos, reconhecidos pelo editor, serão preenchidos nos campos respetivos de forma automática. Os campos variam consoante o tipo de recurso em questão.

O formulário de preenchimento de metadados está dividido em secções, listadas na parte lateral esquerda do Separador, que agrupam de forma lógica os campos de metadados. Na parte lateral direita é apresentado o Painel com os campos que pertencem à secção selecionada na parte esquerda.

A lista de secções é a seguinte:

*   Identificação;

*   Operações (exclusivo a recursos do tipo “Serviço”);

*   Classificação & Palavras-Chave;

*   Informação Geográfica;

*   Informação Temporal;

*   Qualidade;

*   Restrições;

*   Distribuição;

*   Metadados.

Na parte lateral esquerda, onde são listadas as secções, terá indicações de validação da conformidade do preenchimento do metadado. As secções a vermelho estarão não conformes e as a preto conformes. Ao passar com o rato sobre cada secção a vermelho terá a indicação específica dos campos que não estão conformes.

De igual forma os painéis na parte lateral direita também apresentam ajudas textuais para cada um dos campos (premir o botão de informação junto ao nome de cada campo) e indicações de validação. Os campos com “*” são de preenchimento obrigatório e enquanto não forem preenchidos corretamente encontram-se a vermelho.

Alguns campos permitem a introdução de *múltiplos valores*, para os adicionar deverá preencher o campo (com textos exemplo) ou selecionar de um campo de lista de valores posicionados em baixo da Lista / Tabela respetiva e premir o botão <img src="http://193.136.227.146/manual_images/100002010000019300000193BC9FD78E936508CD.png" width="25">. Para remover uma opção da Lista selecione a opção a eliminar e prima o botão <img src="http://193.136.227.146/manual_images/10000201000001930000019328914E2E388B62C5.png" width="25">.

Pode remover mais do que um de uma vez, para tal só terá de fazer uma multi‑seleção de opções (CTRL+*click*) antes de premir o botão de eliminar. Alguns campos do tipo Lista de Valores têm para cada opção da lista uma ajuda textual, para as visualizar basta posicionar o rato sobre as opção da lista.

Cada painel contém um conjunto de elementos e sub‑elementos a preencher. De seguida, descrevem-se cada um destes painéis, respetivos campos e sua obrigatoriedade (*) e multiplicidade de preenchimento.


### Identificação

Informação de base necessária à identificação inequívoca de um dado recurso. Contém os seguintes elementos e sub‑elementos:

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Tipo de Recurso | Sim     | Não      | Define o tipo de recurso ao qual se aplicam os metadados, a partir de uma lista: Conjunto de Dados Geográficos (CDG) (a informação é aplicável a um conjunto de dados geográficos); Série (a informação é aplicável a uma série ou coleção de dados); Serviço (a informação é aplicável à capacidade que uma entidade fornecedora disponibiliza a uma entidade cliente através de um conjunto de interfaces que define um dado comportamento). |
| Tipo de Serviço | Sim     | Não      | Define o tipo de serviço, a partir da lista definida pela especificação do INSPIRE. Não se aplica a CDG nem Séries. |
| Acoplamento     | Sim     | Não      | Tipo de acoplamento dos serviços com os CDG. Não se aplica a CDG nem Séries. |
| Título          | Sim     | Não      | Designação pela qual o recurso é conhecido. O título deve permitir identificar o recurso com o maior rigor possível. Recomenda-se a tradução deste campo para Inglês no campo Título (Inglês). |
| Resumo          | Sim     | Não      | Breve resumo sobre o conteúdo do recurso. Recomenda-se a tradução deste campo para Inglês no campo Resumo (Inglês). |
| Título Alternativo          | Não     | Não      | Nome alternativo ou abreviado pelo qual o recurso é conhecido. |
| Objetivo          | Não     | Não      | Resumo do propósito que conduziu ao desenvolvimento ou modificação do recurso. |
| Créditos | Não      | Sim      | Identificação dos indivíduos e/ou entidades que contribuíram para a produção do recurso. |
| Manutenção do Recurso | Sim      | Sim      | Define a frequência com que o recurso é atualizado, a partir de uma lista. Se nenhuma das opções da lista for adequada, selecione "Conforme necessário". |


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Identificador Único do Recurso | Sim      | Sim      | Pretende identificar de forma unívoca o recurso, é definido normalmente pela entidade responsável pelo mesmo. Pode conter múltiplos conjuntos dos seguintes 2 sub‑elementos. |
| Identificador                  | Sim      | Não      | Utilização de URI (exº http://www.igeo.pt/datasets/AU_CAOP_2011) ou UUID (exº 808c3be3-527a-451b-8611-0bcc1b8c21b0). |
| Espaço de Nomes                | Não      | Não      | Define o âmbito de aplicação do código usado acima. |
  

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resolução Espacial                                                                                                          | Sim          | Sim      | Nível de detalhe do recurso, expresso como um fator de escala ou como uma distância no terreno.Pode conter múltiplos valores dos seus sub‑elementos. Caso se desconheça este elemento e, sendo que é obrigatório, selecione a *checkbox * “Resolução Espacial Desconhecida”. |
| Escala Equivalente  | Condicional      | Sim      | Para um recurso em formato analógico ou conjuntos digitais para impressão é a escala de representação. No caso de recursos digitais a escala deverá corresponder a um compromisso entre a resolução espacial (da informação matricial de origem) e/ou erro do levantamento (precisão dos equipamentos de aquisição utilizados) e o erro de graficismo convertido à escala da carta que se pretende imprimir. |
| Distância                                                                                                                   | Condicional | Sim      | Nível de detalhe dos dados expresso em GSD (*Ground Sample Distance*). Para conjuntos de dados vetoriais que não têm uma escala associada ou não são produzidos para serem disponibilizados em formato analógico, pode-se usar este elemento para descrever a precisão estimada na aquisição dos dados. Expressa em metros. |

**Notas**: Este elemento é obrigatório apenas para CDG e Séries. Para dados vetoriais utiliza-se normalmente a escala (denominador), para dados matriciais a distância no terreno em metros.

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Codificação | Não      | Não      | Define a codificação informática de caracteres utilizada no |
| Estado do Recurso | Não      | Sim      | Define o estado de progresso do recurso, a partir de uma lista: *Arquivado* (dados foram armazenados numa infraestrutura de armazenamento *offline*);*Concluído* (produção dos dados foi concluída); *Contínuo* (dados são atualizados continuamente); *Em desenvolvimento*(dados estão atualmente em processo de criação); *Necessita de atualização* (dados necessitam de atualização); *Obsoleto* (dados já não são relevantes); *Planeado* (estabelecida uma data fixa na qual os dados são atualizados).  |
| Recursos Associados | Não      | Sim      | O domínio deste elemento é um URI, que pode ser um identificador do CDG, ou uma localização (URL) para osmetadados do(s) CDG associados ao recurso. Não se aplica a CDG nem Séries.
| Endereço (URL da visualização gráfica) | Não      | Não      | Define o caminho (URL) para uma figura que ilustra o recurso (deve incluir uma legenda para a figura). |
| Idioma   | Não      | Sim      | Idioma(s) utilizado(s) no recurso. Não se aplica a Serviços.          |
| Representação Espacial | Sim      | Sim      | Forma(s) de representação da informação geográfica, a partir de uma lista: Matricial (informação geográfica segue um modelo de dados matricial); Modelo Estereoscópico (vista tridimensional formada pela intersecção de raios homólogos resultantes de um par de imagens com sobreposição); TIN (informação geográfica representa-se de acordo com uma tecelagem irregular triangular TIN); Texto Tabela (informação geográfica encontra-se codificada em formato textual ou tabular); Vectorial (informação geográfica segue um modelo de dados vetorial); Video (cena obtida de uma gravação de vídeo). Não se aplica a Serviços. |

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Responsáveis pelo Recurso / ou organização responsável pelo recurso- Pode conter múltiplos conjuntos dos seguintes sub‑elementos.  | Sim      | Sim      | Informações necessárias para permitir o contacto com a pessoa e / ou organização responsável pelo recurso. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| Função                                                                 | Não      | Não      | Função desempenhada pela organização responsável, a partir de uma lista: Autor (entidade responsável pela autoria dos recursos); Contacto (entidade / pessoa contactável para obtenção dos recursos ou de informação sobre os recursos); Contacto do Processo (entidade / pessoa que participou em algum processo conducente à modificação dos recursos); Detentor (entidade detentora dos direitos de propriedade sobre os recursos); Editor (entidade que publicou os recursos); Fornecedor (entidade que fornece os recursos); Investigador Principal (entidade de nível hierárquico superior responsável pela recolha da informação e orientação da investigação); Produtor (entidade produtora dos recursos); Tutor (entidade responsável pela tutela dos dados e pela manutenção dos recursos); Utilizador (entidade que utilizada os recursos). |
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável.  |
| Organização                                                            | Sim      | Não      | Nome da organização responsável. Poderá selecionar de uma Lista de valores ou preencher de forma livre no campo “Outra (não listada)” |
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável. |
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável. |
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável.  |
| País                                                                   | Não      | Não      | País da pessoa ou organização responsável.  |
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo. |
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo. |
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo. |
| Informação *Online*                                                    | Não      | Não      | Informação *Online* (endereço URL / URI) que pode ser usada como contacto individual ou institucional. |

**Este elemento disponibiliza as seguintes funcionalidades / botões**: 

“Adicionar Contacto”, para adicionar um novo contacto. 

<img src="http://193.136.227.146/manual_images/100002010000002000000020A3F87039BE9D0D7E.png" width="25"> Para importar um contacto da sua Lista de Contactos para o formulário. 

<img src="http://193.136.227.146/manual_images/10000201000001B7000001B78F0FC5D379C32E50.png" width="25"> Para guardar o contacto na sua Lista de Contactos. 

<img src="http://193.136.227.146/manual_images/100002010000001700000017FBA90A52D3565DE1.png" width="25"> Para remover o contacto.


### Operações

Informação sobre todas as operações disponibilizadas por um Serviço, logo só é preenchido para recursos do tipo “Serviço”. Contém os seguintes elementos e sub‑elementos:


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Operações                         | Sim      | Sim      | Informação sobre as operações disponibilizadas pelo serviço. Para criar uma nova Operação prima o botão “Adicionar Operação”. Deve ser preenchido com um URL para um documento que descreva a interface do serviço, como por exº o GetCapabilities ou um documento WSDL, mais exemplos apresentados abaixo. |
| Nome da Operação                  | Sim      | Não      | Identificador único para um interface específico de um serviço; por exº: "GetCapabilities".
| DCP (*Distributed Computing Platforms*) | Sim      | Sim      | Define a(s) plataforma(s) computacional(ais) em que a operação foi implementada, a partir de uma lista. O valor por omissão deve ser “WebServices”.
| Pontos de Acesso (URI/URL)        | Sim      | Sim      | Ponto de acesso. URL que acede ao documento. O preenchimento deste sub‑elemento, não substitui o preenchimento do Localizador do Recurso referido no Painel “Distribuição”. |


**Exemplos de Nomes de Operação WMS**:

*   GetCapabilities;

*   GetMap;

*   GetFeatureInfo;

*   DescribeLayer;

*   GetLegendGraphic.



**Exemplos de Nomes de Operação WFS**:

*   GetCapabilities;

*   DescribeFeatureType;

*   GetFeature;

*   LockFeature;

*   Transaction;

*   GetPropertyValue (versão 2.0.0 apenas);

*   GetFeatureWithLock (versão 2.0.0 apenas);

*   CreateStoredQuery (versão 2.0.0 apenas);

*   DropStoredQuery (versão 2.0.0 apenas);

*   ListStoredQueries (versão 2.0.0 apenas);

*   DescribeStoredQueries (versão 2.0.0 apenas);

*   GetGMLObject (versão 1.1.0 apenas).



**Exemplos de Nomes de Operação WCS**:

*   GetCapabilities;

*   DescribeCoverage;

*   GetCoverage.


**Classificação & Palavras-Chave**

Informação geral que categoriza e descreve um dado recurso. Contém os seguintes elementos e sub‑elementos:


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Temas INSPIRE | Sim      | Sim      | Se o recurso for um CDG ou Série, deve ser fornecida, pelo menos, uma palavra-chave do Thesaurus Geral Multilingue sobre Recursos Ambientais (GEMET) que descreva o tema de dados geográficos relevante, conforme definido nos anexos I, II ou III da Diretiva INSPIRE (Anexo A). Estes elemento é definido a partir de uma lista. Não se aplica a Serviços.|
| Classificação dos Serviços | Sim      | Sim      | Se o recurso for um Serviço, deve ser fornecida, pelo menos, uma palavra-chave da classificação dos serviços de dados geográficos, definido a partir de uma lista. Poderá consultar uma descrição acerca de cada uma das opções desta lista em Anexo. Não se aplica a CDG nem Séries. |
| Categoria Temática | Sim      | Sim      | Tema principal do recurso. Define a classificação temática geral utilizada para auxiliar o agrupamento e pesquisa do recurso, a partir de uma lista. De acordo com o Perfil SNIMar o tema “Oceanos” deverá estar sempre selecionado. Ao criar um documento de metadados via este editor esta condição será automaticamente aplicada. Não se aplica a Serviços.   |


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Palavras-Chave Livres | Não      | Sim      | Este elemento permite introduzir outras palavras-chave, livres ou associadas a um léxico, que caracterizam o recurso. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| Palavra-Chave         | Não      | Não      | Texto utilizado para descrever um determinado aspeto do recurso.    |
| Tipo                  | Não      | Não      | Utilizado para agrupar as palavras-chave, definido a partir de uma lista.    |
| Thesaurus             | Não      | Não      | Nome do léxico, thesaurus ou fonte de palavras-chave formalmente registado.   |   
| Data                  | Não      | Não      | Data de referência do léxico citado.   |       
| Tipo de Data          | Não      | Não      | Evento usado para a data referenciada, definido a partir de uma lista.    |


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Palavras-Chave SNIMar     | Sim      | Sim      | Descreve o recurso utilizando palavras-chave pertencentes a um dicionário dedicado ao projeto SNIMar.Pode conter múltiplos conjuntos dos seguintes sub‑elementos. | 
| Tipo     | Sim      | Não      | Define o tipo de Palavra-Chave utilizado, a partir de lista.|
| Palavra-Chave       | Sim      | Não      | Define uma designação utilizada para descrever um determinado aspeto do recurso, a partir de uma lista. |
| Versão Thesaurus    | Sim      | Não      | Versão do Thesaurus SNIMar a partir do qual foi selecionada a palavra-chave. |

**Notas**: Deve ser escolhida obrigatoriamente pelo menos uma palavra-chave para o tipo “Disciplina” e pelo menos uma palavra-chave para o tipo “Parâmetro”. Caso o recurso tenha sido criado no contexto de um projeto, é obrigatório inserir uma palavra-chave com o nome do projeto e usar o tipo de palavra ‘Projeto’. Recomenda-se a inserção de palavras dos restantes grupos de palavras provenientes do Thesaurus SNIMar, a partir da lista do Thesaurus com a versão mais recente. Para criar novas palavras-chave SNIMar deverá fazê-lo a partir da plataforma **Collaborative Keywords**, aceda diretamente premindo o ícone 

<img src="http://193.136.227.146/manual_images/10000201000001BD0000009E16A6984AEFE1D85F.png" width="200">

Para adicionar palavras-chave SNIMar prima o botão “Adicionar Palavra-Chave SNIMar”. Ao executar esta ação é aberta uma janela (figura seguinte) de onde deverá selecionar de início o “Tipo de Palavra-Chave” da lista disponível. Ao selecionar um Tipo de Palavra-Chave é apresentada na parte lateral direita a lista de palavras-chave relacionadas com esse Tipo. Poderá selecionar múltiplas palavras-chave para acrescentar ao documento acionando os *checkboxes* respetivos. No caso particular do Tipo de Palavra-Chave “Disciplina” após selecionar uma ou mais disciplinas deverá também selecionar um ou mais parâmetros, apresentados na parte lateral mais à direita (à medida que vai selecionando disciplinas). Apósacionar as palavras-chave pretendidas deve premir o botão “Adicionar Selecionadas”.

<img src="http://193.136.227.146/manual_images/10000000000003A00000027449993894749EB3FE.png">


### Informação Geográfica

Informação sobre os Sistemas de Referência de Coordenadas e sobre a extensão espacial geográfica e altimétrica do recurso. Contém os seguintes elementos e sub‑elementos:

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Localização Geográfica    | Sim      | Sim      | Informação sobre a extensão geográfica do recurso. Pode conter múltiplos conjuntos dos seguintes sub‑elementos.
| Limite Oeste    | Sim      | Não      | Coordenada ocidental do limite da extensão do recurso, expressa em longitude utilizando graus decimais. Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-180, 180].  |
| Limite Este     | Sim      | Não      | Coordenada oriental do limite da extensão do recurso, expressa em longitude utilizando graus decimais. Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-180, 180].  |
| Limite Norte    | Sim      | Não      | Coordenada setentrional do limite da extensão do recurso, expressa em latitude utilizando graus decimais.Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-90, 90].    |
| Limite Sul      | Sim      | Não      | Coordenada meridional do limite da extensão do recurso, expressa em latitude utilizando graus decimais. Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-90, 90].    |
| Contém Recurso  | Sim      | Não      | Indica se o retângulo delimitador abrange uma área coberta pelos dados ou uma área onde os dados não estão presentes. |

**Para adicionar uma nova extensão geográfica pode fazê-lo de duas formas**:

*Manualmente*:

prima o botão “Adicionar Localização”, é então aberta uma janela onde poderá definir os limites nos campos correspondentes e adicioná-los ao metadados premindo o botão “Adicionar”.                                                                                                                                                      

*No Mapa*:

prima o botão                                                                                                                                                                                                                                                                                                                              

<img src="http://193.136.227.146/manual_images/10000201000001E8000001E8CCDB88B34D87F801.png" width="25">

é então aberta uma janela onde poderá desenhar um retângulo que represente os limites. A janela apresenta uma barra de ferramentas de onde pode:                                                                                                                                                                                                                                                                                    

<img src="http://193.136.227.146/manual_images/10000201000001E8000001E8CCDB88B34D87F801.png" width="25"> afastar a visão do mapa à totalidade do globo                                                                                                                                                                                                                                                                                                

<img src="http://193.136.227.146/manual_images/10000201000002AC000002AC93F9F67F6B63BBC7.png" width="25"> mover o mapa                                                                                                                                                                                                                                                                                                                                 

<img src="http://193.136.227.146/manual_images/10000201000000E3000000E3D57FEACA303168F9.png" width="25"> aproximar a visão do mapa                                                                                                                                                                                                                                                                                                                    

<img src="http://193.136.227.146/manual_images/10000201000000E3000000E3A255E6F26DADD695.png" width="25"> afastar a visão do mapa                                                                                                                                                                                                                                                                                                                      

<img src="http://193.136.227.146/manual_images/100002010000019F0000019F2E58215D7D78FD03.png" width="25"> desenhar o retângulo - ao desenhar as coordenadas dos limites os campos respetivos na parte inferior da janela são atualizados. Para adicionar o limite ao metadado prima o botão “Adicionar”.                                                                                                                                               

<img src="http://193.136.227.146/manual_images/100002010000001C0000001A19ADBB8A5C169711.png" width="25"> obter de camada – permite carregar para os campos do formulário a extensão geográfica de um conjunto de dados geográficos carregado no mapa.                                                                                                                                                                                                 

Poderá ainda consultar no mapa uma extensão geográfica presente na tabela de limites, para tal basta selecionar a linha em questão e premir o botão <img src="http://193.136.227.146/manual_images/10000201000001E8000001E8CCDB88B34D87F801.png" width="25">. Se desejar alterar estes limites via o mapa só terá de a desenhar e premir o botão “Alterar”.


<img src="http://193.136.227.146/manual_images/100002010000032000000242921984300E64B038.png">

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Identificador Geográfico | Não      | Sim      | Referência espacial sob a forma de um topónimo ou código que identifica uma localização. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| Identificador            | Não      | Não      | Código que identifica uma localização, exº NUTS. | 
| Contém Recurso           | Não      | Não      | Indica se o retângulo delimitador abrange uma área coberta pelos dados ou uma área onde os dados não estão presentes. |

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Sistema de Referência | Sim          | Sim          | Define o(s) código(s) do(s) sistema(s) de referência de coordenadas sobre o qual o recurso pode ser disponibilizado, a partir de uma lista. |



### Informação Temporal

Informação geral sobre as referências e extensões temporais do recurso. Contém os seguintes elementos e sub‑elementos:

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Extensão Temporal  | Não      | Não      | Período de tempo para o qual o recurso é válido. |
| Data de Início     | Não      | Não      | Data e hora de início.                           |
| Data de Fim        | Não      | Não      | Data e hora de fim.                              |

**Notas**: 

Para introduzir valores terá de usar o Calendário disponibilizado no respetivo campo. Para apagar o conteúdo do campo prima o botão                                                                                                                                                

<img src="http://193.136.227.146/manual_images/1000000000000010000000108DFD72183B48C685.png" width="25">

No caso da extensão temporal corresponder a um instante preencha a Data de Início com o mesmo valor da Data de Fim. Poderá consultar o intervalo temporal resultante dos valores aqui preenchidos no canto superior direito do ecrã. 


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Referência Temporal                                                                     | Sim          | Sim      | Data de referência para o recurso. Este elemento obriga a que pelo menos um dos seus sub‑elementos seja preenchido. |
| Data de Criação                                                                         | Condicional | Não      | Data de referência para a criação do recurso.                                                                       |
| Data de Última Revisão                                                                  | Condicional | Não      | Data de referência da última revisão efetuada ao recurso.                                                           |
| Data de Publicação                                                                      | Condicional | Sim      | Data(s) de referência da publicação do recurso.                                                                     |

**Notas**: 

Para introduzir valores terá de usar o Calendário disponibilizado no respetivo campo. Para apagar o conteúdo do campo prima o botão                                                                                                                                                                                           

<img src="http://193.136.227.146/manual_images/1000000000000010000000108DFD72183B48C685.png" width="25">

No caso da Data de Publicação, por permitir vários valores, terá ainda de premir o botão                                                                                                                                                                                                                          

<img src="http://193.136.227.146/manual_images/100002010000019300000193BC9FD78E936508CD.png" width="25">


### Qualidade

Informação relativa à qualidade dos dados, especificada para um dado âmbito ou para o recurso no seu todo. Contém os seguintes elementos e sub‑elementos:


**Elementos referentes ao Histórico**:
| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Declaração (Português) | Sim      | Não      | Descrição geral sobre o conhecimento do produtor sobre o histórico de um recurso. Os processos e fontes de dados devem ser descritos resumidamente. Se desejar particularizar esta informação poderá fazê-lo preenchendo o elemento opcional “Etapas do Processo”. |
| Declaração (Inglês) | Não      | Não      | Descrição geral sobre o conhecimento do produtor sobre o histórico de um recurso traduzido para Inglês. |
| Etapas do Processo | Não      | Sim      | Descreve os vários processamentos efetuados para a obtenção do recurso. |
| Descrição          | Sim      | Não      | Descrição da etapa do processo efetuado ao conjunto de dados incluindo parâmetros e tolerâncias aplicados. |
| Data               | Não      | Não      | Data ou Intervalo temporal em que a etapa ocorreu.                                                         |
| Justificação       | Não      | Não      | Necessidade ou finalidade da etapa do processo.                                                            |
| Fonte dos Dados | Não      | Sim      | Informações sobre os dados de origem usados na criação do recurso. |


### Elementos referentes ao Relatório

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resultado da Conformidade | Sim      | Não      | Informações sobre o resultado da avaliação do valor obtido, contra um nível de qualidade de conformidade indicado. |
| Especificação             | Sim      | Não      | Citação de uma especificação de produto ou requisito de utilização, face à qual os dados estão a ser avaliados.    |
| Data de Especificação     | Sim      | Não      | Data de referência da especificação citada. | 
| Tipo de Data              | Sim      | Não      | Evento usado para a data referenciada, definido a partir de uma lista. | 
| Resultado Conforme?       | Sim      | Não      | Indicação do resultado de conformidade. | 
| Explicação                | Não      | Não      | Explicação do significado da conformidade do resultado. 


**Notas**: Este elemento é um requisito obrigatório da Diretiva INSPIRE.                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                             
Em caso de desconhecimento pode utilizar a informação recomendada pela Diretiva Inspire premindo o botão “Preencher Automaticamente (INSPIRE)”. Os valores preenchidos serão os seguintes:                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                             
 “*Especificação*”: Regulamento (UE) n . o 1089/2010 da Comissão de 23 de Novembro de 2010 que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos.                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                             
 “*Data de Especificação*”: 2010-12-08                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                             
 “*Tipo de Data*”: Publicação                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                             
 “*Resultado Conforme?*”: Não (*checkbox* desselecionado)                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                             
 “*Explicação*”: Ver a norma da especificação  


### Restrições

Informação relativa a restrições e pré-requisitos legais e de segurança para o acesso e utilização do recurso. Contém os seguintes elementos e sub‑elementos:

| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Restrições Legais    | Sim      | Sim      | Restrições e pré-requisitos legais para acesso e utilização do recurso ou metadado. Pode conter múltiplos conjuntos dos seguintes sub‑elementos.
| Limitações ao Uso    | Sim      | Sim      | Pretende descrever as restrições para o acesso e uso do recurso, descrição dos termos e condições incluindo, se aplicável, taxas a pagar ou a indicação de um URL onde essa informação esteja disponível. Indica também se o recurso não é adequado para um tipo específico de utilização por exº: "não deve ser usado para a navegação". 
| Restrições de Acesso | Sim      | Sim      | Restrições de acesso aplicadas ao recurso para assegurar a propriedade intelectual e quaisquer restrições especiais ou limitações sobre a obtenção do recurso. Definido a partir de uma lista. Definido a partir de uma lista. Se o recurso não tiver restrições de acesso deve ser escolhida a opção "Outras Restrições".
| Restrições de Uso    | Sim      | Sim      | Constrangimentos aplicados de modo a garantir a proteção da propriedade intelectual do recurso bem como restrições especiais ou limitações e advertências sobre o uso do recurso ou metadados. Definido a partir de uma lista. Se o recurso não tiver restrições de uso deve ser escolhida a opção "Outras Restrições". 
| Outras Restrições    | Não      | Sim      | Outras restrições e pré-requisitos legais para aceder e utilizar o recurso ou metadados.
| Restrições de Segurança | Não      | Sim      | Define as restrições de manuseamento do recurso ou metadados, a partir de uma lista (se aplicável): *Altamente Secreto* (do maior nível de segredo); *Confidencial* (disponível para alguém a quem pode ser confiada informação); *Não Classificado* (disponível para divulgação geral); *Restrito* (não para divulgação geral); *Secreto* (mantido ou para ser mantido privado, desconhecido, ou oculto para todos a não ser um grupo seleto de pessoas).


### Distribuição

Informação relativa ao distribuidor e as alternativas para obtenção do recurso. Contém os seguintes elementos e sub‑elementos:


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Formato de Distribuição | Sim      | Sim      | O objetivo deste elemento é dar a conhecer o(s) formato(s) em que o recurso se encontra disponível aos utilizadores. |
| Nome do Formato         | Sim      | Não      | O acrónimo ou extensão por que é conhecido o formato deve, sempre que possível, constar no nome.
| Versão                  | Sim      | Não      | Versão do formato, caso não se saiba pode colocar “Não aplicável” ou “Desconhecida”. 
| Tamanho do Ficheiro | Não      | Não      | Tamanho estimado de uma unidade no formato de transferência especificado, expressa em MegaBytes. |
| Localizador do Recurso                                      | Condicional | Sim      | Informação relativa a fontes *online* a partir das quais pode se obter o recurso, mais informação, ou aceder ao serviço. |
| URL                                                         | Condicional | Não      | Local para o acesso *online* via um endereço URL /URI ou esquema similar. Se não existir recomenda‑se preencher-se com um *link* para um ponto de contacto com mais informação sobre o descarregamento do recurso.  |
| Função                                                      | Condi-cional | Não      | Define o tipo de recurso, a partir de uma lista. Não se aplica a Serviços.


**Notas**: Para os CDG é condicional à existência de um recurso online, para Serviços é obrigatório.


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Responsáveis pela Distribuição (Contacto)                              | Não      | Sim      | Informações necessárias para permitir o contacto com a pessoa / organização responsável pela distribuição do recurso. Pode conter múltiplos conjuntos de sub‑elementos:
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável. 
| Organização                                                            | Sim      | Não      | Nome da organização responsável. Poderá selecionar de uma Lista de valores ou preencher de forma livre no campo “Outra (Não Listada)” 
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável. 
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável. 
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável. 
| País                                                                   | Não      | Não      | País da pessoa ou organização responsável. 
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo. 
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo.
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo. 
| Informação *Online*                                                    | Não      | Não      | Informação *online* (endereço URL / URI) que pode ser usada como contacto individual ou institucional.


**Este elemento disponibiliza as seguintes funcionalidades / botões**: 

“Adicionar Contacto”, para adicionar um novo contacto. 

<img src="http://193.136.227.146/manual_images/100002010000002000000020A3F87039BE9D0D7E.png" width="25"> Para importar um contacto da sua Lista de Contactos para o formulário. 

<img src="http://193.136.227.146/manual_images/10000201000001B7000001B78F0FC5D379C32E50.png" width="25"> Para guardar o contacto na sua Lista de Contactos. 

<img src="http://193.136.227.146/manual_images/100002010000001700000017FBA90A52D3565DE1.png" width="25"> Para remover o contacto.


### Metadados

Informação relativa aos Metadados. Contém os seguintes elementos e sub‑elementos:


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Identificador do Ficheiro | Sim      | Não      | Identificador único do Metadado. Recomenda-se a utilização de um UUID, pode usar o botão “Gerar UUID”. |
| Data dos Metadados | Sim      | Não      | Data de criação do metadado ou da última atualização. |
| Codificação | Condicional    | Não      | Define a codificação informática de caracteres utilizada no metadado. Preencha no caso de ser diferente de “utf8”. |
| Idioma   | Sim      | Não      | Idioma utilizado no documento de metadados. Por definição é “Português”, língua oficial do projeto SNIMar. |
| Norma e Perfil de Metadados | Sim      | Não      | Perfil de Metadados que define as especificações técnicas sobre as quais os Metadados são construídos.
| Nome                        | Não      | Não      | Nome da norma de metadados utilizada. Por definição está fixo em “Perfil SNIMar”, perfil oficial do projeto SNIMar. |
| Versão                      | Não      | Não      | Versão do perfil de metadados utilizado. Por definição está fixa na versão mais atual do perfil à data da versão da extensão “EditorMetadadosMarswInforbiomares”.


| Elemento        | Obrigatório | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Responsáveis pelos Metadados (Contacto)                                | Não      | Sim      | Informações necessárias para permitir o contacto com a pessoa / organização responsável pelo Metadado. Pode conter múltiplos conjuntos dos seguintes sub‑elementos:
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável.
| Organização                                                            | Sim      | Não      | Nome da organização responsável. Poderá selecionar de uma Lista de valores ou preencher de formal livre no campo “Outra (Não Listada)” 
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável.
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável.
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável.
| País                                                                   | Não      | Não      | País da pessoa ou organização responsável.  
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo. 
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo.
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo.
| Informação *Online*                                                    | Não      | Não      | Informação *online * (endereço URL / URI) que pode ser usada como contacto individual ou institucional.


**Este elemento disponibiliza as seguintes funcionalidades / botões**: 

“Adicionar Contacto”, para adicionar um novo contacto. 

<img src="http://193.136.227.146/manual_images/100002010000002000000020A3F87039BE9D0D7E.png" width="25"> Para importar um contacto da sua Lista de Contactos para o formulário. 

<img src="http://193.136.227.146/manual_images/10000201000001B7000001B78F0FC5D379C32E50.png" width="25"> Para guardar o contacto na sua Lista de Contactos. 

<img src="http://193.136.227.146/manual_images/100002010000001700000017FBA90A52D3565DE1.png" width="25"> Para remover o contacto.


Anexo - Classificação dos Serviços
==================================

As palavras-chave têm por base a taxonomia de serviços geográficos da norma EN ISO 19119. Esta taxonomia está organizada em categorias, com as subcategorias a definir o domínio de valores da classificação de serviços de dados geográficos.


| **Código** | **Nome** | **Definição** |
| ---        | ---      | ---           |
| **100**    | **Serviços geográficos com interacção humana** 
| 101        | Visualizador de catálogo                                        | Serviço cliente que permite ao utilizador interagir com um catálogo para localizar, navegar e gerir metadados sobre dados geográficos ou serviços geográficos.
| 102        | Visualizador geográfico                                         | Serviço cliente que permite ao utilizador visualizar uma ou mais colecções de elementos geográficos ou coberturas. 
| 103        | Visualização de folhas de cálculo geográficas                   | Serviço cliente que permite ao utilizador interagir com múltiplos objectos de dados e solicitar cálculos semelhantes a uma folha de cálculo aritmética, mas alargada a dados geográficos. 
| 104        | Editor do serviço                                               | Serviço cliente que permite ao utilizador controlar serviços de processamento geográfico. 
| 105        | Editor da definição de cadeias                                  | Serviço que permite ao utilizador interagir com um serviço de definição de cadeias. 
| 106        | Gestor do fluxo de trabalho                                     | Serviço que permite ao utilizador interagir com um serviço de fluxo de trabalho.
| 107        | Editor de elementos geográficos                                 | Visualizador geográfico que permite ao utilizador interagir com os dados relativos aos elementos geográficos.  
| 108        | Editor de símbolos geográficos                                  | Serviço cliente que permite ao utilizador seleccionar e gerir bibliotecas de símbolos.  
| 109        | Editor de generalização de elementos geográficos                | Serviço cliente que permite ao utilizador modificar as características cartográficas de um elemento geográfico ou colecção de elementos geográficos simplificando a sua visualização, mas mantendo simultaneamente as suas componentes relevantes — o equivalente espacial de simplificação. 
| 110        | Visualizador da estrutura dos dados geográficos                 | Serviço cliente que permite ao utilizador aceder a parte do conjunto de dados para ver a respectiva estrutura interna. 
| **200**    | **Serviço de gestão de informação/modelos geográficos** 
| 201        | Serviço de acesso a elementos geográficos                       | Serviço que permite ao cliente o acesso e a gestão de um repositório de elementos geográficos. 
| 202        | Serviço de acesso a mapas                                       | Serviço que permite ao cliente o acesso a representações gráficas dos dados geográficos, ou seja, imagens de dados geográficos. 
| 203        | Serviço de acesso a coberturas                                  | Serviço que permite ao cliente o acesso e gestão de um repositório de coberturas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                
| 204        | Serviço de descrição de sensores                                | Serviço que fornece a descrição de um sensor de cobertura, incluindo a localização e orientação do sensor, bem como as características geométricas, dinâmicas e radiométricas do sensor, para fins de geoprocessamento. 
| 205        | Serviço de acesso a produtos                                    | Serviço que permite o acesso e gestão de um repositório de produtos geográficos.
| 206        | Serviço de tipos de elementos geográficos                       | Serviço que permite ao cliente o acesso e gestão de um repositório de definições de tipos de elementos geográficos.
| 207        | Serviço de catálogo                                             | Serviço que oferece serviços de pesquisa e gestão num repositório de metadados sobre ocorrências.
| 208        | Serviço de registo                                              | Serviço que permite o acesso a repositórios de metadados sobre tipos.
| 209        | Serviço de repertório                                           | Serviço que permite o acesso a um directório de ocorrências de uma ou várias classes de fenómenos do mundo real com alguma informação relativa à posição.
| 210        | Serviço de gestão de encomendas                                 | Serviço que permite ao cliente encomendar produtos de um fornecedor. 
| 211        | Serviço de encomendas pendentes                                 | Serviço de gestão de encomendas que permite ao utilizador solicitar que um produto sobre uma zona geográfica seja difundido logo que ficar disponível. 
| **300**    | **Serviços de gestão do fluxo de trabalho/tarefas geográficas**
| 301        | Serviço de definição de cadeia                                  | Serviço que permite definir uma cadeia e fazê-la executar pelo serviço de fluxo de trabalho.
| 302        | Serviço de fluxo de trabalho                                    | O serviço de fluxo de trabalho interpreta uma cadeia e controla a instanciação de serviços e a sequenciação de actividades. 
| 303        | Serviço de assinatura                                           | Serviço que permite aos clientes inscreverem-se para serem informados de eventos.
| **400**    | **Serviços de processamento geográfico — elementos espaciais** 
| 401        | Serviço de conversão de coordenadas                             | Serviço que permite modificar as coordenadas de um sistema de coordenadas para um outro sistema de coordenadas relacionado com o mesmo datum.  
| 402        | Serviço de transformação de coordenadas                         | Serviço que permite modificar as coordenadas de um sistema de referência de coordenadas baseado num datum para um sistema de referência de coordenadas baseado num segundo datum. 
| 403        | Serviço de conversão cobertura/vector                           | Serviço que permite mudar a representação espacial de um sistema de cobertura para um sistema vectorial, ou vice- versa.  
| 404        | Serviço de conversão de coordenadas de imagens                  | Um serviço de transformação de coordenadas ou de conversão de coordenadas que permite modificar o sistema de referência de coordenadas de uma imagem. 
| 405        | Serviço de rectificação                                         | Serviço que permite transformar uma imagem numa projecção paralela perpendicular e, por conseguinte, com uma escala constante.
| 406        | Serviço de ortorrectificação                                    | Um serviço de rectificação que corrige as deformações devidas ao ângulo de obtenção da imagem e os desvios da imagem decorrentes do relevo.
| 407        | Serviço de ajustamento do modelo geométrico dos sensores        | Serviço que permite ajustar os modelos geométricos dos sensores a fim de melhorar a correspondência da imagem com outras imagens e/ou posições no solo conhecidas.
| 408        | Serviço de conversão de modelos geométricos das imagens         | Serviço que permite converter modelos geométricos dos sensores num modelo geométrico de sensores diferente, mas equivalente.    
| 409        | Serviço de definição de subconjuntos                            | Serviço que extrai dados de uma fonte numa região espacial contínua com base na localização geográfica ou em coordenadas rectangulares. 
| 410        | Serviço de amostragem                                           | Serviço que extrai dados de uma fonte utilizando um sistema de amostragem coerente com base na localização geográfica ou em coordenadas rectangulares. 
| 411        | Serviço de modificação do seccionamento                         | Serviço que permite modificar o seccionamento dos dados geográficos. 
| 412        | Serviço de medição das dimensões                                | Serviço que calcula as dimensões de objectos visíveis numa imagem ou noutros dados geográficos.     
| 413        | Serviços de manipulação de elementos geográficos                | Estes serviços permitem inserir um elemento geográfico noutro elemento geográfico, imagem ou outro conjunto de dados ou conjunto de coordenadas, com correcção dos desvios translacionais relativos, das diferenças rotacionais, das diferenças de escala e das diferenças de perspectiva. Permitem verificar que todos os elementos geográficos da colecção de elementos geográficos são topologicamente coerentes de acordo com as regras topológicas da colecção de elementos e identifica e/ou corrige eventuais inconsistências detectadas.
| 414        | Serviço de correspondência de elementos geográficos             | Serviço que determina quais são os elementos geográficos ou partes de elementos geográficos provenientes de múltiplas fontes de dados que representam a mesma entidade do mundo real, como acontece na coincidência de limites («edge matching») e na fusão parcial de elementos geográficos («limited conflation»).    
| 415        | Serviço de generalização de elementos geográficos               | Serviço que reduz a variação espacial numa colecção de elementos geográficos a fim de aumentar a eficácia da comunicação mediante a neutralização dos efeitos indesejáveis da redução de dados.   
| 416        | Serviço de determinação do itinerário                           | Serviço que determina o trajecto óptimo entre dois pontos especificados com base nos parâmetros de entrada e nas propriedades contidas na colecção de elementos geográficos. 
| 417        | Serviço de localização                                          | Serviço fornecido por um dispositivo de localização que permite utilizar, obter e interpretar sem ambiguidades as informações relativas à localização e que determina se os resultados satisfazem os requisitos de utilização.  
| 418        | Serviço de análise de proximidade                               | A partir de uma determinada localização ou elemento geográfico, este serviço encontra todos os objectos com um determinado conjunto de atributos que estão localizados a uma distância definida pelo utilizador relativamente à localização ou ao elemento geográfico. 
| **500**    | **Serviços de processamento geográfico — elementos temáticos** 
| 501        | Serviço de cálculo de geoparâmetros                             | Serviço que permite obter resultados quantitativos centrados em aplicações que não podem ser obtidos a partir dos próprios dados em bruto.  
| 502        | Serviço de classificação temática                               | Serviço que classifica regiões de dados geográficos com base em atributos temáticos. 
| 503        | Serviço de generalização de elementos geográficos               | Serviço que generaliza os tipos de elementos geográficos numa colecção de elementos geográficos para aumentar a eficácia da comunicação mediante a neutralização dos efeitos indesejáveis da redução de dados.
| 504        | Serviço de definição de subconjuntos                            | Serviço que permite extrair dados a partir de uma fonte baseada em valores de parâmetros.   
| 505        | Serviço de contagem geográfica                                  | Serviço que permite contar os elementos geográficos.  
| 506        | Serviço de detecção de alterações                               | Serviço que permite encontrar diferenças entre dois conjuntos de dados que representam a mesma zona geográfica em momentos diferentes.   
| 507        | Serviços de extracção de informação geográfica                  | Serviços que permitem a extracção de elementos geográficos e de informações sobre o terreno a partir de imagens rasterizadas ou provenientes de sensores remotos. 
| 508        | Serviço de processamento de imagens                             | Serviço que permite modificar os valores dos atributos temáticos de uma imagem utilizando uma função matemática.      
| 509        | Serviço de redução de resolução                                 | Serviço que permite diminuir a resolução de uma imagem. 
| 510        | Serviços de manipulação de imagens                              | Serviços que permitem manipular os dados das imagens: modificação dos valores de cor e contraste, aplicação de vários filtros, manipulação da resolução da imagem, eliminação de ruído, eliminação do efeito de «striping», correcções radiométricas sistemáticas, atenuação atmosférica, modificações na iluminação da imagem, etc.  
| 511        | Serviços de compreensão de imagens                              | Serviços que permitem a detecção automática de alterações entre imagens, o cálculo de diferenças entre imagens co- registadas, a análise e visualização da significância estatística da diferença entre imagens e o cálculo de diferenças entre imagens baseado em áreas e modelos.
| 512        | Serviços de síntese de imagens                                  | Serviços que permitem criar ou transformar imagens utilizando modelos espaciais em computador, transformações de perspectiva e manipulações de características da imagem para melhorar a sua visualização e resolução e/ou reduzir os efeitos da cobertura de nuvens ou da neblina.
| 513        | Serviços de manipulação de imagens multibandas                  | Serviços que permitem modificar uma imagem utilizando as suas várias bandas.
| 514        | Serviço de detecção de objectos                                 | Serviço que permite identificar objectos do mundo real numa imagem.
| 515        | Serviço de geoidentificação                                     | Serviço que permite procurar em documentos textuais referências a locais, como topónimos, endereços, códigos postais, etc., para fins de preparação da passagem para um serviço de geocodificação.    
| 516        | Serviço de geocodificação                                       | Serviço que permite complementar referências textuais baseadas na localização com coordenadas geográficas (ou outra referência espacial).   
| **600** | **Serviços de processamento geográfico — elementos temporais**   
| 601     | Serviço de transformação do sistema de referência temporal     | Serviço que permite modificar os valores das ocorrências temporais de um sistema de referência temporal para outro sistema de referência temporal.   
| 602     | Serviço de definição de subconjuntos                           | Serviço que permite extrair dados de uma fonte num intervalo contínuo com base em valores de posição temporal.    
| 603     | Serviço de amostragem                                          | Serviço que permite extrair dados de uma fonte por meio de um sistema de amostragem coerente baseado em valores de localização temporal.  
| 604     | Serviço de análise de proximidade temporal                     | A partir de um determinado intervalo de tempo ou evento, este serviço encontra todos os objectos com um determinado conjunto de atributos que estão localizados dentro de um intervalo definido pelo utilizador em relação ao referido intervalo ou evento.
| **700** | **Serviços de processamento geográfico – metadados**  
| 701     | Serviço de cálculo estatístico                                 | Serviço que permite calcular as estatísticas de um conjunto de dados. 
| 702     | Serviços de anotação geográfica                                | Serviços que permitem acrescentar informação auxiliar a uma imagem ou elemento geográfico numa colecção de elementos geográficos.  
| **800** | **Serviços de comunicação geográfica**    
| 801     | Serviço de codificação                                         | Serviço que permite a execução de uma regra de codificação e proporciona uma interface para a funcionalidade de codificação e de descodificação.
| 802     | Serviço de transferência                                       | Serviço que permite executar um ou mais protocolos de transferência, a fim de transferir dados entre sistemas de informação distribuídos através de meios de comunicação fora de linha ou em linha.  
| 803     | Serviço de compressão geográfica                               | Serviço que permite converter partes espaciais de uma colecção de elementos geográficos para formato comprimido, e vice-versa.         
| 804     | Serviço de conversão de formato geográfico                     | Serviço que permite a conversão de um formato de dados geográficos para outro. 
| 805     | Serviço de transmissão de mensagens                            | Serviço que permite simultaneamente a vários utilizadores visualizar e comentar colecções de elementos geográficos e solicitar revisões das mesmas.
| 806     | Gestão remota de ficheiros e de executáveis                    | Serviço que permite o acesso a um sistema secundário de armazenamento de elementos geográficos como se este fosse um recurso local do cliente.
