# cnpj_validador

O **cnpj_validador** é uma biblioteca Python leve, rápida e sem dependências externas desenvolvida para validar CNPJs nos dois formatos aceitos pela Receita Federal: o modelo tradicional (**antigo/numérico**) e o novo modelo (**alfanumérico**).

## 🚀 Recursos

- **Validação Unificada:** Suporta os formatos antigo (apenas números) e novo (alfanumérico).
- **Flexível:** Aceita strings com ou sem formatação (pontuação, barras e traços).
- **Zero Dependências:** Código puro, rápido e seguro.

## 📦 Instalação

Após a publicação no PyPI, você poderá instalar a biblioteca via `pip`:

```bash
pip install cnpj_validador
```

## 🛠️ Como Usar e Testar

O projeto já inclui um script de testes pronto para ser executado no terminal.

1. Certifique-se de ter instalado o pacote localmente:
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

A biblioteca segue estritamente a regulamentação oficial da Receita Federal do Brasil, onde os caracteres alfanuméricos das posições correspondentes são convertidos para valores de 10 a 35 (A=10, B=11, ..., Z=35) antes do cálculo dos dígitos verificadores por meio do módulo 11.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
