import streamlit as st

st.title("Test di Intelligenza Emotiva")

st.write("Rispondi alle seguenti domande da 1 (pochissimo) a 5 (molto).")

def sezione(titolo, domande):
    st.header(titolo)
    punteggi = []
    for d in domande:
        val = st.slider(d, 1, 5, 3)
        punteggi.append(val)
    return sum(punteggi)

auto = sezione("Autoconsapevolezza", [
"Ami scherzare e ridere di te stesso",
"Conosci i tuoi limiti e i tuoi punti di forza",
"Sai quali sono i tuoi difetti e i tuoi pregi",
"Riesci a parlare delle tue emozioni",
"Hai una visione chiara di ciò che sai fare bene",
"Sai cosa ti soddisfa",
"Ti ritieni in grado di raggiungere i tuoi obiettivi",
"Usi bene le tue energie",
"Affronti situazioni difficili",
"Sei consapevole dei tuoi valori"
])

controllo = sezione("Controllo delle emozioni", [
"Sai quali emozioni ti condizionano",
"Gestisci le emozioni negative",
"Sei coerente con i tuoi valori",
"Sei ottimista",
"Mantieni la calma nei cambiamenti",
"Rifletti prima di agire",
"Valuti prima di dare colpe",
"Ami sorridere",
"Non ti senti vittima",
"Impari dagli errori"
])

sociale = sezione("Coscienza sociale", [
"Ascolti le persone",
"Osservi l’ambiente",
"Usi il nome delle persone",
"Fai critiche nel modo giusto",
"Ti metti nei panni degli altri",
"Non ti distrai quando ascolti",
"Sei presente nel momento",
"Pensi a come ti vedono gli altri",
"Pianifichi impegni",
"Osservi ambienti nuovi"
])

talento = sezione("Talento sociale", [
"Hai amicizie durature",
"Rifletti sui rapporti",
"Migliori il tuo comportamento",
"Sei cortese",
"Chiedi feedback",
"Gestisci la collera",
"Fai sentire importanti gli altri",
"Accetti osservazioni",
"Risolvi tensioni",
"Gestisci conflitti"
])

def interpreta(p):
    if p <= 25:
        return "Devi lavorarci molto"
    elif p <= 40:
        return "Buona base"
    else:
        return "Buon punto di partenza"

if st.button("Calcola risultato"):
    st.subheader("Risultati")

    st.write("Autoconsapevolezza:", auto, "-", interpreta(auto))
    st.write("Controllo emozioni:", controllo, "-", interpreta(controllo))
    st.write("Coscienza sociale:", sociale, "-", interpreta(sociale))
    st.write("Talento sociale:", talento, "-", interpreta(talento))

    st.success("Individua l’area più debole e lavora su quella.")
