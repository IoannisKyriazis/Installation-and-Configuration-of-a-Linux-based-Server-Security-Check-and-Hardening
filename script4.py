
# Papadopoulos  Panagiotis  3212018161
# Kyriazis      Ioannis     3212018107


import os
import time   #ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ
 
 
entolh1 = 'last -f /var/log/wtmp > /var/log/pliroforiessyndeshs.txt'   #ΑΠΟΘΗΚΕΥΣΗ ΤΟΥ ΜΟΝΟΠΑΤΙΟΥ ΠΡΟΣ ΤΟ ΑΡΧΕΙΟ ΣΕ ΜΙΑ ΣΥΜΒΟΛΟΣΕΙΡΑ
os.popen("sudo %s"%(entolh1), 'w') #ΕΚΤΕΛΕΣΗ ΣΤΟ ΤΕΡΜΙΝΑΛ

arxeio = open('/var/log/pliroforiessyndeshs.txt', 'r') #ΑΝΟΙΓΜΑ ΑΡΧΕΙΟΥ
axr1='reboot'   
axr2='wtmp'

wra =input('Παρακαλώ εισάγετε την διάρκεια σύνδεσης ενός χρήστη (ΧΧ:ΧΧ):\n')   #ΕΙΣΑΓΟΥΜΕ ΔΙΑΡΚΕΙΑ ΣΥΝΔΕΣΗΣ ΕΝΟΣ ΧΡΗΣΤΗΣ ΣΕ ΜΟΡΦΗ ΧΧ:ΧΧ

for line in arxeio:   #ΔΙΑΒΑΣΜΑ ΚΑΘΕ ΓΡΑΜΜΗΣ ΤΟΥΣ ΑΡΧΕΙΟΥ
    if axr1 not in line:  #ΑΝ ΔΕΝ ΕΙΝΑΙ reboot
        if axr2 not in line: #ΑΝ ΔΕΝ ΕΙΝΑΙ wtmp
            if wra in line:  #ΑΝ ΥΠΑΡΧΕΙ Η ΔΙΑΡΚΕΙΑ ΠΟΥ ΠΛΗΚΤΡΟΛΟΓΗΣΕ Ο ΧΡΗΣΤΗΣ
                plhr=line.split()  #ΧΩΡΙΖΟΥΜΕ ΤΗΝ ΓΡΑΜΜΗ ΣΕ ΔΕΔΟΜΕΝΑ
                print(plhr[0],plhr[1],plhr[2],plhr[3],plhr[4],plhr[5],plhr[6],plhr[7],plhr[8],plhr[9])  #ΕΚΤΥΠΩΝΟΥΜΕ ΤΟΝ ΧΡΗΣΤΗ ΜΕ ΤΗΝ ΣΥΓΚΕΚΡΙΜΕΝΗ ΔΙΑΡΚΕΙΑ ΣΥΝΔΕΣΗΣ
            	
       


arxeio.close()  #ΚΛΕΙΣΙΜΟ ΑΡΧΕΙΟΥ 

