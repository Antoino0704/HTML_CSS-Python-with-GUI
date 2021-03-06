import os
import tkinter as tk
from tkinter.messagebox import *
import tkinter.filedialog

win = tk.Tk()                       
win.title('HTML & CSS')
win.geometry("1920x1080")
win.configure(bg='black')
win.iconbitmap('icon.ico')

#creazione di una scroll bar
frameMain = tk.Frame(win)
frameMain.pack(fill=tk.BOTH, expand=True)

canvars = tk.Canvas(frameMain)
canvars.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frameMain, orient=tk.VERTICAL, command=canvars.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar2 = tk.Scrollbar(win, orient=tk.HORIZONTAL, command=canvars.xview)
scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

canvars.configure(yscrollcommand=scrollbar.set, bg='black')
canvars.configure(xscrollcommand=scrollbar2.set)
canvars.bind('<Configure>', lambda e: canvars.configure(scrollregion=canvars.bbox("all")))

frameTwo = tk.Frame(canvars)
frameTwo.configure(bg='black')

canvars.create_window((0, 0), window=frameTwo, anchor="nw")


#schermata informazioni
showinfo('Importante', 'segui i vari step in ordine, quelli senza numero possono essere fatti dopo quelli col numero e in maniera indipendente il loro ordine')
showinfo('Importante', 'puoi inserire come sfondo o il colore o l\'immagine non tutti e due')


cb = tk.StringVar() #variabile colore background viene dichiarato qui perché servirà anche alla funzione fine

#percorso
path = ""
def percorso_real():
    global path
    path_va = tkinter.filedialog.asksaveasfile('w', defaultextension='.html')
    path = path_va.name
    path_va.close()
    f = open(path, "a")
    f.write('''<!DOCTYPE html>
<html lang="it">
<head>''')
    f.close()


percorso = tk.Button(frameTwo, text='salva', command=percorso_real, fg='white')
percorso.configure(bg='red')
percorso.place(x='300')


#titolo
title = tk.StringVar()
title_label = tk.Label(frameTwo, text='2) inserisci titolo', fg='white')
title_label.configure(bg='red')
title_label.grid(row='2', column='1', pady='50')
title_entry = tk.Entry(frameTwo, textvariable=title)
title_entry.grid(row='2', column='2', pady='50')
def title_file():
    f = open(path, "a")
    f.write('\n<title> ' + str(title.get()) + ' </title>')
    f.write('\n<meta charset="UTF-8" />')
    f.close()

title_button = tk.Button(frameTwo, text='salva titolo', command=title_file, fg='white')
title_button.configure(bg='red')
title_button.grid(row='2', column='3')


#icona
icon = tk.StringVar()
icon_label = tk.Label(frameTwo, text='3) inserisci nome immagine icona', fg='white')
icon_label.configure(bg='red')
icon_label.grid(row='2', column='4', padx='10')
icon_entry = tk.Entry(frameTwo, textvariable=icon)
icon_entry.grid(row='2', column='5')
def icon_img():
    f = open(path, "a")
    f.write('\n<link rel="icon" href="' + str(icon.get()) + '" />')
    f.write('\n</head>')
    f.close()

icon_button = tk.Button(frameTwo, text='salva icona', command=icon_img, fg='white')
icon_button.configure(bg='red')
icon_button.grid(row='2', column='6', padx='20')


#colore sfondo
def color_background():
    cb_label = tk.Label(frameTwo, text='inserisci nome colore in inglese', fg='white')
    cb_label.configure(bg='red')
    cb_label.grid(row='3', column='4')
    cb_entry = tk.Entry(frameTwo, textvariable=cb)
    cb_entry.grid(row='3', column='5')
    fin_cb = cb.get()
    def color_save():
        f = open(path, "a")
        f.write('\n<body style="background-color: ' + str(cb.get()) + '">')
        f.close()
    cb_button = tk.Button(frameTwo, text='salva background colore', command=color_save, fg='white')
    cb_button.configure(bg='red')
    cb_button.grid(row='3', column='6')

cb_button = tk.Button(frameTwo, text='4) colore background', command=color_background, fg='white')
cb_button.configure(bg='red')
cb_button.grid(row='3', column='2', pady='50')


#immagine sfondo
def image_background():
    ib = tk.StringVar()
    ib_label = tk.Label(frameTwo, text='inserisci nome immaggine di sfondo', fg='white')
    ib_label.configure(bg='red')
    ib_label.grid(row='3', column='8')
    ib_entry = tk.Entry(frameTwo, textvariable=ib)
    ib_entry.grid(row='3', column='9')
    def image_save():
        f = open(path, "a")
        f.write('\n<body style="background-image: url(' + str(ib.get()) + ')">')
        f.close()
    cb_button = tk.Button(frameTwo, text='salva immaggine sfondo', command=image_save, fg='white')
    cb_button.configure(bg='red')
    cb_button.grid(row='3', column='10')

cb_button = tk.Button(frameTwo, text='4) immaggine sfondo', command=image_background, fg='white')
cb_button.configure(bg='red')
cb_button.grid(row='3', column='7', pady='50', padx='30')

def titiolo_paragrafo():
    #titolo paragrafo
    htk = tk.Toplevel()
    htk.configure(bg='black')
    htk.geometry('1500x500')
    h = tk.StringVar()
    h_c = tk.StringVar()
    h_f = tk.StringVar()
    h_p = tk.StringVar()
    h_r = tk.StringVar()
    #gerarchia titolo paragrafo
    h_r_label = tk.Label(htk, text='inserisci testo gerarchia titolo paragrafo', fg='white')     #testo
    h_r_label.configure(bg='red')
    h_r_label.grid(row='4', column='1', pady='200')
    h_r_entry = tk.Entry(htk, textvariable=h_r)
    h_r_entry.grid(row='4', column='2')
    #testo
    h_label = tk.Label(htk, text='inserisci testo titolo paragrafo', fg='white')     
    h_label.configure(bg='red')
    h_label.grid(row='4', column='4', pady='200')
    h_entry = tk.Entry(htk, textvariable=h)
    h_entry.grid(row='4', column='5')
    #colore testo
    h_c_label = tk.Label(htk, text='inserisci colore testo', fg='white')
    h_c_label.configure(bg='red')
    h_c_label.grid(row='4', column='7', pady='200')
    h_c_entry = tk.Entry(htk, textvariable=h_c)
    h_c_entry.grid(row='4', column='8')
    #grandezza testo
    h_f_label = tk.Label(htk, text='inserisci grandezza testo', fg='white')
    h_f_label.configure(bg='red')
    h_f_label.grid(row='4', column='10', pady='200')
    h_f_entry = tk.Entry(htk, textvariable=h_f)
    h_f_entry.grid(row='4', column='11')
    #posizione testo
    h_p_label = tk.Label(htk, text='inserisci posizione testo(in inglese)', fg='white')
    h_p_label.configure(bg='red')
    h_p_label.grid(row='4', column='13', pady='200')
    h_p_entry = tk.Entry(htk, textvariable=h_p)
    h_p_entry.grid(row='4', column='15')
    def h_html():
        f = open(path, "a")
        f.write('\n<' + str(h_r.get()) + ' style="color: ' + str(h_c.get()) + '; font-size: ' + str(h_f.get()) + 'px; text-align: ' + str(h_p.get()) + '"> ' + str(h.get()) + ' </' + str(h_r.get()) + '>')
        f.close()
        htk.destroy()
        

    tp_button = tk.Button(htk, text='salva titolo paragrafo', command=h_html, fg='white')
    tp_button.configure(bg='red')
    tp_button.place(y='400', x='750')

titiolo_paragrafob = tk.Button(frameTwo, text='aggiungi titolo paragrafo', command=titiolo_paragrafo, fg='white')
titiolo_paragrafob.configure(bg='red')
titiolo_paragrafob.grid(row='4', column='1', pady='50', stick='W')



def paragrafo():

    #paragrafo
    ptk = tk.Toplevel()
    ptk.configure(bg='black')
    ptk.geometry('1200x300')
    p = tk.StringVar()
    p_c = tk.StringVar()
    p_f = tk.StringVar()
    p_p = tk.StringVar()
    p_label = tk.Label(ptk, text='inserisci testo paragrafo', fg='white')     #testo
    p_label.configure(bg='red')
    p_label.grid(row='6', column='1', pady='100')
    p_entry = tk.Entry(ptk, textvariable=p)
    p_entry.grid(row='6', column='2')
    #colore testo
    p_c_label = tk.Label(ptk, text='inserisci colore testo', fg='white')
    p_c_label.configure(bg='red')
    p_c_label.grid(row='6', column='4', pady='50')
    p_c_entry = tk.Entry(ptk, textvariable=p_c)
    p_c_entry.grid(row='6', column='5')
    #grandezza testo
    p_f_label = tk.Label(ptk, text='inserisci grandezza testo', fg='white')
    p_f_label.configure(bg='red')
    p_f_label.grid(row='6', column='7', pady='50')
    p_f_entry = tk.Entry(ptk, textvariable=p_f)
    p_f_entry.grid(row='6', column='8')
    #posizione testo
    p_p_label = tk.Label(ptk, text='inserisci posizione testo(in inglese)', fg='white')
    p_p_label.configure(bg='red')
    p_p_label.grid(row='6', column='10', pady='50')
    p_p_entry = tk.Entry(ptk, textvariable=p_p)
    p_p_entry.grid(row='6', column='11')
    def p_html():
        f = open(path, "a")
        f.write('\n<p style="color: ' + str(p_c.get()) + '; font-size: ' + str(p_f.get()) + 'px; text-align: ' + str(p_p.get()) + '"> ' + str(p.get()) + ' </p>')
        f.close()
        ptk.destroy()
        

    p_button = tk.Button(ptk, text='salva paragrafo', command=p_html, fg='white')
    p_button.configure(bg='red')
    p_button.place(y='200', x='500')

paragrafob = tk.Button(frameTwo, text='aggiungi paragrafo', command=paragrafo, fg='white')
paragrafob.configure(bg='red')
paragrafob.grid(row='5', column='1', stick='W')


#immaggine
def immaggine():
    itk = tk.Toplevel()
    itk.configure(bg='black')
    itk.geometry('300x200')
    i = tk.StringVar()
    i_label = tk.Label(itk, text='inserisci nome immaggine', fg='white')     #testo
    i_label.configure(bg='red')
    i_label.grid(row='7', column='1', pady='100')
    i_entry = tk.Entry(itk, textvariable=i)
    i_entry.grid(row='7', column='2')
    def i_html():
        f = open(path, "a")
        f.write('\n<br>\n<img src="' + str(i.get()) + '" alt="immaggine" />')
        f.close()
        itk.destroy()
        
    i_button = tk.Button(itk, text='salva immaggine', command=i_html, fg='white')
    i_button.configure(bg='red')
    i_button.place(y='150', x='50')

immaggineb = tk.Button(frameTwo, text='aggiungi immaggine', command=immaggine, fg='white')
immaggineb.configure(bg='red')
immaggineb.grid(row='6', column='1', pady='50', stick='W')



#link
def link():
    ltk = tk.Toplevel()
    ltk.configure(bg='black')
    ltk.geometry('800x300')
    l = tk.StringVar()
    l_name = tk.StringVar()
    l_label = tk.Label(ltk, text='inserisci link', fg='white')     #testo
    l_label.configure(bg='red')
    l_label.grid(row='7', column='1', pady='100')
    l_entry = tk.Entry(ltk, textvariable=l)
    l_entry.grid(row='7', column='2')
    l_name_label = tk.Label(ltk, text='inserisci il nome che verrà visualizzato quando si cliccherà sul link', fg='white')     #testo
    l_name_label.configure(bg='red')
    l_name_label.grid(row='7', column='5', pady='100')
    l_name_entry = tk.Entry(ltk, textvariable=l_name)
    l_name_entry.grid(row='7', column='6')
    def l_html():
        f = open(path, "a")
        f.write('\n<a href="' + str(l.get()) + '"> ' + str(l_name.get()) + ' </a>')
        f.close()
        ltk.destroy()
        
    l_button = tk.Button(ltk, text='salva link', command=l_html, fg='white')
    l_button.configure(bg='red')
    l_button.place(y='150', x='250')

linkb = tk.Button(frameTwo, text='aggiungi link', command=link, fg='white')
linkb.configure(bg='red')
linkb.grid(row='7', column='1', stick='W', pady='10')


#video
def video():
    vtk = tk.Toplevel()
    vtk.configure(bg='black')
    vtk.geometry('800x300')
    v = tk.StringVar()
    v_label = tk.Label(vtk, text='inserisci nome video', fg='white')     #testo
    v_label.configure(bg='red')
    v_label.grid(row='7', column='1', pady='100')
    v_entry = tk.Entry(vtk, textvariable=v)
    v_entry.grid(row='7', column='2')
    def v_html():
        f = open(path, "a")
        f.write('\n<video controls height="600" width="1000">\n<source src="' + str(v.get()) + '" type="video/mp4"/>\n</video>')
        f.close()
        vtk.destroy()
        
    v_button = tk.Button(vtk, text='salva video', command=v_html, fg='white')
    v_button.configure(bg='red')
    v_button.place(y='150', x='250')

videob = tk.Button(frameTwo, text='aggiungi video', command=video, fg='white')
videob.configure(bg='red')
videob.grid(row='8', column='1', stick='W', pady='30')



#musica
def musica():
    mtk = tk.Toplevel()
    mtk.configure(bg='black')
    mtk.geometry('800x300')
    m = tk.StringVar()
    m_label = tk.Label(mtk, text='inserisci nome audio', fg='white')     #testo
    m_label.configure(bg='red')
    m_label.grid(row='7', column='1', pady='100')
    m_entry = tk.Entry(mtk, textvariable=m)
    m_entry.grid(row='7', column='2')
    def m_html():
        f = open(path, "a")
        f.write('\n<audio controls>\n<source src="' + str(m.get()) + '" type="audio/mp3"/>\n</audio>')
        f.close()
        mtk.destroy()
        
    m_button = tk.Button(mtk, text='salva audio', command=m_html, fg='white')
    m_button.configure(bg='red')
    m_button.place(y='150', x='250')

musicab = tk.Button(frameTwo, text='aggiungi audio', command=musica, fg='white')
musicab.configure(bg='red')
musicab.grid(row='9', column='1', stick='W')


#elenco non numerato
def elenco_non_numerato():
    f = open(path, "a")
    f.write('\n<ul>')
    eotk = tk.Toplevel()
    eotk.configure(bg='black')
    eotk.geometry('1600x300')
    eo = tk.StringVar()
    eo_c = tk.StringVar()
    eo_f = tk.StringVar()
    eo_p = tk.StringVar()
    eo_label = tk.Label(eotk, text='inserisci testo elenco non numerato', fg='white')     #testo
    eo_label.configure(bg='red')
    eo_label.grid(row='6', column='1', pady='100')
    eo_entry = tk.Entry(eotk, textvariable=eo)
    eo_entry.grid(row='6', column='2')
    #colore testo
    eo_c_label = tk.Label(eotk, text='inserisci colore elenco non numerato', fg='white')
    eo_c_label.configure(bg='red')
    eo_c_label.grid(row='6', column='4', pady='50')
    eo_c_entry = tk.Entry(eotk, textvariable=eo_c)
    eo_c_entry.grid(row='6', column='5')
    #grandezza testo
    eo_f_label = tk.Label(eotk, text='inserisci grandezza testo elenco non numerato', fg='white')
    eo_f_label.configure(bg='red')
    eo_f_label.grid(row='6', column='7', pady='50')
    eo_f_entry = tk.Entry(eotk, textvariable=eo_f)
    eo_f_entry.grid(row='6', column='8')
    #posizione testo
    eo_p_label = tk.Label(eotk, text='inserisci posizione testo elenco non numerato (in inglese)', fg='white')
    eo_p_label.configure(bg='red')
    eo_p_label.grid(row='6', column='10', pady='50')
    eo_p_entry = tk.Entry(eotk, textvariable=eo_p)
    eo_p_entry.grid(row='6', column='11')
    def app_el():
        f.write('\n<li style="color:' + str(eo_c.get()) + '; font-size: ' + str(eo_f.get()) + 'px; text-align: ' + str(eo_p.get()) + '"> ' + str(eo.get()) + ' </li>')
    def eo_html():
        f.write('\n</ul>')
        f.close()
        eotk.destroy()
        
    eo1_button = tk.Button(eotk, text='aggiungi a elenco non numerato', command=app_el, fg='white')       #pulsante per aggiungere testo a elenco 
    eo1_button.configure(bg='red')
    eo1_button.place(y='150', x='250')

    eo2_button = tk.Button(eotk, text='salva elenco non numerato', command=eo_html, fg='white')       #pulsante per salvare elenco non numerato
    eo2_button.configure(bg='red')
    eo2_button.place(y='150', x='700')

elenco_non_numeratob = tk.Button(frameTwo, text='aggiungi elenco non numerato', command=elenco_non_numerato, fg='white')
elenco_non_numeratob.configure(bg='red')
elenco_non_numeratob.grid(row='10', column='1', pady='20', stick='W')



#elenco numerato
def elenco_numerato():
    f = open(path, "a")
    f.write('\n<ol>')
    etk = tk.Toplevel()
    etk.configure(bg='black')
    etk.geometry('1600x300')
    e = tk.StringVar()
    e_c = tk.StringVar()
    e_f = tk.StringVar()
    e_p = tk.StringVar()
    e_label = tk.Label(etk, text='inserisci testo elenco numerato', fg='white')     #testo
    e_label.configure(bg='red')
    e_label.grid(row='6', column='1', pady='100')
    e_entry = tk.Entry(etk, textvariable=e)
    e_entry.grid(row='6', column='2')
    #colore testo
    e_c_label = tk.Label(etk, text='inserisci colore elenco numerato', fg='white')
    e_c_label.configure(bg='red')
    e_c_label.grid(row='6', column='4', pady='50')
    e_c_entry = tk.Entry(etk, textvariable=e_c)
    e_c_entry.grid(row='6', column='5')
    #grandezza testo
    e_f_label = tk.Label(etk, text='inserisci grandezza testo elenco numerato', fg='white')
    e_f_label.configure(bg='red')
    e_f_label.grid(row='6', column='7', pady='50')
    e_f_entry = tk.Entry(etk, textvariable=e_f)
    e_f_entry.grid(row='6', column='8')
    #posizione testo
    e_p_label = tk.Label(etk, text='inserisci posizione testo elenco numerato (in inglese)', fg='white')
    e_p_label.configure(bg='red')
    e_p_label.grid(row='6', column='10', pady='30')
    e_p_entry = tk.Entry(etk, textvariable=e_p)
    e_p_entry.grid(row='6', column='11')
    def app_eln():
        f.write('\n<li style="color:' + str(e_c.get()) + '; font-size: ' + str(e_f.get()) + 'px; text-align: ' + str(e_p.get()) + '"> ' + str(e.get()) + ' </li>')
    def e_html():
        f.write('\n</ol>')
        f.close()
        etk.destroy()
        
    eo1_button = tk.Button(etk, text='aggiungi a elenco numerato', command=app_eln, fg='white')       #pulsante per aggiungere testo a elenco 
    eo1_button.configure(bg='red')
    eo1_button.place(y='150', x='250')

    eo2_button = tk.Button(etk, text='salva elenco numerato', command=e_html, fg='white')       #pulsante per salvare elenco numerato
    eo2_button.configure(bg='red')
    eo2_button.place(y='150', x='700')

elenco_numeratob = tk.Button(frameTwo, text='aggiungi elenco numerato', command=elenco_numerato, fg='white')
elenco_numeratob.configure(bg='red')
elenco_numeratob.grid(row='11', column='1', pady='20', stick='W')


def tabella():
    f = open(path, "a")
    f.write('\n<table>')
    tatk = tk.Toplevel()
    tatk.configure(bg='black')
    tatk.geometry('1600x300')
    ta = tk.StringVar()
    ta_c = tk.StringVar()
    ta_f = tk.StringVar()
    ta_p = tk.StringVar()
    ta_label = tk.Label(tatk, text='inserisci testo riga', fg='white')     #testo
    ta_label.configure(bg='red')
    ta_label.grid(row='6', column='1', pady='100')
    ta_entry = tk.Entry(tatk, textvariable=ta)
    ta_entry.grid(row='6', column='2')
    #colore testo
    ta_c_label = tk.Label(tatk, text='inserisci colore testo riga', fg='white')
    ta_c_label.configure(bg='red')
    ta_c_label.grid(row='6', column='4', pady='50')
    ta_c_entry = tk.Entry(tatk, textvariable=ta_c)
    ta_c_entry.grid(row='6', column='5')
    #grandezza testo
    ta_f_label = tk.Label(tatk, text='inserisci grandezza testo riga', fg='white')
    ta_f_label.configure(bg='red')
    ta_f_label.grid(row='6', column='7', pady='50')
    ta_f_entry = tk.Entry(tatk, textvariable=ta_f)
    ta_f_entry.grid(row='6', column='8')
    #posizione testo
    ta_p_label = tk.Label(tatk, text='inserisci posizione testo riga(in inglese)', fg='white')
    ta_p_label.configure(bg='red')
    ta_p_label.grid(row='6', column='10', pady='50')
    ta_p_entry = tk.Entry(tatk, textvariable=ta_p)
    ta_p_entry.grid(row='6', column='11')
    def riga_eln():
        f.write(' <td style="color:' + str(ta_c.get()) + '; font-size: ' + str(ta_f.get()) + 'px; text-align: ' + str(ta_p.get()) + '"> ' + str(ta.get()) + ' </td>')
    def caselleinizio():
        f.write('\n<tr> ')
    def casellafine():
        f.write(' </tr>')
    def t_html():
        f.write('\n</table>')
        f.close()
        tatk.destroy()
        
    riga_button = tk.Button(tatk, text='aggiungi riga', command=riga_eln, fg='white')       #pulsante per aggiungere riga
    riga_button.configure(bg='red')
    riga_button.place(y='150', x='450')

    casellainizio_button = tk.Button(tatk, text='aggiungi casella', command=caselleinizio, fg='white')       #pulsante per aggiungere casella
    casellainizio_button.configure(bg='red')
    casellainizio_button.place(y='150', x='250')

    casellafine_button = tk.Button(tatk, text='fine casella', command=casellafine, fg='white')       #pulsante per chiudere casella
    casellafine_button.configure(bg='red')
    casellafine_button.place(y='150', x='650')

    p2_button = tk.Button(tatk, text='salva tabella', command=t_html, fg='white')       #pulsante per salvare tabella
    p2_button.configure(bg='red')
    p2_button.place(y='150', x='1050')

tabellab = tk.Button(frameTwo, text='aggiungi tabella', command=tabella, fg='white')
tabellab.configure(bg='red')
tabellab.grid(row='12', column='1', pady='30', stick='W')




def fine():
    f = open(path, "a")    
    if (cb.get() != 'red'):
        f.write('\n<br>\n<br>\n<br>\n<p style=\"color:red\"> file html creato con html & css Python version <p>')
    else:
        f.write('\n<br>\n<br>\n<br>\n<p style=\"color:black\"> file html creato con html & css <p>')
    f.write('\n</body>\n</html>')
    f.close()
    win.destroy()


fine_button = tk.Button(frameTwo, text='FINE', command=fine, fg='white')
fine_button.configure(bg='red')
fine_button.place(x='900')

#menu info
def info():
    showinfo("INFO HTML & CSS PYTHON GUI DARK VERSION", "Version: 2.2.4\nAuthor: Antonino Buscarino")

menu = tk.Menu(win)
menu.add_command(label='INFO', command=info)
win.configure(menu=menu)

win.mainloop()
