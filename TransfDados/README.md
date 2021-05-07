# Segundo Teste: Transformação de Dados

Para o teste de transformação de dados foi utilizado a linguagem python e também a lib camelot que tem o objetivo de fazer a leitura do pdf, buscar as tabelas nas páginas selecionadas e transformar os resultados em dataframes do pandas e exportá-los em csv. também foi utilizado a lib shutil que tem o objetivo de comprimir a pasta Teste_Intuitive_Care_Gustavo_Abel em zip e por fim a lib pathlib import Path com o objetivo de criar caminhos do sistema compatíveis em diferentes sistemas operacionais.
 
 ## Ferramentas Necessárias
 Deverá ter o python instalado na máquina, instalar o pip (gerenciador de pacotes) e também instalar todas as libs utilizadas com o gerenciador de pacotes da linguagem (pip).
 
 ### Rodando e executando a transformação dos dados
 ```bash
 $ sudo apt install python3-pip
 $ pip3 install "camelot-py[cv]"
 $ python3 main.py
 ```
 E então conforme instruído o script irá gerar a pasta Teste_Intuitive_Care_Gustavo_Abel.zip com todos os quadros solicitados dentro dela.
 
