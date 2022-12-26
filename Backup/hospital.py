from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.furtherInformation=StringVar()
        self.StrogeAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowTouseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="------*HOSPITAL MANAGEMENT SYSTEM*------",fg="Dark orange",bg="white",font=("times new roman",20,"bold"))
        lbltitle.pack(side=TOP,fill=X)

#  ====================================DataFrame======================================
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=80,width=1275,height=368)

        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                         font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=4,width=900,height=330)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                         font=("times new roman",12,"bold"),text="Prescription")                      
        DataframeRight.place(x=910,y=3,width=330,height=330)

#  =====================================Buttons Frame====================================

        Buttonframe=Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=0,y=455,width=1275,height=52)

#  =====================================Details Frame====================================

        Detailsframe=Frame(self.root,bd=15,relief=RIDGE)
        Detailsframe.place(x=0,y=505,width=1275,height=135)

#  ======================================DataframeLeft====================================

        lblNameTablet=Label(DataframeLeft,font=("arial",10,"bold"),text="Name of Tablets:-  ",padx=2,pady=6) 
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",
                                                        font=("arial",10,"bold"),width=33)
        comNameTablet['value']=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",10,"bold"),text="Referance No:-  ",padx=2,pady=6) 
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.ref,width=33)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",10,"bold"),text="Dose:-  ",padx=2,pady=6) 
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Dose,width=33)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablates=Label(DataframeLeft,font=("arial",10,"bold"),text="No Of Tablets:-  ",padx=2,pady=6)
        lblNoOftablates.grid(row=3,column=0,sticky=W)
        txtNoOftablates=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Numberoftablets,width=33)
        txtNoOftablates.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,font=("arial",10,"bold"),text="Lot:-  ",padx=2,pady=6) 
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Lot,width=33)
        txtLot.grid(row=4,column=1)
        
        lblissueDate=Label(DataframeLeft,font=("arial",10,"bold"),text="Issue Date:-  ",padx=2,pady=6) 
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Issuedate,width=33)
        txtissueDate.grid(row=5,column=1)
         
        lblExpDate=Label(DataframeLeft,font=("arial",10,"bold"),text="Exp Date:-  ",padx=2,pady=6) 
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.ExpDate,width=33)
        txtExpDate.grid(row=6,column=1)
         
        lblDailyDose=Label(DataframeLeft,font=("arial",10,"bold"),text="Daily Dose:-  ",padx=2,pady=6) 
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DailyDose,width=33)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",10,"bold"),text="Side Effect:-  ",padx=2,pady=6) 
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.sideEfect,width=33)
        txtSideEffect.grid(row=8,column=1)
         
        lblFurtherinfo=Label(DataframeLeft,font=("arial",10,"bold"),text="  Further Information:-  ",padx=2) 
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.furtherInformation,width=33)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",10,"bold"),text="  Blood Pressure:-  ",padx=2,pady=6) 
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DrivingUsingMachine,width=33)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",10,"bold"),text="  Storage Advice:-  ",padx=2,pady=6) 
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.StrogeAdvice,width=33)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",10,"bold"),text="   Medication:-  ",padx=2,pady=6) 
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.HowTouseMedication,width=33)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",10,"bold"),text="   Patient Id:-  ",padx=2,pady=6) 
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientId,width=33)
        txtPatientId.grid(row=4,column=3)

        lblNshNumber=Label(DataframeLeft,font=("arial",10,"bold"),text="   NSH Number:-  ",padx=2,pady=6) 
        lblNshNumber.grid(row=5,column=2,sticky=W)
        txtNshNumber=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.nhsNumber,width=33)
        txtNshNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",10,"bold"),text="   Patient Name:-  ",padx=2,pady=6) 
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientName,width=33)
        txtPatientname.grid(row=6,column=3)
         
        lblDateOfBirth=Label(DataframeLeft,font=("arial",10,"bold"),text="   Date Of Birth:-  ",padx=2,pady=6) 
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DateOfBirth,width=33)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",10,"bold"),text="   Patient Address:-  ",padx=2,pady=6) 
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientAddress,width=33)
        txtPatientAddress.grid(row=8,column=3)
        


# ===========================================DataFrameRight======================================
        self.txtPrescription=Text(DataframeRight,font=("arial",11,"bold"),width=36,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


# ===========================================Button==============================================
        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="PrescriptionData",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnPrescriptionData.grid(row=0,column=1)

       
        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnUpdate.grid(row=0,column=2)

       
        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnDelete.grid(row=0,column=3)

       
        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=10,padx=2,pady=4)
        btnExit.grid(row=0,column=5)
        


# =======================================================Table===========================================
# ================================Scrollbar=========================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                     "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Referance No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        #self.hospital_table.heading["show"]="headings"



        self.hospital_table.column("nameoftable",width=70)
        self.hospital_table.column("ref",width=70)
        self.hospital_table.column("dose",width=70)
        self.hospital_table.column("nooftablets",width=70)
        self.hospital_table.column("lot",width=70)
        self.hospital_table.column("issuedate",width=70)
        self.hospital_table.column("expdate",width=70)
        self.hospital_table.column("dailydose",width=70)
        self.hospital_table.column("storage",width=70)
        self.hospital_table.column("nhsnumber",width=70)
        self.hospital_table.column("pname",width=70)
        self.hospital_table.column("dob",width=70)
        self.hospital_table.column("address",width=70)


        self.hospital_table.pack(fill=BOTH,expand=1)


























root=Tk()
ob=Hospital(root)
root.mainloop()
