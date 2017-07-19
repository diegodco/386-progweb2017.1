'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.
'''
texto = "The Python Software Foundation and the global Python" \
        "community welcome and encourage participation by everyone. Our community is based on" \
        "mutual respect, tolerance, and encouragement, and we are working to help each other live up" \
        "to these principles. We want our community to be more diverse: whoever you are, and" \
        "whatever your background, we welcome you.".lower()
palavras = texto.lower().split()
palavras_com_python = []
for x in range(len(palavras)):
    palavras[x] = palavras[x].replace(':', '')
    palavras[x] = palavras[x].replace(',', '')
    palavras[x] = palavras[x].replace('.', '')
    if palavras[x][:1] in 'python':
        palavras_com_python.append(palavras[x])
    elif palavras[x][-1:] in 'python':
        palavras_com_python.append(palavras[x])
print(palavras_com_python)
