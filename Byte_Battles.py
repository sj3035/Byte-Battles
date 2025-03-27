import cv2

def identify_ather(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Error: Image not found or unable to read the file. Check the path!")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the function
identify_ather("C:\\Users\\sjaya\\Downloads\\ather_scooter.jpg")

