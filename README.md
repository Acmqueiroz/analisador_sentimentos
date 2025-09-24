# 🧠 Analisador de Sentimentos IA

Um analisador de sentimentos moderno e intuitivo construído com Flask e TextBlob, que utiliza inteligência artificial para determinar o sentimento por trás de qualquer texto.

## ✨ Características

- 🎨 **Design Moderno**: Interface glassmorphism com animações suaves
- 📱 **Responsivo**: Funciona perfeitamente em desktop e mobile
- 🚀 **Rápido**: Análise instantânea de sentimentos
- 🎯 **Preciso**: Utiliza algoritmos avançados de processamento de linguagem natural
- 🌈 **Visual**: Indicadores coloridos e métricas detalhadas
- ⌨️ **Atalhos**: Suporte a Ctrl+Enter para análise rápida

## 🖼️ Screenshots e Prints

### Interface Principal
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
│  💡 Exemplos para testar:                                  │
│  [Positivo] [Negativo] [Neutro] [Emocionado]               │
└─────────────────────────────────────────────────────────────┘
```

### Resultado - Sentimento Positivo
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
└─────────────────────────────────────────────────────────────┘
```

### Resultado - Sentimento Negativo
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
└─────────────────────────────────────────────────────────────┘
```

### Resultado - Sentimento Neutro
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
└─────────────────────────────────────────────────────────────┘
```

> 📖 **Veja mais prints detalhados e exemplos em [EXEMPLOS.md](EXEMPLOS.md)**

## ⚠️ Importante: Idioma do Texto

**O analisador funciona melhor com textos em INGLÊS**. O TextBlob utiliza modelos de linguagem treinados principalmente em inglês, então:

- ✅ **Recomendado**: Textos em inglês
- ⚠️ **Limitado**: Textos em português (pode ter menor precisão)
- ❌ **Não recomendado**: Outros idiomas

### 🎯 Por que Inglês?

O TextBlob utiliza algoritmos de processamento de linguagem natural que foram treinados principalmente em:
- **Corpus de texto em inglês** (maior disponibilidade)
- **Modelos estatísticos** otimizados para inglês
- **Dicionários de sentimentos** em inglês
- **Padrões linguísticos** específicos do inglês

### 📝 Exemplos de Textos em Inglês:

**Positivo:**
- "I am very happy with this new project! 😊"
- "This product is amazing, I love it!"
- "Great service, highly recommended!"

**Negativo:**
- "This is terrible, I hate it!"
- "Worst experience ever, very disappointed."
- "Poor quality, waste of money."

**Neutro:**
- "The weather is normal today."
- "This is just a regular day."
- "Nothing special happened."

> 📖 **Veja mais exemplos detalhados em [EXEMPLOS.md](EXEMPLOS.md)**

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.7+
- pip

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd analisador_sentimentos
```

2. **Navegue para a pasta app:**
```bash
cd app
```

3. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
```

4. **Ative o ambiente virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

5. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Executando a Aplicação

```bash
python analisador_sentimentos.py
```

A aplicação estará disponível em: `http://localhost:5000`

### 🧪 Testando a Aplicação

1. **Acesse a URL:** `http://localhost:5000`
2. **Digite um texto em inglês** (ex: "I am very happy!")
3. **Clique em "Analisar Sentimento"** ou pressione `Ctrl+Enter`
4. **Observe o resultado** com emoji, classificação e métricas

### 📸 Capturando Screenshots

Para capturar prints da aplicação funcionando:

1. **Execute a aplicação** em background
2. **Abra o navegador** em `http://localhost:5000`
3. **Teste diferentes textos** em inglês
4. **Capture as telas** mostrando:
   - Interface principal
   - Resultados positivos, negativos e neutros
   - Métricas e barras de progresso

## 📋 Dependências

- **Flask**: Framework web para Python
- **TextBlob**: Biblioteca para processamento de linguagem natural
- **NLTK**: Natural Language Toolkit (dependência do TextBlob)

## 🎯 Como Usar

1. **Acesse a aplicação** no seu navegador
2. **Digite ou cole um texto** na área de texto (preferencialmente em inglês)
3. **Clique em "Analisar Sentimento"** ou pressione `Ctrl+Enter`
4. **Veja o resultado** com:
   - Emoji representativo do sentimento
   - Classificação (Positivo/Negativo/Neutro)
   - Polaridade numérica (-1 a 1)
   - Intensidade em porcentagem
   - Barra de progresso visual

## 🔧 Funcionalidades Técnicas

### API Endpoints

- **GET `/`**: Página principal com interface
- **POST `/analisar`**: Endpoint para análise de sentimentos

### Estrutura do Projeto

```
analisador_sentimentos/
├── app/
│   ├── analisador_sentimentos.py    # Aplicação Flask principal
│   ├── requirements.txt             # Dependências Python
│   ├── templates/
│   │   └── index.html               # Template HTML moderno
│   └── venv/                        # Ambiente virtual
└── README.md                        # Este arquivo
```

### Algoritmo de Análise

O analisador utiliza o **TextBlob** que implementa:

1. **Análise de Polaridade**: Mede o sentimento de -1 (muito negativo) a +1 (muito positivo)
2. **Classificação Automática**: 
   - `polaridade > 0.1`: Positivo
   - `polaridade < -0.1`: Negativo  
   - `-0.1 ≤ polaridade ≤ 0.1`: Neutro
3. **Cálculo de Intensidade**: Porcentagem baseada no valor absoluto da polaridade

## 🎨 Design e UX

### Características Visuais
- **Gradiente de fundo** com cores modernas
- **Efeito glassmorphism** nos cards
- **Animações suaves** em todos os elementos
- **Cores dinâmicas** baseadas no sentimento
- **Tipografia moderna** com fonte Inter

### Responsividade
- **Mobile-first**: Otimizado para dispositivos móveis
- **Grid flexível**: Adapta-se a diferentes tamanhos de tela
- **Touch-friendly**: Botões e elementos adequados para toque

## 🧪 Exemplos de Teste

A aplicação inclui exemplos pré-definidos para teste:

- **Positivo**: "I am very happy with this new project! 😊"
- **Negativo**: "This product is terrible, I don't recommend it."
- **Neutro**: "The weather today is normal, neither too hot nor too cold."
- **Emocionado**: "I love traveling and discovering new places! ✈️"

## 🔍 Limitações

1. **Idioma**: Funciona melhor com textos em inglês
2. **Contexto**: Não considera contexto cultural específico
3. **Ironia/Sarcasmo**: Pode ter dificuldade com linguagem figurada
4. **Textos muito curtos**: Precisão pode ser menor com frases muito curtas

## 🛠️ Desenvolvimento

### Estrutura do Código

- **Backend**: Flask com API REST
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Processamento**: TextBlob para análise de sentimentos
- **Templates**: Jinja2 para renderização

### Melhorias Futuras

- [ ] Suporte a múltiplos idiomas
- [ ] Análise de emoções específicas
- [ ] Histórico de análises
- [ ] Exportação de resultados
- [ ] API para integração com outros sistemas

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Fazer push para a branch
5. Abrir um Pull Request

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:

1. Abra uma issue no GitHub
2. Descreva o problema detalhadamente
3. Inclua screenshots se possível
4. Especifique seu ambiente (OS, Python version, etc.)

---

**Desenvolvido com ❤️ usando Flask e TextBlob**
