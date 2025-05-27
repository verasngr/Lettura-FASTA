# lettura_fasta.py

def leggi_fasta(Lettura-FASTA):
    with open(Lettura-FASTA, 'r') as f:
        righe = f.readlines()

    intestazione = righe[0].strip()
    sequenza = ''.join([riga.strip() for riga in righe[1:]])
    
    print("ID:", intestazione[1:])
    print("Sequenza:", sequenza)

# Esempio d’uso (da attivare se hai un file fasta):
# leggi_fasta("sequenza.fasta")
