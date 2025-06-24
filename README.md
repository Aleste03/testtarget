 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/README.md
index 0000000000000000000000000000000000000000..281bfa5656306cdbad4b147115478d1998ed467d 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,16 @@
+# Calculadora de Renda Mensal
+
+Este repositório inclui uma página web simples para estimar o valor acumulado e a renda mensal de um investimento.
+
+## Como executar
+
+1. Abra o terminal na pasta do projeto.
+2. Rode um servidor local com o comando:
+
+   ```bash
+   python3 -m http.server 8000
+   ```
+
+3. Acesse `http://localhost:8000/index.html` no navegador para usar a calculadora.
+
+Também é possível abrir o arquivo `index.html` diretamente em um navegador, mas o servidor local facilita testes em diferentes dispositivos.
 
EOF
)
