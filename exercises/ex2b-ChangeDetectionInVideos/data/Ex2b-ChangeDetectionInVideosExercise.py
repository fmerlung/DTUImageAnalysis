import time
import cv2 as cv
import numpy as np
from skimage.util import img_as_float
from skimage.util import img_as_ubyte


def show_in_moved_window(win_name, img, x, y):
    """
    Show an image in a window, where the position of the window can be given
    """
    cv.namedWindow(win_name)
    cv.moveWindow(win_name, x, y)
    cv.imshow(win_name,img)


def capture_from_camera_and_show_images():
    print("Starting image capture")

    print("Opening connection to camera")
    url = 0
    use_droid_cam = True
    if use_droid_cam:
        url = "http://192.168.1.195:4747/video"
    cap = cv.VideoCapture(url)
    # cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    print("Starting camera loop")
    # Get first image
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame")
        exit()

    # Transform image to gray scale and then to float, so we can do some processing
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = img_as_float(frame_gray)
    background = frame_gray


    # To keep track of frames per second
    start_time = time.time()
    n_frames = 0
    stop = False
    while not stop:
        ret, new_frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break

        # Transform image to gray scale and then to float, so we can do some processing
        new_frame_gray = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY)
        new_frame_gray = img_as_float(new_frame_gray)


        # Compute background image
        alpha = 0.95
        background = alpha * background + (1-alpha)*new_frame_gray
        # Compute difference image
        dif_img = np.abs(new_frame_gray - background)


        # Compute binary image based on threshold
        T = 0.1
        ret, binary_img = cv.threshold(dif_img, T, 1, cv.THRESH_BINARY)
        ubyte_binary_img = np.array(img_as_ubyte(binary_img))
        flat = ubyte_binary_img.flatten()

        fore_pixels = np.count_nonzero((flat == 255))

        total_pixels = binary_img.shape[0] * binary_img.shape[1]       
        back_pixels = total_pixels - fore_pixels
        fore_percent = fore_pixels / total_pixels

        # Keep track of frames-per-second (FPS)
        n_frames = n_frames + 1
        elapsed_time = time.time() - start_time
        fps = int(n_frames / elapsed_time)

        # Put the FPS on the new_frame
        str_out = f"fps: {fps}"
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(new_frame, str_out, (100, 100), font, 1, 255, 1)

        alert_threshold = 0.05
        if (fore_percent > alert_threshold):
            cv.putText(new_frame, f"change detected!", (100, 150), font, 1, (1, 1, 255), 1)

        # Display the resulting frame
        show_in_moved_window('Input', new_frame, 0, 10)
        show_in_moved_window('Difference image', dif_img, 600, 10)
        show_in_moved_window('Binary image', ubyte_binary_img, 1200, 10)
        show_in_moved_window('Background', background, 0, 520)

        # Old frame is updated
        frame_gray = new_frame_gray

        if cv.waitKey(1) == ord('q'):
            stop = True

    print("Stopping image loop")
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    capture_from_camera_and_show_images()
