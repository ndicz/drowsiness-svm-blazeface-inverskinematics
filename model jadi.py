from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import math
import time
import csv

import pandas as pd
import pickle
import serial
ard = serial.Serial('COM6', 9600) 

filename = 'ngantuk_modelp'
loaded_model = pickle.load(open(filename,'rb'))
y_pred_test = loaded_model.predict
y_pred_test_count = 0

time_interval = 0
time_prev = 0

filename = 'coba.csv'

fx = 0
fy = 0

fx1 = 0
fy1 = 0

fx2 = 0
fy2 = 0

fx3 = 0
fy3 = 0

fx4 = 0
fy4 = 0

fx5 = 0
fy5 = 0

fx6 = 0
fy6 = 0

fx7 = 0
fy7 = 0

fx8 = 0
fy8 = 0
mouth_x = 0
mouth_y = 0

l_eye_val = 0
r_eye_val = 0
fx9 = 0
fy9 = 0

fx10 = 0
fy10 = 0

fx11 = 0
fy11 = 0

fx12 = 0
fy12 = 0

fx_imaginer = 0
fy_imaginer = 0

face_length = 0
face_degree = 0

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(0)

cap.set(3, 800)
cap.set(4, 720)
detector = FaceMeshDetector(0.5)

filename = 'coba.csv'

ngantuk_state = 0
ngantuk_state_prev = 0

y_pred_test_prev = ""

ngantuk_count = 0

kedip = "tidak"
kedip_prev = "tidak"
kedip_count=0
total_kedip = 0

kepala_miring = "tidak"
kepala_miring_prev = "tidak"
kepala_miring_count = 0
total_kepala_miring = 0

mulut_nguap = "tidak"
mulut_nguap_prev = "tidak"
mulut_nguap_count = 0
total_nguap = 0



time_csv=0
time_csv_prev=0

with open(filename, 'a') as csvfile:
    print("write")

    csvwriter = csv.writer(csvfile)


    csvwriter.writerow(['jumlah kedip', 'jumlah kepala miring', 'jumlah menguap', 'kondisi'])

while True:

    success, img = cap.read()
    success, img2 = cap.read()
    img, faces = detector.findFaceMesh(img)
    cv2.putText(img, str("SETPOINT BALL"), (0, 500), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 0), 3)
    if faces:
        fx, fy = faces[0][410]
        fx1, fy1 = faces[0][186]
        fx2, fy2 = faces[0][0]
        fx3, fy3 = faces[0][17]
        fx4, fy4 = faces[0][378]
        fx5, fy5 = faces[0][159]
        fx6, fy6 = faces[0][145]
        fx7, fy7 = faces[0][386]
        fx8, fy8 = faces[0][374]

        fx9, fy9 = faces[0][234]

        fx10, fy10 = faces[0][347]

        fx11, fy11 = faces[0][10]
        fx12, fy12 = faces[0][152]

        fx_imaginer = fx11
        fy_imaginer = fy12
        imaginer_length = 0

        cv2.circle(img, (fx11, fy12), 10, (0, 0, 0), cv2.FILLED)
        cv2.line(img, (fx, fy), (fx1, fy1), (255, 255, 255), 3)
        mouth_x = math.sqrt(pow((fx1 - fx), 2) + pow((fy1 - fy), 2))
        mouth_y = math.sqrt(pow((fx3 - fx2), 2) + pow((fy3 - fy2), 2))
        l_eye_val = math.sqrt(pow((fx5 - fx6), 2) + pow((fy5 - fy6), 2))
        r_eye_val = math.sqrt(pow((fx7 - fx8), 2) + pow((fy7 - fy8), 2))
        face_length = math.sqrt(pow((fx12 - fx11), 2) + pow((fy12 - fy11), 2))


        cv2.line(img, (fx2, fy2), (fx3, fy3), (255, 255, 255), 3)

        cv2.putText(img, str("x mulut :"), (fx4, fy4), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        cv2.putText(img, str(round(mouth_x, 0)), (fx4 + 80, fy4), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        cv2.putText(img, str("y mulut :"), (fx4, fy4 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        cv2.putText(img, str(round(mouth_y, 0)), (fx4 + 80, fy4 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        cv2.putText(img, str("L eye val :"), (fx9, fy9), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        cv2.putText(img, str(round(l_eye_val, 0)), (fx9, fy9 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        cv2.putText(img, str("R eye val :"), (fx10, fy10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        cv2.putText(img, str(round(r_eye_val, 0)), (fx10, fy10 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        cv2.putText(img, str("jumlah kedip : ") + str(kedip_count) , (0, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, str("jumlah mulut : ") + str(mulut_nguap_count), (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, str("jumlah kepala miring : ") + str(kepala_miring_count), (0, 250), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, str("Kondisi : ") + str(y_pred_test), (0, 100), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)



        cv2.line(img, (fx5, fy5), (fx6, fy6), (255, 0, 0), 3)
        cv2.line(img, (fx7, fy7), (fx8, fy8), (255, 255, 255), 3)

        cv2.line(img, (fx11, fy11), (fx12, fy12), (255, 255, 255), 3)
        cv2.line(img, (fx12, fy12), (fx_imaginer, fy_imaginer), (255, 255, 255), 3)
        imaginer_length = math.sqrt(pow((fx12 - fx_imaginer), 2) + pow((fy12 - fy_imaginer), 2))
        data_test = str(kedip_count)
        cv2.putText(img, str(round(imaginer_length, 0)), (fx12, fy12 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255),
                    2)
        cv2.putText(img, str(round(face_length, 0)), (fx12, fy12 + 40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        face_degree = math.degrees(math.acos((imaginer_length / face_length)))
        cv2.putText(img, str(round(face_degree, 0)), (fx12, fy12 + 60), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        if ((mouth_x > 130) and (mouth_y > 100) and (l_eye_val < 15) and (r_eye_val < 15) or (face_degree < 86)):


            ngantuk_state = 1
        else:

            ngantuk_state = 0




    cv2.imshow("stress detector", img)
    cv2.imshow("no imaginer", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time_interval = time.time() - time_prev


    if time_interval > 0.5:

        if ngantuk_state != ngantuk_state_prev:
            ngantuk_count = ngantuk_count + 0.5
            if ngantuk_state == 1:

                pass

        ngantuk_state_prev = ngantuk_state

        ngantuk_state_prev = ngantuk_state


        if ((l_eye_val < 15) and (r_eye_val < 15)):
            kedip = "yes"
        else:
            kedip = "no"

        if (face_degree < 76):
            kepala_miring = "yes"
        else:
            kepala_miring = "no"

        if ((mouth_x > 130) and (mouth_y > 100)):
            mulut_nguap = "yes"

        else:
            mulut_nguap = "no"


        ############ngitung kedip########
        if (kedip_prev != kedip):
            if (kedip == "yes"):
                kedip_count = kedip_count + 1



        ############ngitung kepala########
        if (kepala_miring_prev != kepala_miring):
            if (kepala_miring_prev == "yes"):
                kepala_miring_count = kepala_miring_count + 1

        #############mulut count ##############
        if (mulut_nguap_prev != mulut_nguap):
            if (mulut_nguap_prev == "yes"):
                mulut_nguap_count = mulut_nguap_count + 1




        kedip_prev = kedip
        kepala_miring_prev = kepala_miring
        mulut_nguap_prev = mulut_nguap

        time_prev = time.time()

    time_csv = time.time() - time_csv_prev
    if (time_csv > 10):
        with open(filename, 'a') as csvfile:

            csvwriter = csv.writer(csvfile)
            fitur_test = [[str(kedip_count), str(kepala_miring_count), str(mulut_nguap_count)]]
            y_pred_test = loaded_model.predict(fitur_test)
            print(y_pred_test)
            if(y_pred_test =="mengantuk"):
                y_pred_test_count= y_pred_test_count + 1
                ard.write(str(1).encode()) 
                if y_pred_test == 1:
                    cv2.imwrite((str(y_pred_test) + '.png'), img2)
            else:
            
                ard.write(str(2).encode())
            y_pred_test_prev = y_pred_test


            csvwriter.writerow([str(kedip_count), str(kepala_miring_count), str(mulut_nguap_count), str(y_pred_test)])
            total_kedip = kedip_count + total_kedip
            total_nguap = mulut_nguap_count + total_nguap
            total_kepala_miring = kepala_miring_count + total_kepala_miring
            kedip_count = 0
            kepala_miring_count = 0
            mulut_nguap_count = 0

        time_csv_prev = time.time()

    print(time_csv)

cap.release()
cv2.destroyAllWindows()
