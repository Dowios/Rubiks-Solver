# Rubiks-Solver

確定你已有以下模組：
* Opencv
* PySerial

## ConnectArduino.py
輸入一串字串如"U R Ri L F X E D"，可控制Arduino轉動魔術方塊機器的馬達。 <br>
如果要與Arduino通訊，請將ConnectArduino.py中的兩個註解啟用，並將'COM9'改成Arduino的序列埠： <br>
> #ser = serial.Serial('COM9', 9600) <br>
> #ser.write(move.encode())
## Camera.py
開啟Webcam後，先以滑鼠點擊紅、橘、黃、綠、藍、白進行校正。 <br>
校正完可以點擊魔術方塊上任何一面，將會輸出其顏色代碼(ROYGBW)
