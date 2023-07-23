import flet as ft

md = '''
# Ajutor

### **Cum caut o melodie?**

Pentru a căuta o melodie, trebuie să apăsați pe butonul de căutare din bara de navigare. Acolo, puteți căuta după numele melodiei, artistului sau albumului.

### **Cum primesc o recomandare?**

Pentru a primi o recomandare se poate apăsa pe butonul cu iconița în forma unui bec al fiecărei melodii sau pe butonul de Surprinde-mă! din bara de navigare a paginii de Recomandare.

### **Cum caut după caracteristici?**

În pagina de recomandare, puteți căuta după caracteristici apăsând pe butonul de căutare după ce ați scris caracteristicile dorite (energie, dansabilitate, tempo). Apoi, puteți alege din lista de melodii rezultate.

### **Cum văd informațiile unei melodii?**

Pentru a vedea informațiile unei melodii, trebuie să apăsați pe zona colorată a melodiei respective.

### **Cum adaug/șterg o melodie în/din playlist?**

În panoul de informații a fiecărei melodii există un buton cu un semn de plus. Apăsând pe acesta, melodia va fi adăugată în playlist. Pentru a șterge o melodie din playlist, trebuie să apăsați pe butonul cu un coș de gunoi din panoul de informații a melodiei respective.

'''

def Help(page: ft.Page):


    tab = ft.ResponsiveRow([
        ft.Column([ft.Markdown(md, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB)],expand=True,scroll='hidden',col={'md':8})
    ],alignment=ft.MainAxisAlignment.CENTER,expand=True)
    return tab