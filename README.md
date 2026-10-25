# cnpj_validador

O **cnpj_validador** é uma biblioteca Python leve, rápida e sem dependências externas desenvolvida para validar CNPJs nos dois formatos aceitos pela Receita Federal: o modelo tradicional (**antigo/numérico**) e o novo modelo (**alfanumérico**).

## 🚀 Recursos

- **Pronta para Produção:** Biblioteca publicada e utilizável em qualquer aplicação Python (Web, APIs, Scripts, Relatórios).
- **Validação Unificada:** Suporta os formatos antigo (apenas números) e novo (alfanumérico).
- **Flexível:** Aceita strings com ou sem formatação (pontuação, barras e traços).
- **Zero Dependências:** Código puro, rápido e seguro.

## 📦 Instalação

Você pode instalar a biblioteca de forma global ou no ambiente virtual de qualquer projeto via `pip`:

```bash
pip install cnpj_validador
```

## 💻 Como Usar em Seus Projetos

Para utilizar a validação em seus próprios sistemas, basta importar a função e passar o documento como string:

```python
from cnpj_validador import validar_cnpj

# Usando em um CNPJ no novo formato alfanumérico
if validar_cnpj("12.ABC.345/01DE-35"):
    print("O CNPJ é válido!")
else:
    print("O CNPJ é inválido!")

# Também aceita o formato numérico tradicional com ou sem máscara
resultado = validar_cnpj("00394460000141") 
```

## 🛠️ Como Testar Localmente (No código-fonte)

O projeto também inclui um script de testes pronto para ser executado no terminal de desenvolvimento.

1. Certifique-se de ter instalado o pacote localmente na pasta raiz:
```bash
pip install -e .
```

2. Execute o arquivo de testes que está na raiz do projeto:
```bash
python teste.py
```

3. Digite qualquer CNPJ (antigo ou novo alfanumérico) direto no prompt do terminal para obter o retorno em tempo real:
```text
Digite um cnpj para ser validado: 12.ABC.345/01DE-35
✅ Sucesso: O CNPJ Alfanumérico '12.ABC.345/01DE-35' é VÁLIDO!
```

## ⚙️ Regra de Validação

A biblioteca segue estritamente a regulamentação oficial da Receita Federal do Brasil (Nota Técnica Conjunta nº 2025/001), onde o valor decimal corresponde ao código ASCII de cada caractere menos 48 antes do cálculo dos dígitos verificadores por meio do módulo 11.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
