# Client UDP 
Um cliente UDP é um programa ou dispositivo que utiliza o protocolo UDP (User Datagram Protocol) para se comunicar com um servidor ou outro dispositivo em uma rede. O UDP é um protocolo de transporte simples e sem conexão, que permite a transmissão de dados sem a necessidade de estabelecer uma conexão prévia, como ocorre no TCP (Transmission Control Protocol).

Características do UDP:
Sem conexão: Não há handshake inicial (como no TCP) para estabelecer uma conexão.

Leve e rápido: Como não há garantia de entrega, ordenação ou controle de fluxo, o UDP é mais rápido e consome menos recursos.

Não confiável: Os pacotes podem ser perdidos, duplicados ou chegar fora de ordem.

Ideal para aplicações sensíveis ao tempo: Como streaming de vídeo, VoIP (voz sobre IP) ou jogos online, onde a velocidade é mais importante do que a confiabilidade.

Funcionamento de um Cliente UDP:
Um cliente UDP envia datagramas (pacotes de dados) para um servidor UDP especificando o endereço IP e a porta de destino. O servidor UDP recebe esses pacotes e pode responder de volta, mas não há garantia de que os pacotes chegarão ao destino ou que chegarão na ordem correta.

William Tormen -> https://williamtormen.com.br