# Stock App
This was made with PyQt it uses yfincese libery to pull stock data from yahoo. Then uses pandas to put it within a CSV file or a Excel file. 

![Stock App](/Stockapp.png)

## This is only a Demo of my GUI work. 

# Some of the code. 
~~~
   def showdata(self):
       obj = yf.Ticker(self.txt_stcok.text())
       if self.ck_enable.isChecked() == False:
            data = obj.history()  
            self.txtb_display.insertPlainText(str(data))
       else:
            data = obj.history(interval=str(self.cb_Per.currentText()), start=str(self.date_start.text()), end=str(self.date_end.text()))
            self.txtb_display.insertPlainText(str(data))
        
    #converts data to execl file
    def conExecl(self):
      datafrme = self.txtb_display.toPlainText()
      data = datafrme.split()
      print("Data is being put on file.")
      df = pa.DataFrame(data)
      df.to_excel('output.xlsx', index=False)
      
        
    #converts data to csv file
    def conCSV(self):
       dataframe = self.txtb_display.toPlainText()
       data = dataframe.split()
       print("Data is being put on file.")
       df = pa.DataFrame(data)
       df.to_csv('output.csv', index=False)

~~~
