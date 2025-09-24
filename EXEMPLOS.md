# 📸 Exemplos de Uso - Analisador de Sentimentos

## 🖼️ Screenshots da Aplicação

### 1. Interface Principal
```
┌─────────────────────────────────────────────────────────────┐
│                    🧠 Analisador de Sentimentos IA          │
│                                                             │
│  Descubra o sentimento por trás de qualquer texto usando   │
│  inteligência artificial                                    │
│                                                             │
│  ✏️ Digite ou cole seu texto aqui:                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ I am very happy with this new project! 😊         │    │
│  │                                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│              🧠 Analisar Sentimento                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. Resultado - Sentimento Positivo
```
┌─────────────────────────────────────────────────────────────┐
│  🧠 Analisador de Sentimentos IA                           │
│                                                             │
│  ✏️ Digite ou cole seu texto aqui:                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ I am very happy with this new project! 😊         │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 😀  Positivo                                        │    │
│  │     O texto expressa sentimentos positivos!         │    │
│  │                                                     │    │
│  │  Polaridade: 0.200    │  Intensidade: 20%          │    │
│  │  ████░░░░░░░░░░░░░░░░ │  ████░░░░░░░░░░░░░░░░       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  💡 Exemplos para testar:                                  │
│  [Positivo] [Negativo] [Neutro] [Emocionado]               │
└─────────────────────────────────────────────────────────────┘
```

### 3. Resultado - Sentimento Negativo
```
┌─────────────────────────────────────────────────────────────┐
│  🧠 Analisador de Sentimentos IA                           │
│                                                             │
│  ✏️ Digite ou cole seu texto aqui:                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ This product is terrible, I hate it!                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 😡  Negativo                                        │    │
│  │     O texto expressa sentimentos negativos.         │    │
│  │                                                     │    │
│  │  Polaridade: -0.600  │  Intensidade: 60%           │    │
│  │  ████████████░░░░░░░ │  ████████████░░░░░░░         │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  💡 Exemplos para testar:                                  │
│  [Positivo] [Negativo] [Neutro] [Emocionado]               │
└─────────────────────────────────────────────────────────────┘
```

### 4. Resultado - Sentimento Neutro
```
┌─────────────────────────────────────────────────────────────┐
│  🧠 Analisador de Sentimentos IA                           │
│                                                             │
│  ✏️ Digite ou cole seu texto aqui:                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ The weather is normal today.                        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 😐  Neutro                                          │    │
│  │     O texto é neutro em relação aos sentimentos.    │    │
│  │                                                     │    │
│  │  Polaridade: 0.000   │  Intensidade: 0%            │    │
│  │  ░░░░░░░░░░░░░░░░░░░░ │  ░░░░░░░░░░░░░░░░░░░░        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  💡 Exemplos para testar:                                  │
│  [Positivo] [Negativo] [Neutro] [Emocionado]               │
└─────────────────────────────────────────────────────────────┘
```

## 📝 Exemplos de Textos para Teste

### ✅ Textos em Inglês (Recomendado)

**Positivos:**
- "I am very happy with this new project! 😊"
- "This product is amazing, I love it!"
- "Great service, highly recommended!"
- "I had a wonderful time at the party!"
- "This is the best day ever!"

**Negativos:**
- "This product is terrible, I hate it!"
- "Worst experience ever, very disappointed."
- "Poor quality, waste of money."
- "I'm so frustrated with this service."
- "This is absolutely awful!"

**Neutros:**
- "The weather is normal today."
- "This is just a regular day."
- "Nothing special happened."
- "The meeting was scheduled for 3 PM."
- "I bought some groceries at the store."

### ⚠️ Textos em Português (Precisão Limitada)

**Positivos:**
- "Estou muito feliz com este projeto!"
- "Este produto é incrível, eu amo!"
- "Excelente serviço, altamente recomendado!"

**Negativos:**
- "Este produto é terrível, eu odeio!"
- "Pior experiência de sempre, muito decepcionado."
- "Qualidade ruim, desperdício de dinheiro."

**Neutros:**
- "O clima está normal hoje."
- "Este é apenas um dia comum."
- "Nada de especial aconteceu."

## 🎯 Escalas de Polaridade

| Polaridade | Classificação | Cor | Emoji | Descrição |
|------------|---------------|-----|-------|-----------|
| > 0.1 | Positivo | Verde | 😀 | Sentimentos positivos claros |
| -0.1 a 0.1 | Neutro | Laranja | 😐 | Sentimento neutro ou ambíguo |
| < -0.1 | Negativo | Vermelho | 😡 | Sentimentos negativos claros |

## 🔍 Interpretação dos Resultados

### Polaridade
- **Valores positivos**: Sentimento positivo
- **Valores negativos**: Sentimento negativo  
- **Valores próximos de zero**: Sentimento neutro
- **Valores extremos (±0.8+)**: Sentimentos muito intensos

### Intensidade
- **0-20%**: Sentimento fraco
- **21-50%**: Sentimento moderado
- **51-80%**: Sentimento forte
- **81-100%**: Sentimento muito intenso

## 💡 Dicas para Melhores Resultados

1. **Use textos em inglês** para maior precisão
2. **Textos mais longos** tendem a ser mais precisos
3. **Evite ironia e sarcasmo** - podem ser mal interpretados
4. **Use pontuação adequada** para melhor análise
5. **Teste com diferentes exemplos** para entender o comportamento

## 🚀 Como Executar os Testes

1. **Inicie a aplicação:**
```bash
cd app
python analisador_sentimentos.py
```

2. **Acesse:** `http://localhost:5000`

3. **Teste os exemplos:**
   - Copie e cole os textos de exemplo
   - Clique em "Analisar Sentimento"
   - Observe os resultados e métricas

4. **Experimente seus próprios textos:**
   - Digite textos em inglês
   - Teste diferentes tipos de sentimento
   - Compare os resultados
