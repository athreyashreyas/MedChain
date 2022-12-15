import sympy,random
import math
import hashlib
from cryptography.fernet import Fernet

def primefactors(n):

    ans=[]
    while(n%2==0):
        ans.append(2)
        n=n//2
    for i in range(3,int(math.sqrt(n)),2):
        while(n%i==0):
            ans.append(i)
            n=n//i
    if(n>2):
        ans.append(n)

    ans=list(set(ans))
    return ans
P=sympy.randprime(2,1000)
doctorPublic=7
patientPublic=11
doctorN=16771
patientN=15689
base_key=Fernet.generate_key()



def publickey():
    
    
    ans=primefactors(P-1)
    G=-1
    for r in range(2,P):
        flag=0
        for i in ans:
            if(pow(r,(P-1)//i,P)==1):
                flag=1
                break
        if(flag==0):
            G=r
            
    
    return P,G

class Id:
    
    doctorId = 1
    patientId = 1
    
class Doctor:
    
    def __init__(self, email, name, address, hospital, specialization,  patientList = {}, currentPatient = None):
        self.email = email
        self.name = name
        self.address = address
        self.hospital = hospital
        self.specialization = specialization
        self.id = Id.doctorId
        self.signature = 6943
        self.patientList = patientList
        self.currentPatient = currentPatient
        Id.doctorId += 1
        

    def requestAccess(self, patient):

        P,G=publickey()
        
        privD=random.randrange(2,P)
        valD=pow(G,privD,P)
        val,history=patient.giveAccess(valD)
        if(val==0):
            print('Access denied')
            return 0
        else:
            secret=pow(val,privD,P)
            secret= bytes(str(secret), 'utf-8')
            print(' ')
            print('In the Doctor class')
        
            print('Secret established',secret)
            encryption_key=base_key+secret
        
            f=Fernet(encryption_key)
            d=f.decrypt(history)
            print('History of doctors')
            print(d)
            return 1

            

    
        
        
    def writePrescription(self, patient):
        prescription = self.requestAccess(patient)
        
        if prescription != 0:

            
            num = int(input("Enter the number of medicines : "))
            medicines = []
            
            for i in range(num):
                medicines.append((input("Enter name of medicine %s : "%(i+1)),input("Enter the frequency per day : ")))
                
            print('Medicines prescribed')
            print(medicines)
            s=self.name+str(self.id)+str(medicines)
            print(s)
            print('Doctor sign',s)
            result = hashlib.sha256(s.encode())
            hashed=result.hexdigest()
            
            sign=[]
            for i in range(len(hashed)):
                sign.append(pow(ord(hashed[i]),self.signature,doctorN))
        
            return medicines,sign
        else:
            print("Access Denied! ")

class Patient:
    
    def __init__(self, email, name, age, address, otherInfo, currentDoctor,  historyOfDoctors = None):
        self.email = email
        self.name = name
        self.age = age
        self.address = address
        self.otherInfo = otherInfo
        self.id = Id.patientId
        self.signature = 12371
        self.currentDoctor = currentDoctor
        self.historyOfDoctors = historyOfDoctors
        Id.patientId += 1

  
    def sign(self,med):
        s=self.name+str(self.id)
        result = hashlib.sha256(s.encode())
        hashed=result.hexdigest()

        sign=[]
        for i in range(len(hashed)):
            sign.append(pow(ord(hashed[i]),self.signature,patientN))

        return sign


    
    def giveAccess(self, keyD):
        accessGranted =  False
        P,G=publickey()
                
        print('Prime number',P)
        print('Primitive Root',G)
        privP=random.randrange(2,P)
        val=pow(G,privP,P)

        print('Do you want the patient to give key')
        s='Y'
        if(s[0]=='y' or s[0]=='Y'):
            secret=pow(keyD,privP,P)
            print('In the Patient Class')
            print('Secret established',secret)
            print(' ')
            secret= bytes(str(secret), 'utf-8')
            encryption_key=base_key+secret
            f=Fernet(encryption_key)

            past=''
            
            for i in self.historyOfDoctors:
                past+=i+' '
            print('Past doctors')
            print(past)
            past=bytes(str(past), 'utf-8')
            token=f.encrypt(past)
            return val,token
        else:
            return 0,0
    
class Prescription:

    def __init__(self, pres):
        self.pres = pres

    def upload(prescription):

         '''
            Convert prescription to json and put it on ledger/MedChain
         '''
    def giveInfo(self):
        print(' ')
        print('########################')
        print('General Prescription')
        print('Patient Name',self.patientName)
        print('Doctor Name',self.doctorName)
        print('Medicines',self.medicines)
        
        code=[]
        for i in range(len(self.pS)):
            code.append(chr(pow(self.pS[i],patientPublic,patientN)))
        print('Patient Sign : ',''.join(map(str,code)))


        code=[]
        for i in range(len(self.dS)):
            code.append(chr(pow(self.dS[i],doctorPublic,doctorN)))
        print('Doctor Sign : ',''.join(map(str,code)))

        print('############################')

chemE=7
chemN=16771
chemD=6943
class Chemist:
    def __init__(self):
        self.hasSupplied = False
        
    def verifySignature(self, patient, doctor, prescription):
        return True
 
    def readPrescription(self, patient, doctor, prescription):
        verified = self.verifySignature(patient, doctor, prescription)
 
        if verified :
            hasSupplied = True
        else:
            print("Permission Denied")

def modInverse(e,M):
    for x in range(1,M):
        if((e*x)%M==1):
            return x
    
def sendPres(pres):
 
 
    P=sympy.randprime(2,200)
    Q=sympy.randprime(2,200)
    N=(P-1)*(Q-1)
    n=P*Q
    while(True):
        e=random.randrange(2,N-2)
        if(math.gcd(e,N)==1):
            break
    
 
    d=modInverse(e,N)

 
    med_encrypt=[]
    for i in range(len(pres.medicines)):
        t=pres.medicines[i][0]
        
        print('the medicines intended',t)
        liss=[]
        dns=[]
        
        for j in range(len(t)):
            liss.append(pow(ord(t[j]),e,n))
        
        
        
        med_encrypt.append(liss)
 
    
 
    
    one_time=[]
    g=str(d)
    print('The secret key for decruption',g)
    for j in range(len(g)):
        m=str(g[j])
        one_time.append(pow(ord(m),chemE,chemN))
 
    
    return one_time,med_encrypt,n
    
    
 
 
# message - encrypt karenge using 1 time key
# key - usko let's say chemist ki public id se encrpyt karenge
 
 
 
def readPres(one_time,med_encrypt,n):
 
    print('Now the chemist is reading the prescription')
    cnt=''
    for j in range(len(one_time)):
        cnt+=chr(pow(one_time[j],chemD,chemN))
    cnt=int(cnt)
    print('Secret one time',cnt)
    
    for t in  range(len(med_encrypt)):
        x=med_encrypt[t]
        
        for j in range(len(x)):
            print(chr(pow(x[j],cnt,n)),end="")
        print(' ')
        

        



# patient=Patient("Rahul",21,["Mr. Shyam"],"Mohan")
    

# doctor=Doctor("Mohan","Vidya Vihar Hospital",45,{},"Rahul")
# med,signD=doctor.writePrescription(patient)

# signP=patient.sign(med)  
# pres=Prescription("Rahul","Mohan",signP,signD,med)
  
# pres.giveInfo()


    
        
        
        
        
