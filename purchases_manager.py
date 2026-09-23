'''''''''
The initiative proposes an introductory and progressive pathway 
to Python programming, designed for students who wish to acquire useful 
and immediately applicable skills, even without specific prerequisites. 
The course guides participants from setting up the working environment and 
learning the fundamentals of the language to data analysis, initial machine 
learning models, and the basics of neural networks.  Particular 
attention was devoted to understanding the role that these tools play 
today in engineering practice and research, with examples and applications of 
interest also in the biomedical field. In the final part of the program, the topic
of Federated Learning was introduced, presented as a modern paradigm for distributed
learning in contexts where privacy, security, and the management of sensitive data
are of central importance. The objective is not only to provide basic technical skills, 
but also to offer an accessible and informed understanding of the value of these emerging approaches.

''''
import datetime
import numpy as np
import matplotlib.pyplot as plt
# dati in memoria (si azzerano alla chiusura del programma)
entrate = []
spese = []
def aggiungi_voce(lista, tipo):
    print(f"\n--- Aggiungi {tipo} ---")
    try:
        importo = float(input("Importo (€): "))
        if importo <= 0:
            print("L'importo deve essere positivo.")
            return
    except ValueError:
        print("Importo non valido.")
        return
    data_str = input("Data (GG/MM/AAAA) o premi invio per oggi: ")
    if not data_str:
        data_str = datetime.date.today().strftime("%d/%m/%Y")
    else:
        try:
            datetime.datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("Formato data non valido.")
            return
    categoria = input("Categoria: ").strip().lower()
    nota = input("Nota (opzionale): ").strip()
    lista.append({
        "importo": importo,
        "data": data_str,
        "categoria": categoria,
        "nota": nota
    })
    print(f"{tipo} aggiunta con successo!")
def visualizza_saldo():
    tot_entrate = sum(e["importo"] for e in entrate)
    tot_spese = sum(s["importo"] for s in spese)
    saldo = tot_entrate - tot_spese
    print("\n--- Riepilogo Saldo ---")
    print(f"Totale Entrate: {tot_entrate:.2f} €")
    print(f"Totale Spese:   {tot_spese:.2f} €")
    print("-" * 23)
    print(f"Saldo Finale:   {saldo:.2f} €")
def visualizza_grafici():
    if not spese and not entrate:
        print("\nNessun dato disponibile per generare grafici.")
        return
    print("\n--- Grafici ---")
    print("1. Spese per categoria (Torta)")
    print("2. Andamento spese nel tempo (Linea)")
    print("3. Entrate vs Spese (Barre)")
    scelta = input("Scegli un grafico (1-3): ")
    if scelta == "1":
        if not spese:
            print("Nessuna spesa registrata.")
            return
        categorie = {}
        for s in spese:
            categorie[s["categoria"]] = categorie.get(s["categoria"], 0) + s["importo"]
        plt.figure(figsize=(8, 6))
        plt.pie(categorie.values(), labels=categorie.keys(), autopct='%1.1f%%', startangle=140)
        plt.title("Ripartizione Spese per Categoria")
        plt.axis('equal')
        plt.savefig("grafico_torta.png")
        plt.show()
        print("Grafico salvato come 'grafico_torta.png'.")
    elif scelta == "2":
        if not spese:
            print("Nessuna spesa registrata.")
            return
        spese_per_data = {}
        for s in spese:
            d = datetime.datetime.strptime(s["data"], "%d/%m/%Y").date()
            spese_per_data[d] = spese_per_data.get(d, 0) + s["importo"]
        date_ordinate = sorted(spese_per_data.keys())
        valori = [spese_per_data[d] for d in date_ordinate]
        etichette = [d.strftime("%d/%m/%Y") for d in date_ordinate]
        x = np.arange(len(etichette))
        plt.figure(figsize=(10, 6))
        plt.plot(x, valori, marker='o', linestyle='-', color='r')
        plt.xticks(x, etichette, rotation=45)
        plt.title("Andamento Spese nel Tempo")
        plt.xlabel("Data")
        plt.ylabel("Importo (€)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("grafico_linea.png")
        plt.show()
        print("Grafico salvato come 'grafico_linea.png'.")
    elif scelta == "3":
        tot_entrate = sum(e["importo"] for e in entrate)
        tot_spese = sum(s["importo"] for s in spese)
        valori = [tot_entrate, tot_spese]
        x = np.arange(2)
        plt.figure(figsize=(6, 5))
        bars = plt.bar(x, valori, color=['green', 'red'])
        plt.xticks(x, ['Entrate', 'Spese'])
        plt.title("Confronto Entrate vs Spese")
        plt.ylabel("Importo (€)")
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2,
                     yval + (max(valori) * 0.01),
                     f"{yval:.2f} €", ha='center', va='bottom')
        plt.tight_layout()
        plt.savefig("grafico_barre.png")
        plt.show()
        print("Grafico salvato come 'grafico_barre.png'.")
    else:
        print("Scelta non valida.")
def menu():
    print("\n" + "=" * 30)
    print("      GESTORE DI SPESE")
    print("=" * 30)
    print("1. Aggiungi Entrata")
    print("2. Aggiungi Spesa")
    print("3. Visualizza Saldo")
    print("4. Visualizza Grafici")
    print("5. Esci")
    print("=" * 30)
def main():
    while True:
        menu()
        scelta = input("Seleziona un'opzione (1-5): ")
        if scelta == "1":
            aggiungi_voce(entrate, "Entrata")
        elif scelta == "2":
            aggiungi_voce(spese, "Spesa")
        elif scelta == "3":
            visualizza_saldo()
        elif scelta == "4":
            visualizza_grafici()
        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida, riprova.")
if __name__ == "__main__":
    main()

