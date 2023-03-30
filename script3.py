
# Papadopoulos  Panagiotis  3212018161
# Kyriazis      Ioannis     3212018107


import os
import sys     #ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ
import time


arxeio = open('/etc/stoixeia', 'r')  #ΑΝΟΙΓΜΑ ΑΡΧΕΙΟΥ
codes={}

#EISAGOYME TIS LEKSEIS APO TO ARXEIO STO LEKSIKO
print('Χρήστες με κενό password:')
for line in arxeio:  #ΔΙΑΒΑΣΜΑ ΚΑΘΕ ΓΡΑΜΜΗΣ ΤΟΥΣ ΑΡΧΕΙΟΥ
    (username,kvdikos)=line.split(',')   #ΧΩΡΙΖΟΥΜΕ ΤΙΣ ΠΛΗΡΟΦΟΡΙΕΣ ΤΗΣ ΓΡΑΜΜΗΣ ΤΟΥ ΑΡΧΕΙΟΥ
    codes[username]=kvdikos
    if kvdikos==' \n': #ΑΝ Ο ΚΩΔΙΚΟΣ ΕΙΝΑΙ ΚΕΝΟΣ
        print('Χρήστης: %s'%(username))  #ΕΜΦΑΝΙΖΕΙ ΤΟ ΟΝΟΜΑ ΧΡΗΣΤΗ
        entolh1 = 'usermod -L %s'%(username)   #ΤΟΝ ΑΠΕΝΕΡΓΟΠΟΙΕΙ
        os.popen("sudo -S %s"%(entolh1), 'w')

print("Οι παραπάνω λογαριασμοί απενεργοποιήθηκαν!!!") 

arxeio.close()   #ΚΛΕΙΣΙΜΟ ΑΡΧΕΙΟΥ 
