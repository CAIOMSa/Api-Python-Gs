# API de Monitoramento e Controle de Energia
##Global Solution Semestre 1 - Caio, Junior e Wesley
 * Caio Martinez Saes RM: 560753
 * Wesley Santos Zimmer RM: 560264
 * José Claudio da Silva Junior RM: 559680

## Descrição
Este projeto, em python, tem como objetivo armazenar e mostrar informações obtidades a partir dados de um ESP32 e um WebSite.

## Funcionalidades Principais
* Armazenagem de dados: Recebe dados de um WebSite e de uma placa Esp32 e armazena eles em um csv.
* Envio de dados da API: Realiza tratamento dos dados armazenados para um endpoint GET usado no WebSite.
* Tratamento de erros: O sistema implementa mecanismos para lidar com erros comuns, como a indisponibilidade da API.

## Requisitos
* **Software:**
    * Python instalado com as dependencias do projeto

## Instalação e Configuração
1. **Baixar o repositório:** Baixe este repositório (Opcional) e o repositório do WebSite
2. **Baixa as dependências:** Instale as bibliotecas do python utilizando pip install.
3. **(Opcional)Verifique o endereço da api:** Corrija se necessário o caminho da api contido no Web site e esp32 físico.

## Uso
2. **Hardware:** Carregar o código adaptado para ter a conexão com a rede e para a placa esp32 física e conectar os componentes.
2. **Api:** Executar a api em dispositivo que esteja na mesma rede da placa física ou hospedado em servidor.
4. **Início:** Ligar a placa e iniciar o sistema.

## Dependências
* **Bibliotecas:** Pandas, Flask, Json, datetime


## Informações Adicionais
* **Melhorias futuras:** Hospedar a api em um servidor.

## Link dos demais repositorios:
* https://github.com/juniorlds98/Global-Solution-S1/tree/main/Projeto
* https://github.com/CAIOMSa/Arduino-Gs/tree/main


## Endpoints da Api:
### Login
* Post:
  * **url:** http://localhost:5000/Login
  * **header:** Content-Type application/json
  * json:
      {
      	"Nome":"teste",
      	"Senha":"12345t"
      }
### Meta
* Post:
  * **url:** http://localhost:5000/Meta
  * **header:** Content-Type application/json
  * json:
        {
        "IdUser":  1,
        "Meta":  "10",
        "Month":  "10",
        }
### Energia
* Post:
  * **url:** http://localhost:5000/Energia
  * **header:** Content-Type application/json
  * json:
        {
        "IdUser":  1,
        "Produzido":  "68.00",
        "Gasto":  "34.00",
        "Armazenado":  "3.00",
        "Distribuido":  "31.00"
        }
* Get:
  * **url:** http://localhost:5000/Energia?id=1
