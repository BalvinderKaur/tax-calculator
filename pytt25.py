from tkinter import *

t = Tk()
import math
import locale
import tkinter as Tk

t.minsize(850, 600)
t.configure(background='pink')


def detail():
    f3 = Frame(bg="pink")
    f3.place(x=100, y=0, width=800, height=600)
    u = Label(f3, text="REGISTRATION DETAILS", bg="sky blue", fg="black")
    u.place(x=270, y=30)
    u1 = Label(f3, text="First Name", bg="black", fg="white")
    u1.place(x=250, y=90)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=90, width=120)

    u2 = Label(f3, text="Last Name", bg="black", fg="white")
    u2.place(x=250, y=130)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=130, width=120)

    u2 = Label(f3, text="Registration ID", bg="black", fg="white")
    u2.place(x=250, y=170)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=170, width=120)

    u2 = Label(f3, text="mobile no.", bg="black", fg="white")
    u2.place(x=250, y=210)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=210, width=30, height=27)
    e1 = Entry(f3, font=("", 12))
    e1.place(x=390, y=210, width=120)

    u2 = Label(f3, text="Income source", bg="black", fg="white")
    u2.place(x=250, y=250)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=250, width=120, height=30)

    u2 = Label(f3, text="Address", bg="black", fg="white")
    u2.place(x=250, y=290)

    e1 = Entry(f3, font=("", 12))
    e1.place(x=350, y=290, width=120, height=30)

    b3 = Button(f3, text="Register", command=calculator)
    b3.place(x=310, y=360, width=100, height=40)

    b2 = Button(f3, text="Back", command=home)
    b2.place(x=310, y=430, width=100, height=40)


def calculator():
    locale.setlocale(locale.LC_ALL, '')
    root = Tk.Tk()
    root.title("Income Tax Calculator")
    root.geometry("900x300")
    TaxFreeNum = 250000

    def callback():
        GetGrossTax = GrossTaxIn.get()
        GrossYear = float(GetGrossTax)
        GrossMonth = GrossYear / 12
        GrossWeek = GrossYear / 52
        GrossDay = GrossYear / 365
        Yearli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossYear))
        Yearli.grid(row=1, column=1)
        Monthli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossMonth))
        Monthli.grid(row=1, column=2)
        Weekli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossWeek))
        Weekli.grid(row=1, column=3)
        Dayli = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossDay))
        Dayli.grid(row=1, column=4)

        TaxFreeYear = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum))
        TaxFreeYear.grid(row=2, column=1)
        TaxFreeMonth = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 12))
        TaxFreeMonth.grid(row=2, column=2)
        TaxFreeWeek = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 52))
        TaxFreeWeek.grid(row=2, column=3)
        TaxFreeDay = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TaxFreeNum / 365))
        TaxFreeDay.grid(row=2, column=4)

        if GrossYear > 250000:
            TotalTaxableYear = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossYear - TaxFreeNum))
            TotalTaxableYear.grid(row=3, column=1)
            TotalTaxableMonth = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossMonth - TaxFreeNum / 12))
            TotalTaxableMonth.grid(row=3, column=2)
            TotalTaxableWeekly = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossWeek - TaxFreeNum / 52))
            TotalTaxableWeekly.grid(row=3, column=3)
            TotalTaxableDaily = Tk.Label(RightFrame, text='₹{:,.2f}'.format(GrossDay - TaxFreeNum / 365))
            TotalTaxableDaily.grid(row=3, column=4)
        else:
            TotalTaxableYear = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableYear.grid(row=3, column=1)
            TotalTaxableMonth = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableMonth.grid(row=3, column=2)
            TotalTaxableWeekly = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableWeekly.grid(row=3, column=3)
            TotalTaxableDaily = Tk.Label(RightFrame, text='₹0.00')
            TotalTaxableDaily.grid(row=3, column=4)

        if GrossYear > 1500000:
            AdditionalRate = GrossYear - 1500000
            AdditionalRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(AdditionalRate * 0.30))
            AdditionalRateTax.grid(row=6, column=1)
            HigherRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(500000 * 0.25))
            HigherRate.grid(row=5, column=1)
            BasicRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(750000 * 0.10))
            BasicRate.grid(row=4, column=1)
            TotalIn = (150000 * 0.10) + (200000 * 0.25) + (AdditionalRate * 0.30)

        elif GrossYear <= 1500000 and GrossYear >= 1000000:
            HigherRate = GrossYear - 1000000
            HigherRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(HigherRate * 0.25))
            HigherRateTax.grid(row=5, column=1)
            BasicRate = Tk.Label(RightFrame, text='₹{:,.2f}'.format(150000 * 0.10))
            BasicRate.grid(row=4, column=1)
            AdditionalRateTax = Tk.Label(RightFrame, text='₹0.00')
            AdditionalRateTax.grid(row=6, column=1)
            TotalIn = (34449 * 0.10) + (HigherRate * 0.25)

        elif GrossYear <= 999999 and GrossYear >= 250001:
            BasicRate = GrossYear - 250001
            BasicRateTax = Tk.Label(RightFrame, text='₹{:,.2f}'.format(BasicRate * 0.10))
            BasicRateTax.grid(row=4, column=1)
            HigherRateTax = Tk.Label(RightFrame, text='₹0.00')
            HigherRateTax.grid(row=5, column=1)
            AdditionalRateTax = Tk.Label(RightFrame, text='₹0.00')
            AdditionalRateTax.grid(row=6, column=1)
            TotalIn = (BasicRate * 0.10)

        else:
            TotalIn = 0

        TotalNetTax = round(TotalIn)
        TotalNetTaxLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetTax))
        TotalNetTaxLi.grid(row=9, column=1)

        TotalNetWages = GrossYear - TotalNetTax
        TotalNetWagesMonthly = TotalNetWages / 12
        TotalNetWagesWeekly = TotalNetWages / 52
        TotalNetWagesDaily = TotalNetWages / 365
        TotalNetWagesLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWages))
        TotalNetWagesLi.grid(row=10, column=1)
        TotalNetWagesMonthlyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesMonthly))
        TotalNetWagesMonthlyLi.grid(row=10, column=2)
        TotalNetWagesWeeklyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesWeekly))
        TotalNetWagesWeeklyLi.grid(row=10, column=3)
        TotalNetWagesDailyLi = Tk.Label(RightFrame, text='₹{:,.2f}'.format(TotalNetWagesDaily))
        TotalNetWagesDailyLi.grid(row=10, column=4)

    LeftFrame = Tk.Frame(root, width=300, height=200, pady=3)
    RightFrame = Tk.Frame(root, width=400, height=200, pady=3)

    LeftFrame.grid(sticky="n", row=0, column=0)
    RightFrame.grid(sticky="n", row=0, column=1)

    TaxYearOp = Tk.StringVar()
    TaxYearOp.set("2020/2021")

    TaxYear = Tk.Label(LeftFrame, text="Select tax year")
    TaxYear.grid(row=1, column=0)

    Placeholder = Tk.Label(LeftFrame, text="")
    Placeholder.grid(row=1, column=1)

    TaxYearLi = Tk.OptionMenu(Placeholder, TaxYearOp, "2020/2021")
    TaxYearLi.grid(row=1, column=1)
    Placeholder2 = Tk.Label(LeftFrame, text="")
    Placeholder2.grid(row=2, column=1)
    Pension = Tk.Label(LeftFrame, text="Pension contributions (₹)")
    Pension.grid(row=3, column=0)
    PensionEn = Tk.Entry(LeftFrame)
    PensionEn.grid(row=3, column=1)
    GrossTaxLa = Tk.Label(LeftFrame, text="annual earnings here! >")
    GrossTaxLa.grid(row=4, column=0)
    GrossTaxIn = Tk.Entry(LeftFrame)
    GrossTaxIn.grid(row=4, column=1)
    TaxCalGo = Tk.Button(LeftFrame, text="Calculate My Wage", command=callback)
    TaxCalGo.grid(row=5, column=1)

    Summary = Tk.Label(RightFrame, text="Salary Summary", width=15)
    Summary.grid(row=0, column=0)
    Yearly = Tk.Label(RightFrame, text="Year", width=10)
    Yearly.grid(row=0, column=1)
    Monthly = Tk.Label(RightFrame, text="Monthly", width=10)
    Monthly.grid(row=0, column=2)
    Weekly = Tk.Label(RightFrame, text="Weekly", width=10)
    Weekly.grid(row=0, column=3)
    Daily = Tk.Label(RightFrame, text="Daily", width=10)
    Daily.grid(row=0, column=4)

    Summary = Tk.Label(RightFrame, text="Salary Summary", width=15)
    Summary.grid(row=0, column=0)
    GrossPay = Tk.Label(RightFrame, text="Gross Pay", width=15)
    GrossPay.grid(row=1, column=0)
    TaxFree = Tk.Label(RightFrame, text="Tax Free Allowance", width=15)
    TaxFree.grid(row=2, column=0)
    TotalTaxable = Tk.Label(RightFrame, text="Total Taxable", width=15)
    TotalTaxable.grid(row=3, column=0)
    Tax20 = Tk.Label(RightFrame, text="10% rate", width=15)
    Tax20.grid(row=4, column=0)
    Tax40 = Tk.Label(RightFrame, text="25% rate", width=15)
    Tax40.grid(row=5, column=0)
    Tax45 = Tk.Label(RightFrame, text="30% rate", width=15)
    Tax45.grid(row=6, column=0)
    TotalDeductions = Tk.Label(RightFrame, text="Total Deductions", width=15)
    TotalDeductions.grid(row=9, column=0)
    NetWage = Tk.Label(RightFrame, text="Net Wage", width=15)
    NetWage.grid(row=10, column=0)


def home():
    f1 = Frame(bg="#696969")
    f1.place(x=0, y=0, width=850, height=600)

    b2 = Button(f1, text="ENTER DETAILS", command=detail)
    b2.place(x=350, y=240, width=150, height=80)


home()
t.mainloop()
