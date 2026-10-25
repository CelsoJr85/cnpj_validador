import re
from cnpj_validador import validar_cnpj

print("--- Iniciando Testes do cnpj_validador ---")

# Captura o CNPJ direto digitado pelo usuário no terminal
cnpj = input("Digite um cnpj para ser validado: ")

# ==========================================
# ETAPA 1: PROCESSAMENTO E VERIFICAÇÃO
# ==========================================
is_null = cnpj is None or str(cnpj).strip() == ""

if not is_null:
  cnpj_limpo = re.sub(r"[^A-Za-z0-9]", "", str(cnpj))
  eh_alfanumerico = any(c.isalpha() for c in cnpj_limpo)
  is_valido = validar_cnpj(cnpj)
else:
  eh_alfanumerico = False
  is_valido = False

# ==========================================
# ETAPA 2: RETORNO DE RESULTADOS (IF/ELIF/ELSE)
# ==========================================
if is_null:
  print("❌ Erro: Insira um CNPJ válido! O campo está vazio.")
elif is_valido:
  if eh_alfanumerico:
    print(f"✅ Sucesso: O CNPJ Alfanumérico '{cnpj}' é VÁLIDO!")
  else:
    print(f"✅ Sucesso: O CNPJ Tradicional '{cnpj}' é VÁLIDO!")
else:
  print(f"❌ Erro: O CNPJ '{cnpj}' é INVÁLIDO!")
