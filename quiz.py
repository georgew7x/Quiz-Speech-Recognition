# bibliotecas importadas
import speech_recognition as sr
import time

# funcao que da inicio ao quiz
def ouvir_microfone():
    # o microfone eh chamado, ajustado e o participante eh introduzido ao programa
    microfone = sr.Recognizer()
    with sr.Microphone() as source:  
        microfone.adjust_for_ambient_noise(source)
        print("\n" * 20)
        print("Esse quiz usa comandos por voz. Fale perto do microfone! :)")
        time.sleep(2)
        print("Qual o seu nome? ")
        audio = microfone.listen(source)
        nome = microfone.recognize_google(audio,language='pt-BR')
        print("\n" * 10)     
        print("Voce pode responder o quiz dizendo, por exemplo: 'opção A', 'letra A', ou a resposta em si!")
        time.sleep(5)
        print(f"Inicio do Quiz. Boa Sorte, {nome}!")
        time.sleep(2)
        print('3...'),time.sleep(1),print('2...'),time.sleep(1),print('1...'),time.sleep(2)
        print("\n" * 10)
        
        try:    
            # as questoes iniciam, somando pontos a cada acerto 
            pontos = 0
            print('Questao 1: De quem é a famosa frase “Penso, logo existo”?'),print(''),print('Opcao A: Socrates'),print('Opcao B: Descartes'),print('Opcao C: William Shakespere')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 1: De quem é a famosa frase “Penso, logo existo”?'),print(''),print('Opcao A: Socrates'),print('Opcao B: Descartes'),print('Opcao C: William Shakespere'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("\n" * 10)              
            if "Descartes" in frase or "opção b" in frase or "letra b" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, essa frase é de autoria de Descartes...")
            
            print('Questao 2: De onde é a invenção do chuveiro eletrico?'),print(''),print('Opcao A: Canada'),print('Opcao B: Alemanha'),print('Opcao C: Brasil')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 2: De onde é a invenção do chuveiro eletrico?'),print(''),print('Opcao A: Canada'),print('Opcao B: Alemanha'),print('Opcao C: Brasil'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR') 
            print("\n" * 10)             
            if "Brasil" in frase or "opção C" in frase or "letra c" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, o chuveiro eletrico foi inventado no Brasil...")
            
            print('Questao 3: Qual o maior pais do mundo?'),print(''),print('Opcao A: India'),print('Opcao B: Estados Unidos'),print('Opcao C: Russia')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 3: Qual o maior pais do mundo?'),print(''),print('Opcao A: India'),print('Opcao B: Estados Unidos'),print('Opcao C: Russia'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("\n" * 10)              
            if "Rússia" in frase or "opção C" in frase or "letra c" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, o maior pais do mundo eh a Russia...")
            
            print('Questao 4: Qual o menor pais do mundo?'),print(''),print('Opcao A: Vaticano'),print('Opcao B: Coreia do Sul'),print('Opcao C: Equador')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 4: Qual o menor pais do mundo?'),print(''),print('Opcao A: Vaticano'),print('Opcao B: Coreia do Sul'),print('Opcao C: Equador'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("\n" * 10)              
            if "Vaticano" in frase or "Vaticano" in frase or "opção a" in frase or "letra a" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta certa eh Vaticano...")
            
            print('Questao 5: Qual o maior animal do mundo?'),print(''),print('Opcao A: Elefante'),print('Opcao B: Baleia-Azul'),print('Opcao C: Girafa Masai')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 5: Qual o maior animal do mundo?'),print(''),print('Opcao A: Elefante'),print('Opcao B: Baleia-Azul'),print('Opcao C: Girafa Masai'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')  
            print("\n" * 10)            
            if "baleia azul" in frase or "opção b" in frase or "letra b" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, o maior animal do mundo eh a Baleia-Azul...")
            
            print('Questao 6: Quem foi o presidente dos Estados Unidos entre 2009 e 2017?'),print(''),print('Opcao A: Barack Obama'),print('Opcao B: Donald Trump'),print('Opcao C: John F. Kennedy')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 6: Quem foi o presidente dos Estados Unidos entre 2009 e 2017?'),print(''),print('Opcao A: Barack Obama'),print('Opcao B: Donald Trump'),print('Opcao C: John F. Kennedy'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("\n" * 10)              
            if "Obama" in frase or "opção a" in frase or "letra a" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta correta era Barack Obama...")
            
            print('Questao 7: Qual a religiao monoteista com o maior numero de adeptos no mundo?'),print(''),print('Opcao A: Islamismo'),print('Opcao B: Hinduismo'),print('Opcao C: Cristianismo')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 7: Qual a religiao monoteista com o maior numero de adeptos no mundo?'),print(''),print('Opcao A: Islamismo'),print('Opcao B: Hinduismo'),print('Opcao C: Cristianismo'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("\n" * 10)              
            if "cristianismo" in frase or "opção C" in frase or "letra c" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta certa seria Cristianismo...")
            
            print('Questao 8: Como se chamam os vasos que transportam sangue do coraçao para a periferia do corpo?'),print(''),print('Opcao A: Veias'),print('Opcao B: Aorta'),print('Opcao C: Arterias')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 8: Como se chamam os vasos que transportam sangue do coraçao para a periferia do corpo?'),print(''),print('Opcao A: Veias'),print('Opcao B: Aorta'),print('Opcao C: Arterias'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR') 
            print("\n" * 10)             
            if "artérias" in frase or "opção C" in frase or "letra c" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta correta seria Arterias...")
            
            print('Questao 9: Qual o metal cujo simbolo quimico é o Au?'),print(''),print('Opcao A: Ouro'),print('Opcao B: Mercurio'),print('Opcao C: Aluminio')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 9: Qual o metal cujo simbolo quimico é o Au?'),print(''),print('Opcao A: Ouro'),print('Opcao B: Mercurio'),print('Opcao C: Aluminio'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR')   
            print("\n" * 10)           
            if "ouro" in frase or "opção a" in frase or "letra a" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta certa era Ouro...")

            print('Questao 10: Em que seculo o continente europeu foi devastado pela peste bubonica?'),print(''),print('Opcao A: Seculo 11'),print('Opcao B: Seculo 5'),print('Opcao C: Seculo 14')
            print('3...'),time.sleep(3),print('2...'),time.sleep(3),print('1...'),time.sleep(3)
            print("\n" * 10)
            print('Questao 10: Em que seculo o continente europeu foi devastado pela peste bubonica?'),print(''),print('Opcao A: Seculo 11'),print('Opcao B: Seculo 5'),print('Opcao C: Seculo 14'),print(''),print('Ouvindo...'),print('')
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio,language='pt-BR') 
            print("\n" * 10)             
            if "14" in frase or "quatorze" in frase or "opção C" in frase or "letra c" in frase:
                print("Você acertou!")
                pontos = pontos + 1
            else:
                print("Você errou, a resposta certa era Seculo 14...")
        # ao fim das questoes a pontuacao do participante eh registrada em um arquivo txt
            print(f'Voce pontuou {pontos} questoes de 10.')
            if pontos >= 7:
                print('Meus parabens!')
            else:
                print('Estude mais.')
            with open(r"historico.txt","r") as arquivo:
                texto=arquivo.read()
            with open(r"historico.txt","w") as arquivo:
                arquivo.write(texto+f"\r{nome} pontuou {pontos}/10")
        # caso o speech_recognition nao reconheca o que foi dito, essa excessao vai informar que houve um erro e vai reiniciar as questoes
        except sr.UnknownValueError:
            print('Erro inesperado, reiniciando o quiz...'),time.sleep(5)
            ouvir_microfone()
            return frase

while True:
    print("-------------"),print("1 - Começar Quiz"),print("2 - Ver historico"),print("3 - Sair"),print("-------------")
    o=input("Digite o numero: ")
    if o == "1":
        ouvir_microfone()
    elif o == "2":
        with open(r"historico.txt","r") as arquivo:
            texto=arquivo.read()
            print("\n" * 10) 
            print(f"Historico:\n",texto)
    elif o == "3":
        exit()
    else:
        print("\n" * 10)
        print("Opcao invalida")