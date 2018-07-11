import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates


import urllib
import json
import pandas as pd
import numpy as np



LARGE_FONT = ("Times", 16)
NORM_FONT = ("Times",  12)
SMALL_FONT = ("Times", 10)

'''Style for plot'''
style.use("ggplot")

'''Our plot object'''
f = plt.figure()
#a = f.add_subplot(111)

"""Default Graph and Exchange Values"""
exchange = "BTC-e"
Counter = 9000
programName = "btce"
resamplesize = "15min"
DataPace = "tick"
candleWidth = 0.008

paneCount = 1

"""Indicators"""
topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"
chartLoad = True
EMAs = []
SMAs = []


def tutorial():
##    def leavemini(what):
 ##       what.destroy()
        
    def page2():
        tut.destroy()
        tut2 = tk.Tk()
        
        def page3():
            tut2.destroy()
            tut3 = tk.Tk()
            
            tut3.wm_title("Part 3")
            label = ttk.Label(tut3,text="Part 3",font=NORM_FONT)
            label.pack(side="top",fill="x",pady=10)
            B1 = ttk.Button(tut3,text="Done!",command=tut3.destroy)
            B1.pack()
            tut3.mainloop()
            
        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2,text="Part 2",font=NORM_FONT)
        label.pack(side="top",fill="x",pady=10)
        B1 = ttk.Button(tut2,text="Done!",command=page3)
        B1.pack()
        tut2.mainloop()
        
    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut,text="What do you need help with?",font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
        
    B1 = ttk.Button(tut,text = "Overview of the application",command=page2)
    B1.pack()
    B2 = ttk.Button(tut,text = "How do I trade?",command=lambda:popupmsg("Not yet completed."))
    B2.pack()
    B1 = ttk.Button(tut,text = "Indicator Questions/Help",command=lambda:popupmsg("Not yet completed."))
    B1.pack()
def loadChart(run):
    global chartLoad
    
    if run == "Start":
        chartLoad = True
    elif run == "stop":
        chartLoad = False
        


def addMiddleIndicator(what):
    global middleIndicator
    global Counter
    
    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")
    
    if what != "none":
        if middleIndicator == "none":
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be.")
                label.pack(side='top',fill='x',pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                
                def callback():
                    global middleIndicators
                    global Counter
                    
                    middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicators.append(group)
                    Counter = 9000
                    print("Middle Indicator set to:",middleIndicators)
                    midIQ.destroy()
                    
                b = ttk.Button(midIQ,text="Submit",width=10,command=callback)
                b.pack()
                tk.mainloop()
                
            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side='top',fill='x',pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                
                def callback():
                    global middleIndicators
                    global Counter
                    
                    middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicators.append(group)
                    Counter = 9000
                    print("Middle Indicator set to:",middleIndicators)
                    midIQ.destroy()
                    
                b = ttk.Button(midIQ,text="Submit",width=10,command=callback)
                b.pack()
                tk.mainloop()
        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be.")
                label.pack(side='top',fill='x',pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                
                def callback():
                    global middleIndicators
                    global Counter
                    
                    #middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicators.append(group)
                    Counter = 9000
                    print("Middle Indicator set to:",middleIndicators)
                    midIQ.destroy()
                    
                b = ttk.Button(midIQ,text="Submit",width=10,command=callback)
                b.pack()
                tk.mainloop()
            
            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side='top',fill='x',pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                
                def callback():
                    global middleIndicators
                    global Counter
                    
                    #middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicators.append(group)
                    Counter = 9000
                    print("Middle Indicator set to:",middleIndicators)
                    midIQ.destroy()
                    
                b = ttk.Button(midIQ,text="Submit",width=10,command=callback)
                b.pack()
                tk.mainloop()
    
    else:
        middleIndicators = "none"


def addTopIndicator(what):
    global topIndicator
    global Counter
    
    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")
    elif what == "none":
        topIndicator = what
        Counter = 9000
    
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text = "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top",fill="x",pady=10)
        
        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()
        
        def callback():
            global topIndicator
            global Counter
            
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            topIndicator =  group
            Counter = 9000
            print("Set top indicator to",group)
            rsiQ.destroy()
        
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
        
    elif what == "macd":
        topIndicator = "macd"
        Counter = 9000

def addBottomIndicator(what):
    global bottomIndicator
    global Counter
    
    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")
    elif what == "none":
        bottomIndicator = what
        Counter = 9000
    
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text = "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top",fill="x",pady=10)
        
        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()
        
        def callback():
            global bottomIndicator
            global Counter
            
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            bottomIndicator =  group
            Counter = 9000
            print("Set bottom indicator to",group)
            rsiQ.destroy()
        
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
        
    elif what == "macd":
        bottomIndicator = "macd"
        Counter = 9000



"""Stock info time frame"""
def changeTimeFrame(tf):
    global DataPace
    global Counter
    if tf == "7d" and resamplesize == "1min":
        popupmsg("Too much data chosen, choose a smaller time frame or a higher OHLCI.")
    else:
        DataPace = tf
        Counter = 9000

"""Size of stock plot bars"""
def changeSampleSize(size,width):
    global resamplesize
    global Counter
    global candleWidth
    if DataPace == "7d" and resamplesize == "1min":
        popupmsg("Too much data chosen, choose a smaller time frame or a higher OHLCI.")
    elif DataPace == "tick":
        popupmsg("You're currently viewing tick data, not OHLC.")
    else:
        resamplesize = size
        Counter = 9000
        candleWidth = width

"""Selects the Bitcoin Exchange"""
def changeExchange(toWhat,pn):
    global exchange
    global Counter
    global programName
    
    exchange = toWhat
    programName = pn
    Counter = 9000




'''A pop up message window for functions under construction'''
def popupmsg(msg):
    
    popup = tk.Tk()
  
    popup.wm_title("BTC Message")
    label = ttk.Label(popup, text=msg,font=NORM_FONT)
    label.pack(side='top',fill='x',pady=10)
    B1 = ttk.Button(popup,text="Okay",command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
"""Loads BTC buy and sell data from exchange"""
def animate(i):
    global refreshRate
    global Counter
    
    if chartLoad:
        if paneCount == 1:
            if DataPace == "tick":
                try:
                    a = plt.subplot2grid((6,4),(0,0),rowspan=4,colspan=4)
                    a2= plt.subplot2grid((6,4),(5,0),rowspan=1,colspan=4,sharex = a)
        
                    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                    data = urllib.request.urlopen(dataLink)
                    data = data.read().decode("utf-8")
                    data = json.loads(data)
                    data = data["btc_usd"]
                    data = pd.DataFrame(data)
                    
                    data["datestamp"] = np.array(data['timestamp']).astype("datetime64[s]")
                    allDates = data["datestamp"].tolist()
                    
                    
                    """buys and sells are now a panda data set"""
                    buys = data[(data['type']=="bid")]
                    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
                    buyDates = (buys["datestamp"]).tolist()
                    
                    sells = data[(data['type']=="ask")]
                    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
                    sellDates = (sells["datestamp"]).tolist()
                    """Matplotlib does not recognize unix timestamps"""
                    
                    volume = data["amount"]
                    
                    
                    
                    a.clear()
                    
                    a.plot_date(buyDates, buys["price"],"#00A3E0", label="buys")
                    a.plot_date(sellDates, sells["price"],"#183A54", label="sells")
                    title = "BTC-e BTCUSD Prices\nLast Price: "+str(data["price"][1999])
                    a.set_title(title)
                    
                    a2.fill_between(allDates,0,volume,facecolor="#183A54")
                    
                    a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                    a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:M:S"))
                    
                    
                    a.legend(bbox_to_anchor=(0,1.02,1,.102), loc=3,ncol=2,borderaxespad=0)
                except Exception as e:
                    print("Failed because of:",e)
    
    
"""Class that initializes our application windows"""
class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC Client")

        container = ttk.Frame(self)
        container.pack(side="top",fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
  
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        exchangeChoice = tk.Menu(menubar,tearoff=1)
        exchangeChoice.add_command(label="BTC-e",command=lambda: changeExchange("BTC-e","btce"))
        
        exchangeChoice.add_command(label="Bitfinex",command=lambda: changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="BitsCamp",command=lambda: changeExchange("BitsCamp","bitscamp"))
        exchangeChoice.add_command(label="Huobi",command=lambda: changeExchange("Huobi","huobi"))
        
        menubar.add_cascade(label="Exchange",menu=exchangeChoice)
    
        dataTF = tk.Menu(menubar,tearoff=1)
        dataTF.add_command(label = "Tick",command=lambda: changeTimeFrame('tick'))
        dataTF.add_command(label = "1 Day",command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label = "3 Day", command=lambda: changeTimeFrame('3d'))
        dataTF.add_command(label = "1 Week",command=lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label = "Data Time Frame", menu = dataTF)
        
        OHLCI = tk.Menu(menubar,tearoff=1)
        OHLCI.add_command(label="1 Minute",command=lambda: changeSampleSize('1min',0.0005))
        OHLCI.add_command(label="5 Minutes",command=lambda: changeSampleSize('5min',0.0005))
        OHLCI.add_command(label="15 Minutes",command=lambda: changeSampleSize('15min',0.0005))
        OHLCI.add_command(label="30 Minutes",command=lambda: changeSampleSize('30min',0.0005))
        OHLCI.add_command(label="1 Hour",command=lambda: changeSampleSize('1H',0.0005))
        OHLCI.add_command(label="3 Hours",command=lambda: changeSampleSize('3H',0.0005))
        menubar.add_cascade(label = "OHLCI", menu = OHLCI)
        tk.Tk.config(self, menu=menubar)
    
        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None", 
                            command = lambda: addTopIndicator('none'))
        topIndi.add_command(label="RSI", 
                            command = lambda: addTopIndicator('rsi'))
        topIndi.add_command(label="MACD", 
                            command = lambda: addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)
    
        
        mainIndi = tk.Menu(menubar, tearoff=1)
        mainIndi.add_command(label="None", 
                            command = lambda: addMiddleIndicator('none'))
        mainIndi.add_command(label="SMA", 
                            command = lambda: addMiddleIndicator('sma'))
        mainIndi.add_command(label="EMA", 
                            command = lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label="Main/Middle Indicator", menu=mainIndi)
        
        
        bottomIndi = tk.Menu(menubar, tearoff=1)
        bottomIndi.add_command(label="None", 
                            command = lambda: addBottomIndicator('none'))
        bottomIndi.add_command(label="RSI", 
                            command = lambda: addBottomIndicator('rsi'))
        bottomIndi.add_command(label="MACD", 
                            command = lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label="Bottom Indicator", menu=bottomIndi)
    
        tradeButton = tk.Menu(menubar,tearoff=1)
        tradeButton.add_command(label = "Manual Trading",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label = "Automated Trading",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        
        tradeButton.add_command(label = "Quick Buy",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label = "Quick Sell",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label = "Set-up Quick Buy/Sell",
                                command=lambda: popupmsg("This is not live yet"))
        menubar.add_cascade(label="Trading",menu=tradeButton)
        
        startStop = tk.Menu(menubar, tearoff =1)
        startStop.add_command(label="resume",
                              command = lambda: loadChart('start'))
        startStop.add_command(label="pause",
                              command = lambda: loadChart('stop'))
        menubar.add_cascade(label="Resume/Pause client",menu=startStop)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)
        
        menubar.add_cascade(label="Help",menu=helpmenu)
        
        
        self.frames = {}

        for F in (StartPage, BTCe_Page):
        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
            self.show_frame(StartPage)

    """Raises the given frame from the dictionary"""
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

"""The first page the user sees."""
class StartPage(tk.Frame):

    def __init__(self, parent, controller): #parent is SeaofBTCapp class
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="""ALPHA Bitcoin Trading Application. Use at your own risk. There is no promise of warranty.""", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Agree",command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()

        button5 = ttk.Button(self, text="Disagree",command=quit)
        button5.pack()
        
        
        
"""Spare Page"""
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label2 = ttk.Label(self, text="Page 1", font=LARGE_FONT)
        label2.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button2.pack()

        button3 = ttk.Button(self, text="Page 2",command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        
        button4 = ttk.Button(self, text="Graph Page",command=lambda: controller.show_frame(PageThree))
        button4.pack()
        
        
"""Our Bitcoin Exchange Graph window. Has canvas and toolbar."""
class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label4 = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label4.pack(pady=10,padx=10)

        button6 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button6.pack()

       
        
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack()
        

"""Main window initialization."""
app = SeaofBTCapp()
app.geometry("1280x720")
"""A MatPlotLib object. Takes animate definition as param. 1 second = 1000"""
ani = animation.FuncAnimation(f,animate, interval=1000)
app.mainloop()

        

        
        
