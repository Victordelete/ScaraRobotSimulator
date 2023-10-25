# Robot Simulator SAC: Simulation Analyze and Control

## Resumo

Arquivo auxiliar para testes do programa de simulação de um robô SCARA. O programa tem o intuito de auxiliar a programação offline deste robô, para a criação de trajetórias complexas e funcionais. O programa permite que arquivos sejam criados, editados e compilados para uma pseudo linguagem de controle do robô, sendo possível tanto simulação como controle do robô. 

![Interface](/img/interface.png)

A interface é composta por representação gráfica do robô em plot 3D, janela para edição de texto e quadro para representação do log de funcionamento do software. 

Mais informações podem ser coletadas no meu [Trabalho de Graduação](https://bdm.unb.br/bitstream/10483/32491/1/2021_VictorHugoMarquesVieira_tcc.pdf), onde o software é analisado em seus mais diversos aspectos. 

## Pseudo compilador

A linguagem de programação implementada para controle do robô associa comandos a um valor númerico, que é interpretado em comandos para a engine de simulação, e para o controlador eletrõnico caso seja o requerido. 

Os comandos implementados são: 

1. move ângulo1 angulo2 altura
    1. move o braço para o ponto por cinemática direta.
2. pmove X Y altura
    1. move o braço para o ponto equivalente a posição X,Y,Z pela cinemática inversa.
3. down
    1. move o efetuador terminal para seu ponto mais baixo.
4. up
    1. move o efetuador terminal para seu ponto mais alto.
5. home
    1. move o braço para o estado inicial (0,0,0)

São apresentadas junto ao software alguns arquivos de teste para da simulação. Estes arquivos, assim como novos, devem ser mantidos na pasta raíz do programa, tanto para acionamento direto como acionamento via imagem docker. 

## Construção gráfica 

O robô tem sua construção gráfica proporcional a um robô real, mantendo as delimitações mecânicas. Foi construído um modelo em CAD do robô, e exportado os pontos e conexões de triangulo. 

Estes pontos são armazenados nos arquivos de construção [apresentados](/App/VisualData/), com algoritmo de conversão do mesmo em modelo de apresentação de dado em 3D do Matplotlib. Utiliza-se de construção animada do gráfico para gerar as movimentações necessárias para simular o funcionamento do robô. 

## Controle real

O software inicialmente tem a intenção de simulação e controle do robô real. Devido a atualização atual não ter disponibilidade o robõ para testes, a conexão serial que possibilitava este controle não pode ser testada.

## Acionamento Docker

Para simplificar os testes por outros usuários foi configurado uma imagem Docker com as versões necessários para funcionamento do software. Decidiu-se por isso, para facilitar testes e futuras implementações.

Como há acionamento de intervenção gráfica, é necessário a configuração de um servidor para apresentação da interface a imagem docker. Recomenda-se para isso o [Xlaunch](https://sourceforge.net/projects/xming/), servido recomendado para esta demanda.

Seguem comandos para construção e acionamento da imagem. 

```
docker build -t rsac_image .

set-variable -name DISPLAY -value 192.168.56.11:0.0

docker run -ti --rm -e DISPLAY=$DISPLAY rsac_image
```

Salientando que é necessário a alteração do IP de display pelo da máquina com conexão ao servidor. 