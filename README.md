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

## 🛠️ Como Usar

Basta importar a função `validar_cnpj` e passar o documento como string. A função retorna `True` para documentos válidos e `False` para inválidos.

```python
from cnpj_validador import validar_cnpj

# Testando formato alfanumérico (Novo)
print(validar_cnpj("12.ABC.345/0001-XX"))  # Retorna True ou False

# Testando formato tradicional apenas números (Antigo)
print(validar_cnpj("12.345.678/0001-00"))  # Retorna True ou False

# Também aceita strings sem pontuação
print(validar_cnpj("12ABC3450001XX"))       # Retorna True ou False
```

## ⚙️ Regra de Validação

A biblioteca segue estritamente a regulamentação oficial da Receita Federal do Brasil, onde os caracteres alfanuméricos das posições correspondentes são convertidos para valores de 10 a 35 (A=10, B=11, ..., Z=35) antes do cálculo dos dígitos verificadores por meio do módulo 11.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
