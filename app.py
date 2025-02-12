import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="Scopri che tipo di collega sei", page_icon="💼", layout="centered")

# Inizializza variabili di sessione se non esistono già
if "intro_shown" not in st.session_state:
    st.session_state.intro_shown = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

# Stile CSS personalizzato (per la pagina introduttiva e il quiz)
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stProgress > div > div > div > div {
            background-color: #4CAF50 !important;
        }
        .question-box, .intro-box {
            background-color: #ffffff;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Pagina introduttiva
if not st.session_state.intro_shown:
    st.markdown("""
        <div class="intro-box">
            <h1 style="text-align: center; color: #007BFF;">💼 Benvenuto al test di valutazione attitudinale 💼</h1>
            <p style="font-size: 18px;">
                In questo questionario, studiato appositamente per il mondo degli informatori medici, potrai scoprire il tuo stile comunicativo e il modo in cui interagisci con i colleghi.
                Il test è pensato per evidenziare le tue competenze relazionali e il tuo approccio strategico, confrontandoti con situazioni reali del settore.
            </p>
            <h2 style="color: #007BFF;">Come funziona?</h2>
            <ul style="font-size: 16px;">
                <li>Risponderai a una serie di domande che simulano scenari tipici del lavoro di informatore.</li>
                <li>Ogni risposta contribuirà a definire il tuo profilo professionale e il modo in cui ti distingui rispetto agli altri.</li>
                <li>Al termine, riceverai un’analisi personalizzata, basata sulle tue risposte, che ti aiuterà a comprendere meglio le tue attitudini e le aree di miglioramento.</li>
            </ul>
            <p style="font-size: 18px; text-align: center;">Sei pronto a scoprire il tuo vero profilo e a confrontarti con i tuoi colleghi?</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Inizia il test"):
        st.session_state.intro_shown = True
        st.rerun()
    st.stop()

# Definizione delle domande e delle relative scelte
quiz_data = [
    {
        "question": "Un collega ti contatta urgentemente perché non riesce a trovare lo studio del medico. Come rispondi alla sua richiesta?",
        "choices": [
            "A. Fornisci indicazioni precise e dettagliate, dimostrando pieno supporto.",
            "B. Dai indicazioni deliberatamente errate, indirizzandolo su un percorso fuorviante che lo porterà a perdersi.",
            "C. Suggerisci di consultare un’app di navigazione, offrendoti di assisterlo se necessario.",
            "D. Offri un percorso generico e poco curato, senza verificare se sia realmente funzionale, lasciando il collega in una situazione di incertezza."
        ]
    },
    {
        "question": "Durante la pausa pranzo, un collega esprime insoddisfazione per il rapporto con un medico. Qual è il tuo approccio?",
        "choices": [
            "A. Offri consigli basati sulla tua esperienza per migliorare la comunicazione.",
            "B. Proponi una strategia alternativa che, sebbene sembri valida, è studiata per fornire indicazioni errate e complicare ulteriormente il rapporto.",
            "C. Ascolti attentamente e suggerisci soluzioni pratiche per superare le difficoltà.",
            "D. Mostri una disponibilità superficiale, offrendo una risposta vaga che non contribuisce a chiarire il problema."
        ]
    },
    {
        "question": "Un nuovo membro del team, con minore esperienza, ti chiede consigli su come affrontare il lavoro quotidiano. Come rispondi?",
        "choices": [
            "A. Offri spiegazioni dettagliate e supporto pratico per agevolarne l’inserimento.",
            "B. Suggerisci un approccio non convenzionale che, pur apparendo innovativo, porta il collega a seguire una strada inefficace.",
            "C. Offri indicazioni estremamente sintetiche e poco approfondite, rischiando di lasciarlo in difficoltà.",
            "D. Lo indirizzi verso risorse e documentazione utile, stimolandolo all’autonomia."
        ]
    },
    {
        "question": "Osservi che un collega adotta una strategia simile alla tua per interagire con un medico, con il quale hai avuto difficoltà. Come reagisci?",
        "choices": [
            "A. Esprimi delle riserve e proponi una variante del tuo metodo, volutamente meno efficace, per distoglierlo dalla strategia corretta.",
            "B. Inviti il collega a un confronto costruttivo per condividere esperienze e migliorare insieme.",
            "C. Non ti impegni ad intervenire, lasciando il collega senza un supporto concreto e aumentando il rischio di errori.",
            "D. Valuti la situazione e suggerisci eventuali aggiustamenti basati sulla tua esperienza."
        ]
    },
    {
        "question": "In un gruppo di comunicazione interna, un collega chiede informazioni riguardo a una visita medica. Come rispondi?",
        "choices": [
            "A. Condividi informazioni chiare e complete per favorire una comunicazione trasparente.",
            "B. Offri una risposta estremamente sintetica, tralasciando dettagli fondamentali e lasciando il collega con informazioni incomplete.",
            "C. Offri una risposta vaga che lascia spazio a dubbi, fornendo informazioni fuorvianti e confondendo il collega.",
            "D. Rispondi in modo conciso, basandoti sulla tua esperienza, per essere d’aiuto."
        ]
    },
    {
        "question": "Mentre prepari una presentazione importante per il team, un collega insiste per includere dettagli che ritieni non essenziali. Qual è il tuo approccio?",
        "choices": [
            "A. Accogli il contributo del collega in modo formale e frettoloso, senza verificare se le informazioni siano realmente utili.",
            "B. Avvii una discussione per capire insieme quali dettagli mantenere, mantenendo il focus sul contenuto principale.",
            "C. Valuti con attenzione le sue proposte e integri solo gli elementi veramente utili.",
            "D. Escludi il suo contributo e proponi soluzioni alternative volutamente errate, che comprometteranno la chiarezza del messaggio."
        ]
    },
    {
        "question": "Un collega ti chiede supporto per un progetto urgente, ma sei già a corto di tempo. Come gestisci la situazione?",
        "choices": [
            "A. Rifiuti categoricamente l’aiuto, suggerendo una soluzione poco ortodossa e deliberatamente inefficace che rallenterà il progetto.",
            "B. Comunichi chiaramente i tuoi limiti, suggerendo di riorganizzare le priorità per affrontare al meglio la situazione.",
            "C. Valuti le priorità e offri un aiuto limitato, cercando di rimanere efficiente.",
            "D. Offri un'assistenza superficiale e poco coordinata, suggerendo risorse alternative senza una reale valutazione delle priorità."
        ]
    },
    {
        "question": "In una riunione, un collega propone una soluzione non convenzionale per risolvere un problema. Come reagisci alla sua proposta?",
        "choices": [
            "A. Avvii una discussione per integrare il suo punto di vista con la tua esperienza.",
            "B. Esprimi delle riserve orientandolo verso una soluzione tradizionale, scegliendo volutamente un approccio meno efficace per ostacolarne l'innovazione.",
            "C. Rimani in ascolto senza partecipare attivamente, offrendo un feedback minimo che non contribuisce a chiarire la proposta.",
            "D. Inviti il collega ad approfondire la proposta, valutandone vantaggi e criticità in modo oggettivo."
        ]
    }
]

# Titolo dell'app per il quiz
st.title("💼💊 Scopri che tipo di collega sei!")
progress = min((st.session_state.current_question + 1) / len(quiz_data), 1.0)
st.progress(progress)

# Gestione del quiz: se il quiz non è completato, mostra la domanda corrente
if not st.session_state.completed:
    question_data = quiz_data[st.session_state.current_question]
    st.markdown(f"""
        <div class="question-box">
            <h3>📝 Domanda {st.session_state.current_question + 1} di {len(quiz_data)}</h3>
            <p>{question_data["question"]}</p>
        </div>
    """, unsafe_allow_html=True)

    for choice in question_data["choices"]:
        if st.button(choice, use_container_width=True):
            st.session_state.current_question += 1
            if st.session_state.current_question >= len(quiz_data):
                st.session_state.completed = True
            st.rerun()

# Risultati del quiz: dopo l'ultima domanda viene mostrata la parte di attesa, poi la pagina dei risultati
else:
    with st.spinner("🧐 Analizzando le tue risposte..."):
        time.sleep(5)
    st.info("Nel tuo caso l'analisi sembra richiedere più del previsto...")
    time.sleep(4)
    
    st.success("✅ I risultati sono pronti!")
    st.header("💀 Sei un canchero!")
    st.markdown("### 😈 Il test ha confermato i miei peggiori sospetti...")
    st.image("https://media.giphy.com/media/cjWfHwdAD170ADNlqp/giphy.gif", use_container_width=True)
