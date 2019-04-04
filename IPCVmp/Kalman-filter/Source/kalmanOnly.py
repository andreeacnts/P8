import os
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

face_cascade = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_smile.xml')



def detect_one_face(im):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 3)
    if len(faces) == 0:
        return (0, 0, 0, 0)
    return faces[0]


def hsv_histogram_for_window(frame, window):
    # set up the ROI for tracking
    c, r, w, h = window
    roi = frame[r:r + h, c:c + w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return roi_hist


def resample(weights):
    n = len(weights)
    indices = []
    C = [0.] + [sum(weights[:i + 1]) for i in range(n)]
    u0, j = np.random.random(), 0
    for u in [(u0 + i) / n for i in range(n)]:
        while u > C[j]:
            j += 1
        indices.append(j - 1)
    return indices


def draw_on_image(ret, frame):
    # find four vertices of the rectangle from ret
    pt = cv2.boxPoints(ret)
    # round them to integers
    pt = np.int0(np.around(pt))
    img = cv2.polylines(
        img=frame,
        pts=[pt],
        isClosed=True,
        color=255,
        thickness=2
    )
    cv2.imshow('img', img)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        return



def display_kalman2(frame, pos):
    pt = np.int0(np.around(pos))
    img = cv2.circle(frame, (pt[0], pt[1]), 10, (0, 255, 0), -1)

    cv2.imshow('img', frame)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        return


def display_kalman3(frame, pos, ret):
    pt = np.int0(np.around(pos))
    img = cv2.circle(frame, (pt[0], pt[1]), 10, (0, 255, 0), -1)
    pt1 = (ret[0],ret[1])
    pt2 = (ret[0]+ret[2],ret[1]+ret[3])

    cv2.rectangle(img, pt1, pt2, (0, 255, 0), 3)


    cv2.imshow('img', frame)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        return

def display_of(frame , mask, pos):

    frame = cv2.circle(frame, (pos[0], pos[1]), 5)
    img = cv2.add(frame, mask)
    cv2.imshow('frame', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        return

def skeleton_tracker(v, file_name):
    # Open output file
    output_name = sys.argv[3] + file_name
    output = open(output_name, "w")

    frameCounter = 0
    # read first frame
    ret, frame = v.read()
    if ret == False:
        return

    # detect face in first frame
    c, r, w, h = detect_one_face(frame)

    # Write track point for first frame
    output.write("%d,%d,%d\n" % pt)  # Write as 0,pt_x,pt_y
    frameCounter = frameCounter + 1

    # set the initial tracking window
    track_window = (c, r, w, h)

    # calculate the HSV histogram in the window
    # NOTE: you do not need this in the Kalman, Particle or OF trackers
    roi_hist = hsv_histogram_for_window(frame, (c, r, w, h))  # this is provided for you

    # initialize the tracker
    # e.g. kf = cv2.KalmanFilter(4,2,0)
    # or: particles = np.ones((n_particles, 2), int) * initial_pos

    while (1):
        ret, frame = v.read()  # read another frame
        if ret == False:
            break

        # perform the tracking
        # e.g. cv2.meanShift, cv2.CamShift, or kalman.predict(), kalman.correct()

        # use the tracking result to get the tracking point (pt):
        # if you track a rect (e.g. face detector) take the mid point,
        # if you track particles - take the weighted average
        # the Kalman filter already has the tracking point in the state vector

        # write the result to the output file
        output.write("%d,%d,%d\n" % pt)  # Write as frame_index,pt_x,pt_y
        frameCounter = frameCounter + 1

    output.close()





def kalman_filter_tracker(v, file_name):
    # Open output file
    output_name = sys.argv[3] + file_name
    output = open(output_name, "w")

    frameCounter = 0
    # read first frame
    ret, frame = v.read()
    if not ret:
        return

    # detect face in first frame
    c, r, w, h = detect_one_face(frame)

    # Write track point for first frame
    pt = (0,   c + w/2.0, r + h/2.0)
    output.write("%d,%d,%d\n" % pt)  # Write as 0,pt_x,pt_y
    frameCounter += 1

    kalman = cv2.KalmanFilter(4, 2, 0)

    state = np.array([c + w / 2, r + h / 2, 0, 0], dtype='float64')  # initial position
    kalman.transitionMatrix = np.array([[1., 0., .1, 0.],
                                        [0., 1., 0., .1],
                                        [0., 0., 1., 0.],
                                        [0., 0., 0., 1.]])
    kalman.measurementMatrix = 1. * np.eye(2, 4)
    kalman.processNoiseCov = 1e-5 * np.eye(4, 4)
    kalman.measurementNoiseCov = 1e-3 * np.eye(2, 2)
    kalman.errorCovPost = 1e-1 * np.eye(4, 4)
    kalman.statePost = state
    while (1):
        # use prediction or posterior as your tracking result
        ret, frame = v.read()  # read another frame
        if not ret:
            break

        img_width = frame.shape[0]
        img_height = frame.shape[1]

        def calc_point(angle):
            return (np.around(img_width / 2 + img_width / 3 * np.cos(angle), 0).astype(int),
                    np.around(img_height / 2 - img_width / 3 * np.sin(angle), 1).astype(int))

        # e.g. cv2.meanS    hift, cv2.CamShift, or kalman.predict(), kalman.correct()

        # use the tracking result to get the tracking point (pt):
        # if you track a rect (e.g. face detector) take the mid point,
        # if you track particles - take the weighted average
        # the Kalman filter already has the tracking point in the state vector

        prediction = kalman.predict()

        pos = 0
        c, r, w, h = detect_one_face(frame)
        if w != 0 and h != 0:
            state = np.array([c + w / 2, r + h / 2, 0, 0], dtype='float64')
            # kalman.statePost = state
            measurement = (np.dot(kalman.measurementNoiseCov, np.random.randn(2, 1))).reshape(-1)
            measurement = np.dot(kalman.measurementMatrix, state) + measurement
            posterior = kalman.correct(measurement)
            pos = (posterior[0], posterior[1])
        else:
            measurement = (np.dot(kalman.measurementNoiseCov, np.random.randn(2, 1))).reshape(-1)
            measurement = np.dot(kalman.measurementMatrix, state) + measurement
            pos = (prediction[0], prediction[1])

        # display_kalman3(frame, pos, (c, r, w, h))
        process_noise = np.sqrt(kalman.processNoiseCov[0, 0]) * np.random.randn(4, 1)
        state = np.dot(kalman.transitionMatrix, state) + process_noise.reshape(-1)

        pt = (frameCounter, pos[0], pos[1])
        if frameCounter != 256:
            output.write("%d,%d,%d\n" % pt) # Write as frame_index,pt_x,pt_y
        else:
            output.write("%d,%d,%d" % pt)  # Write as frame_index,pt_x,pt_y
        frameCounter += 1
    output.close()






if __name__ == '__main__':
    question_number = -1

    # Validate the input arguments
    if (len(sys.argv) != 4):
        help_message()
        sys.exit()
    else:
        question_number = int(sys.argv[1])
        if (question_number > 4 or question_number < 1):
            print("Input parameters out of bound ...")
            sys.exit()

    # read video file
    video = cv2.VideoCapture(sys.argv[2]);

    if (question_number == 1):
        CAM_shift_tracker(video, "output_camshift.txt")
    elif (question_number == 2):
        particle_filter_tracker(video, "output_particle.txt")
    elif (question_number == 3):
        kalman_filter_tracker(video, "output_kalman.txt")
    elif question_number == 4:
        optical_flow_tracker(video, "output_of.txt")

'''
For Kalman Filter:

# --- init

state = np.array([c+w/2,r+h/2,0,0], dtype='float64') # initial position
kalman.transitionMatrix = np.array([[1., 0., .1, 0.],
                                    [0., 1., 0., .1],
                                    [0., 0., 1., 0.],
                                    [0., 0., 0., 1.]])
kalman.measurementMatrix = 1. * np.eye(2, 4)
kalman.processNoiseCov = 1e-5 * np.eye(4, 4)
kalman.measurementNoiseCov = 1e-3 * np.eye(2, 2)
kalman.errorCovPost = 1e-1 * np.eye(4, 4)
kalman.statePost = state


# --- tracking

prediction = kalman.predict()

# ...
# obtain measurement

if measurement_valid: # e.g. face found
    # ...
    posterior = kalman.correct(measurement)

# use prediction or posterior as your tracking result
'''

'''
For Particle Filter:

# --- init

# a function that, given a particle position, will return the particle's "fitness"
def particleevaluator(back_proj, particle):
    return back_proj[particle[1],particle[0]]

# hist_bp: obtain using cv2.calcBackProject and the HSV histogram
# c,r,w,h: obtain using detect_one_face()
n_particles = 200

init_pos = np.array([c + w/2.0,r + h/2.0], int) # Initial position
particles = np.ones((n_particles, 2), int) * init_pos # Init particles to init position
f0 = particleevaluator(hist_bp, pos) * np.ones(n_particles) # Evaluate appearance model
weights = np.ones(n_particles) / n_particles   # weights are uniform (at first)


# --- tracking

# Particle motion model: uniform step (TODO: find a better motion model)
np.add(particles, np.random.uniform(-stepsize, stepsize, particles.shape), out=particles, casting="unsafe")

# Clip out-of-bounds particles
particles = particles.clip(np.zeros(2), np.array((im_w,im_h))-1).astype(int)

f = particleevaluator(hist_bp, particles.T) # Evaluate particles
weights = np.float32(f.clip(1))             # Weight ~ histogram response
weights /= np.sum(weights)                  # Normalize w
pos = np.sum(particles.T * weights, axis=1).astype(int) # expected position: weighted average

if 1. / np.sum(weights**2) < n_particles / 2.: # If particle cloud degenerate:
    particles = particles[resample(weights),:]  # Resample particles according to weights
# resample() function is provided for you
'''
