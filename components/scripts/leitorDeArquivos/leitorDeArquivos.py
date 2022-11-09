def main():
    vetorTempo = [];
    # ler arquivo e escrever os elementos sem a quebra de linha em outro arquivo
    with open("./components/leituradeArquivos/t.txt", encoding="utf8", errors='ignore') as tempo:
        for line in tempo:
            vetorTempo.append(line.split('\n')[0]);
    tempo.close();
    # escrever os elementos em outro arquivo separados por vírgula
    tempo = open("./t.txt", "w");
    for i in range(len(vetorTempo)):
        tempo.write(vetorTempo[i] + ",");
    tempo.close();

    # agora com o arquivo x.txt, ler o arquivo e escrever os elementos sem a quebra de linha em outro arquivo
    vetorX = [];
    with open("./components/leituradeArquivos/x.txt", encoding="utf8", errors='ignore') as x:
        for line in x:
            vetorX.append(line.split('\n')[0]);
    x.close();
    # escrever os elementos em outro arquivo separados por vírgula
    x = open("./x.txt", "w");
    for i in range(len(vetorX)):
        x.write(vetorX[i] + ",");
    x.close();

    # agora com o arquivo y.txt, ler o arquivo e escrever os elementos sem a quebra de linha em outro arquivo
    vetorY = [];
    with open("components/leituradeArquivos/y.txt", encoding="utf8", errors='ignore') as y:
        for line in y:
            vetorY.append(line.split('\n')[0]);
    y.close();
    # escrever os elementos em outro arquivo separados por vírgula
    y = open("./y.txt", "w");
    for i in range(len(vetorY)):
        y.write(vetorY[i] + ",");
    y.close();
main()