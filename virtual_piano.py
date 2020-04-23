import cv2
import numpy as np
import pyaudio
import time

cam = cv2.VideoCapture(0)
p = pyaudio.PyAudio()


font = cv2.FONT_HERSHEY_SIMPLEX

i = 0

def play_audio(freq):
    volume = 1    
    fs = 44100      
    duration = 1
    time.sleep(0.005)
    f = freq  

    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs + f)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    stream.write(volume*samples)

    # stream.stop_stream()

    # stream.close()


while(True):

    ret,frame = cam.read()
    frame = cv2.flip(frame,1)

    act_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    image = frame.copy()

    image[:360,:,:] = (0,0,0) 

    image[:360,200:300,:] = (255,255,255)
    cv2.putText(image,f"C4",(230,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(image,f"D4",(330,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    image[:360,400:500,:] = (255,255,255)
    cv2.putText(image,f"E4",(430,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(image,f"F4",(530,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    image[:360,600:700,:] = (255,255,255)
    cv2.putText(image,f"G4",(630,300), font, 1,(0,255,0),2,cv2.LINE_AA)

    image[:360,800:900,:] = (255,255,255)
    cv2.putText(image,f"H4",(730,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    image[:360,1000:1100,:] = (255,255,255)
    cv2.putText(image,f"A4",(830,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(image,f"B4",(930,300), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(image,f"C4",(1030,300), font, 1,(0,255,0),2,cv2.LINE_AA)


    roi1 = frame[:360,200:300,:]
    roi2 = frame[:360,300:400,:]
    roi3 = frame[:360,400:500,:]
    roi4 = frame[:360,500:600,:]
    roi5 = frame[:360,600:700,:]
    roi6 = frame[:360,700:800,:]
    roi7 = frame[:360,800:900,:]
    roi8 = frame[:360,900:1000,:]
    roi9 = frame[:360,1000:1100,:]

    gray1 = cv2.cvtColor(roi1,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY)
    hist1 = cv2.calcHist([thresh1],[0],None,[256],[0,256])

    gray2 = cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
    hist2 = cv2.calcHist([thresh2],[0],None,[256],[0,256])

    gray3 = cv2.cvtColor(roi3,cv2.COLOR_BGR2GRAY)
    ret,thresh3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY)
    hist3 = cv2.calcHist([thresh3],[0],None,[256],[0,256])

    gray4 = cv2.cvtColor(roi4,cv2.COLOR_BGR2GRAY)
    ret,thresh4 = cv2.threshold(gray4,127,255,cv2.THRESH_BINARY)
    hist4 = cv2.calcHist([thresh4],[0],None,[256],[0,256])

    gray5 = cv2.cvtColor(roi5,cv2.COLOR_BGR2GRAY)
    ret,thresh5 = cv2.threshold(gray5,127,255,cv2.THRESH_BINARY)
    hist5 = cv2.calcHist([thresh5],[0],None,[256],[0,256])

    gray6 = cv2.cvtColor(roi6,cv2.COLOR_BGR2GRAY)
    ret,thresh6 = cv2.threshold(gray6,127,255,cv2.THRESH_BINARY)
    hist6 = cv2.calcHist([thresh6],[0],None,[256],[0,256])

    gray7 = cv2.cvtColor(roi7,cv2.COLOR_BGR2GRAY)
    ret,thresh7 = cv2.threshold(gray7,127,255,cv2.THRESH_BINARY)
    hist7 = cv2.calcHist([thresh7],[0],None,[256],[0,256])

    gray8 = cv2.cvtColor(roi8,cv2.COLOR_BGR2GRAY)
    ret,thresh8 = cv2.threshold(gray8,127,255,cv2.THRESH_BINARY)
    hist8 = cv2.calcHist([thresh8],[0],None,[256],[0,256])

    gray9 = cv2.cvtColor(roi9,cv2.COLOR_BGR2GRAY)
    ret,thresh9 = cv2.threshold(gray9,127,255,cv2.THRESH_BINARY)
    hist9 = cv2.calcHist([thresh9],[0],None,[256],[0,256])

    T = 1200

    if(i>1):
        if(hist1[0]>T):
            print("Key1 Pressed")
            image = cv2.rectangle(image, (200,0), (300,360), (255,0,0), 5)
            play_audio(261)
        if(hist2[0]>T):
            print("Key2 Pressed")
            image = cv2.rectangle(image, (300,0), (400,360), (255,0,0), 5)
            play_audio(294)
        if(hist3[0]>T):
            print("Key3 Pressed")
            image = cv2.rectangle(image, (400,0), (500,360), (255,0,0), 5)
            play_audio(330)
        if(hist4[0]>T):
            print("Key4 Pressed")
            image = cv2.rectangle(image, (500,0), (600,360), (255,0,0), 5)
            play_audio(349)
        if(hist5[0]>T):
            print("Key5 Pressed")
            image = cv2.rectangle(image, (600,0), (700,360), (255,0,0), 5)
            play_audio(392)
        if(hist6[0]>T):
            print("Key6 Pressed")
            image = cv2.rectangle(image, (700,0), (800,360), (255,0,0), 5)
            play_audio(440)
        if(hist7[0]>T):
            print("Key7 Pressed")
            image = cv2.rectangle(image, (800,0), (900,360), (255,0,0), 5)
            play_audio(494)
        if(hist8[0]>T):
            print("Key8 Pressed")
            image = cv2.rectangle(image, (900,0), (1000,360), (255,0,0), 5)
            play_audio(515)
        if(hist9[0]>T):
            print("Key9 Pressed")
            image = cv2.rectangle(image, (1000,0), (1100,360), (255,0,0), 5)
            play_audio(261)

    cv2.putText(image,f"SAI VARUN",(10,150), font, 1,(0,255,0),2,cv2.LINE_AA)

    cv2.putText(image,f"KODATHALA",(10,200), font, 1,(0,0,255),2,cv2.LINE_AA)



    cv2.putText(image,f"VIRTUAL",(1120,150), font, 1,(255,255,0),2,cv2.LINE_AA)

    cv2.putText(image,f"PIANO",(1120,200), font, 1,(255,255,0),2,cv2.LINE_AA)


    cv2.imshow('PIANO',image)

    i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# stream.stop_stream()

# stream.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
p.terminate()