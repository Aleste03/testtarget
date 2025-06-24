 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/index.html
index 0000000000000000000000000000000000000000..6eea1801e9142b829f0994e2b95a8d1fe5a47ff0 100644
--- a//dev/null
+++ b/index.html
@@ -0,0 +1,83 @@
+<!DOCTYPE html>
+<html lang="pt-BR">
+<head>
+    <meta charset="UTF-8">
+    <title>Calculadora de Renda Mensal</title>
+    <style>
+        body {
+            font-family: Arial, sans-serif;
+            background: #f4f4f4;
+            margin: 0;
+            padding: 2em;
+            display: flex;
+            justify-content: center;
+        }
+        main {
+            background: #fff;
+            padding: 2em;
+            border-radius: 8px;
+            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
+            width: 320px;
+        }
+        label {
+            display: block;
+            margin-top: 1em;
+        }
+        input[type="number"] {
+            width: 100%;
+            padding: 0.4em;
+            box-sizing: border-box;
+        }
+        button {
+            margin-top: 1em;
+            width: 100%;
+            padding: 0.6em;
+        }
+        #resultado {
+            margin-top: 1em;
+            font-weight: bold;
+            white-space: pre-line;
+        }
+    </style>
+</head>
+<body>
+<main>
+    <h1>Calculadora de Renda Mensal</h1>
+    <label>Investimento Inicial (R$)
+        <input type="number" id="investimentoInicial" step="0.01" required>
+    </label>
+    <label>Aporte Mensal (R$)
+        <input type="number" id="aporteMensal" step="0.01" required>
+    </label>
+    <label>Taxa de Juros Mensal (%)
+        <input type="number" id="taxaJuros" step="0.01" required>
+    </label>
+    <label>Período (meses)
+        <input type="number" id="periodo" required>
+    </label>
+    <button onclick="calcularRenda()">Calcular</button>
+
+    <div id="resultado"></div>
+</main>
+
+<script>
+function calcularRenda() {
+    const investimentoInicial = parseFloat(document.getElementById('investimentoInicial').value) || 0;
+    const aporteMensal = parseFloat(document.getElementById('aporteMensal').value) || 0;
+    const taxaJuros = (parseFloat(document.getElementById('taxaJuros').value) || 0) / 100;
+    const periodo = parseInt(document.getElementById('periodo').value) || 0;
+
+    let montante = investimentoInicial;
+    for (let i = 0; i < periodo; i++) {
+        montante = montante * (1 + taxaJuros) + aporteMensal;
+    }
+
+    const rendaMensal = montante * taxaJuros;
+
+    document.getElementById('resultado').innerText =
+        'Valor acumulado: R$ ' + montante.toFixed(2) + '\n' +
+        'Renda mensal aproximada: R$ ' + rendaMensal.toFixed(2);
+}
+</script>
+</body>
+</html>
 
EOF
)
