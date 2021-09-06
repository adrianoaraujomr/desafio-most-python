# Desafio MOST

### Objetivo

Fazer uma aplicação que tentar remover ao máximo o espaço em branco ao redor de uma imagem.

### Rodar programa

Para rodar o servidor deve-se ter o python instalado. Com o pip deve-se instalar as bibliotecas presentes no arquivo `requirements.txt` com elas instaladas basta usar o comando:

``` 
python run.py
``` 

Com o servidor flask rodando basta fazer as requisições. No diretorio /postman tem uma collection com exemplo de requisicao que é aceita, um POST em que o body é uma imagem no formato binário.

### Processo

O processo para desenvolvimento da solução foi primeiramente buscar na internet como se poderia resolver o problema em questão. Foi descoberto que uma forma de resolver esse problema é fazer a binarição da imagem e usar das funções prontas do opencv para encontrar o retângulo que contem o conteúdo da imagem. O que foi em suma o que foi feito. O que foi adicionado a mais foi um passo para remoção de noise, consitindo em um algorimto para fazer essa redução e também os algoritmos de erosão seguido por dilatação que também podem remover ruídos.
