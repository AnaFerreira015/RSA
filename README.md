<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Bras%C3%A3o_Ufal.png/1200px-Bras%C3%A3o_Ufal.png" width="200px"/>
</p>

# :closed_lock_with_key: Criptografia RSA

Implementação do algorítmo de criptografia RSA (Rivest-Shamir-Adleman) para a disciplina de Matemática Discreta da Universidade Federal de Alagoas - UFAL

# :scroll: Informações Gerais

O algoritmo foi desenvolvido com [Python 3.x](https://www.python.org). Nenhuma biblioteca externa ao pacote padrão foi usada no desenvolvimento do código.

## :interrobang: Como utilizar?

Primeiro passo é rodar o arquivo [main.py](main.py) que é o ponto de partida do algorítmo;

```
python main.py
```

Ao iniciar o arquivo, um menu será exibido contendo 4 opções;

```
Escolha uma opção:

[1] Gerar chave pública
[2] Criptografar
[3] Descriptografar
[0] Sair
```

Basta escolher a opção desejada e seguir os passos que serão mostrados.

## :heavy_exclamation_mark: Pontos Importantes

1. Para realizar o passo **[2] Criptografar**, é necesário um arquivo de texto chamado _public_key.txt_ que conterá os valores de _n_ e _e_ respectivamente e serão utlizados nos passos de criptografar mensagem.

    :warning: Caso não exista esse arquivo no seu diretório, basta escolher a opção **[1] Gerar Chave Pública** no menu principal, preencher os dados necessários e o arquivo será gerado automaticamente.

2. Para realizar o passo **[3] Descriptografar**, é necessário um arquivo chamado _excrypted_message.txt_. Que é de onde o programa irá ler a mensagem criptografada e realizar as etapas para descriptografar e mostrar na tela para o usuário.

    :warning: Caso não exista esse arquivo no seu diretório, existem duas opções:

    1. **Se você já tiver um texto criptografado e deseja somente descriptografar:** Basta criar o arquivo _encrypted_message.txt_ manualmente e colocar o texto criptografado lá dentro, separando cada número com vírgula.

    ```
    11, 27, 18, 7, 14, 6, 8, 7, 18, 14, 5, 22, 11
    ```

    2. **Se você deseja criptografar e logo após descriptografar uma mensagem:** Então basta você seguir os passos **[2] e [3]** do menu.

# :raising_hand: Participantes

-   Ana Ferreira
-   Frederico Guilherme
-   Lucas Tenório
-   Phyllipe Bezerra
-   Rafael Augusto
