# -*- coding: utf-8 -*-        #este código é pra apresentar acentos nas palavras


#importamos a Biblioteca do ChatBot
from chatterbot.trainers import ListTrainer    
#importamos a Biblioteca do ChatBot



#importamos agora o chatBot
from chatterbot import ChatBot       
#importamos agora o chatBot



#Definimos uma variável para o nosso chatBot
bot=ChatBot('Meu ChatBot')
#Definimos uma variável para o nosso chatBot



#Criamos um mini banco de palavras pro nosso ChatBot Começar a aprender em cima delas
ListaDePalavras=['oi','olá','bom dia','Muito bom dia',
                 'estou bem','fico feliz','qual a razão da vida?',
                 'não sei','você é legal','Você também é legal']
#Criamos um mini banco de palavras pro nosso ChatBot Começar a aprender em cima delas



#Definimos o treinamento em Listas
bot.set_trainer(ListTrainer)
#Definimos o treinamento em Listas



#Colocamos o Bot pra treinar em cima das palavras que colocamos la na linha 23,24 e 25
bot.train(ListaDePalavras)
#Colocamos o Bot pra treinar em cima das palavras que colocamos la na linha 23,24 e 25



while True:
     #Iniciamos sempre esperando o usuário digitar alguma coisa
    Pergunta=input('Você: ')     
     #Iniciamos sempre esperando o usuário digitar alguma coisa
     
     
     #Definimos a resposta do Bot em cima da pergunta que fizermos,por isso é legal    
    Resposta=bot.get_response(Pergunta)#       colocarmos perguntas e respostas coerentes
                                                   
    
    #Agora imprimimos na tela a resposta que o Bot separou pra gente
    print('Bot: ',Resposta)
     #Agora imprimimos na tela a resposta que o Bot separou pra gente

