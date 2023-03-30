
# Papadopoulos  Panagiotis  3212018161
# Kyriazis      Ioannis     3212018107


import os
import sys       #ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ
import time


arxeio = open('/etc/stoixeia', 'r')   #ΑΝΟΙΓΜΑ ΑΡΧΕΙΟΥ

codes={}  #ΔΗΜΙΟΥΡΓΙΑ ΛΕΞΙΚΟΥ 
papenergopoihshs={}    #ΔΗΜΙΟΥΡΓΙΑ ΛΕΞΙΚΟΥ 

#ΕΙΣΑΓΟΥΜΕ ΤΙΣ ΣΥΜΒΟΛΟΣΕΙΡΕΣ ΑΠΟ ΤΟ ΑΡΧΕΙΟ ΣΤΟ ΛΕΞΙΚΟ
for line in arxeio: #ΔΙΑΒΑΣΜΑ ΚΑΘΕ ΓΡΑΜΜΗΣ ΤΟΥΣ ΑΡΧΕΙΟΥ
    (username,kvdikos)=line.split(',') #ΧΩΡΙΖΟΥΜΕ ΤΙΣ ΠΛΗΡΟΦΟΡΙΕΣ ΤΗΣ ΓΡΑΜΜΗΣ ΤΟΥ ΑΡΧΕΙΟΥ
    codes[username]=kvdikos #ΑΝΤΙΣΤΟΙΧΟΥΜΕ ΤΙΣ ΣΥΜΒΟΛΟΣΕΙΡΕΣ ΜΙΑ ΠΡΟΣ ΜΙΑ ΑΝΑΛΟΓΑ ΜΕ ΟΝΟΜΑ ΧΡΗΣΤΗ ΚΑΙ ΚΩΔΙΚΟ

i=0 #ΜΕΤΑΒΛΗΤΗ ΓΙΑ ΝΑ ΜΕΤΡΑΕΙ ΤΙΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΓΕΝΙΚΕΣ ΠΡΟΣΠΑΘΕΙΕΣ ΤΟΥ ΧΡΗΣΤΗ

while i<10:  #ΜΕΤΡΑΕΙ ΤΙΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΓΕΝΙΚΕΣ ΠΡΟΣΠΑΘΕΙΕΣ ΤΟΥ ΧΡΗΣΤΗ 
    print('Για την συνδεσή σας στο server πιέστε 1')         #ΕΚΤΥΠΩΝΕΙ ΜΗΝΥΜΑ            
    print('Για την έξοδό σας από τον server πιέστε οποιοδήποτε άλλο πλήκτρο')     #ΕΚΤΥΠΩΝΕΙ ΜΗΝΥΜΑ  
    epilogh =input('Παρακαλώ εισάγετε την επιλογή σας:\n')   #ΕΙΣΑΓΕΙ ΧΡΗΣΤΗΣ ΑΠΟ ΤΟ ΠΛΗΚΤΡΟΛΟΓΙΟ 
    
    if epilogh =='1':  
   
        usernamexrhsth=input('\nUsername:\n')  #ΕΙΣΑΓΩΓΗ ΟΝΟΜΑΤΟΣ ΧΡΗΣΤΗ ΚΑΙ ΚΩΔΙΚΟ
        kvdikosxrhsth=input('Κωδικός:\n')

        #ΕΛΕΓΧΟΥΜΕ ΑΝ ΤΟ ΟΝΟΜΑ ΧΡΗΣΤΗ ΥΠΑΡΧΕΙ ΣΤΟ ΛΕΞΙΚΟ CODES
        if usernamexrhsth in codes : #ΑΝ ΥΠΑΡΧΕΙ ΤΟ ΟΝΟΜΑ ΧΡΗΣΤΗ 
            if kvdikosxrhsth in codes[usernamexrhsth] :  #ΑΝ ΕΙΝΑΙ ΣΩΣΤΟΣ Ο ΚΩΔΙΚΟΣ 
                print('\nΕπιτυχής σύνδεση!')  #ΕΚΤΥΠΩΝΕΙ ΜΗΝΥΜΑ 
                break  #ΣΤΟΠ
            else: #ΑΛΛΙΩΣ
                print('\nΤα Στοιχεία εισόδου είναι λάθος!\n\n') #ΕΚΤΥΠΩΝΕΙ ΜΗΝΥΜΑ 
                i+=1 #+1 ΑΠΟΤΥΧΗΜΕΝΗ ΓΕΝΙΚΗ ΠΡΟΣΠΑΘΕΙΑ

                if  usernamexrhsth in papenergopoihshs : #ΑΝ Ο ΧΡΗΣΤΗΣ ΥΠΑΡΧΕΙ ΣΤΟΝ ΠΙΝΑΚΑ ΧΡΗΣΤΩΝ ΜΕ ΤΙΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΠΡΟΣΠΑΘΕΙΕΣ
                    fores = papenergopoihshs[usernamexrhsth] #ΠΑΙΡΝΟΥΜΕ ΤΙΣ ΠΡΟΗΓΟΥΜΕΝΕΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΠΡΟΣΠΑΘΕΙΕΣ
                    fores+=1 #+1
                    papenergopoihshs[usernamexrhsth]=fores      #ΕΝΗΜΕΡΩΝΟΥΜΕ ΤΟΝ ΠΙΝΑΚΑ
                else:
                    fores=1 
                    papenergopoihshs[usernamexrhsth]=fores  #ΠΑΙΡΝΕΙ 1 ΑΠΟΤΥΧΗΜΕΝΗ ΠΡΟΣΠΑΘΕΙΑ ΚΑΙ ΕΙΣΑΓΕΤΑΙ ΣΤΟΝ ΠΙΝΑΚΑ
                   
                if papenergopoihshs[usernamexrhsth] == 3 : #ΑΝ ΟΙ ΑΠΟΤΥΧΗΜΕΝΕΣ ΠΡΟΣΠΑΘΕΙΕΣ ΤΟΥ ΧΡΗΣΤΗ ΓΙΝΟΥΝ ΙΣΕΣ ΜΕ 3
                    print('\nΟ Λογαριασμός σας απενεργοποιήθηκε!!!\n\n')
                    entolh1 = 'usermod -L %s'%(usernamexrhsth) #ΕΚΤΕΛΕΙ ΤΗΝ ΕΝΤΟΛΗ ΑΠΕΝΕΡΓΟΠΟΙΗΣΗΣ ΤΟΥ ΧΡΗΣΤΗ
                    os.popen("sudo -S %s"%(entolh1), 'w')
                    time.sleep(10)  #ΠΕΡΙΜΕΝΟΥΜΕ 10 ΔΕΥΤΕΡΟΛΕΠΤΑ
                    entolh = 'exit' 
                    os.popen("sudo -S %s"%(entolh), 'w') #ΕΞΟΔΟΣ ΑΠΟ ΤΟ ΣΚΡΙΠΤ
                    sys.exit() 
                        

        else:
            print('\nΤα Στοιχεία εισόδου είναι λάθος!\n\n')
            i+=1 #+1 ΟΙ ΓΕΝΙΚΕΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΠΡΟΣΠΑΘΕΙΕΣ
            continue
    else:
        break    
        
if i == 10:  #ΑΝ ΟΙ ΓΕΝΙΚΕΣ ΑΠΟΤΥΧΗΜΕΝΕΣ ΠΡΟΣΠΑΘΕΙΕΣ ΕΙΝΑΙ 10
    print('\nΠολλές προσπάθειες εισόδου!!!\n\n')
    time.sleep(10)
    entolh = 'exit'
    os.popen("sudo -S %s"%(entolh), 'w')  #ΕΞΟΔΟΣ ΑΠΟ ΤΟ ΣΚΡΙΠΤ
    sys.exit()      

arxeio.close()     #ΚΛΕΙΣΙΜΟ ΑΡΧΕΙΟΥ                                                    #KLEINOYME TO 
