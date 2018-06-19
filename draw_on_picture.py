import cv2

img_c = cv2.imread('flaming.jpeg', cv2.IMREAD_COLOR)
# (0,200,0 ) -> color BGP
# 10 -> grubość
# (200,180) -> wsporzedna lewego gornego rogu
# (320,350) -> wsporzedna prawego dolnego rogu

img = cv2.rectangle(img_c, (200,180),(320,350),(0,200,0),10)
font = cv2.FONT_HERSHEY_SIMPLEX
# (80,800) -> wsporzedna pierwszej literki
#(0,255,255) -? kolor napisu
# 2 - wielkośc czcionki
# 10 - grubosc

cv2.putText(img, 'Umiem obrazy!', (80,800), font, 2, (0,255,255), 10, cv2.LINE_AA )
cv2.imshow('flaming gray', img)
key = cv2.waitKey(0)
if key == 27:
   cv2.destroyAllWindows()
