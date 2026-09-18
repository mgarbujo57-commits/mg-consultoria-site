# MG Consultoria — Site Python + Flask

## Teste local

1. Instale Python 3.10 ou superior.
2. Abra o terminal dentro desta pasta.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python app.py
```

5. Abra no navegador:

http://localhost:5000

## Publicação em nuvem

Para serviços que aceitam aplicações Flask, use:

```bash
gunicorn app:app
```

## Personalizações importantes

- O número do WhatsApp está no arquivo `templates/index.html`.
- O e-mail está no arquivo `templates/index.html`.
- O formulário atualmente exibe uma confirmação e imprime os dados no terminal.
- Para uso real, conecte o formulário a um e-mail, banco de dados ou CRM.
- O CSS usa Google Fonts; se a hospedagem bloquear fontes externas, o site continua funcionando com fontes alternativas.
