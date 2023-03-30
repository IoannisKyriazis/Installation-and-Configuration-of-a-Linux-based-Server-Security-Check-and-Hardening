
# Papadopoulos  Panagiotis  3212018161
# Kyriazis      Ioannis     3212018107


import os
import sys  #ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ
import time


arxeio = open('/var/log/commands.log', 'r') #ΑΝΟΙΓΜΑ ΑΡΧΕΙΟΥ

epilogh =input('Παρακαλώ εισάγετε την επιλογή σας:\n')   #ΕΙΣΑΓΟΥΜΕ ΜΙΑ ΣΥΜΒΟΛΟΣΕΙΡΑ ΓΙΑ ΝΑ ΔΟΥΜΕ ΑΝ ΥΠΑΡΧΕΙ ΜΕΣΑ ΣΤΟ ΑΡΧΕΙΟ

for line in arxeio:  #ΔΙΑΒΑΣΜΑ ΚΑΘΕ ΓΡΑΜΜΗΣ ΤΟΥΣ ΑΡΧΕΙΟΥ
    if epilogh in line: #ΕΑΝ Η ΣΥΜΒΟΛΟΣΕΙΡΑ ΠΟΥ ΕΙΣΑΓΑΓΑΜΕ ΠΡΙΝ ΥΠΑΡΧΕΙ ΣΤΗΝ ΣΥΓΚΕΚΡΙΜΕΝΗ ΣΕΙΡΑ

        (hmera,allo)=line.split('ioannisserver') 
        (xrhsths,c,entolh)=allo.split(':')    #ΧΩΡΙΖΟΥΜΕ ΤΙΣ ΠΛΗΡΟΦΟΡΙΕΣ ΤΗΣ ΓΡΑΜΜΗΣ ΤΟΥ ΑΡΧΕΙΟΥ
        (a,b,g,entolh1)=entolh.split(' ',3)
        (tentolh,n)=entolh1.split('[')
        print(xrhsths,hmera,tentolh)  #ΕΚΤΥΠΩΣΕ ΟΛΗ ΤΗΝ ΣΕΙΡΑ


arxeio.close()  #ΚΛΕΙΣΙΜΟ ΑΡΧΕΙΟΥ
