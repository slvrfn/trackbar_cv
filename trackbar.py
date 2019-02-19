
import cv2 as cv2
import copy

# Some helper functions.
def scale(factor): return lambda x: x*factor
def identity(x): return x
def param(count,initial_value = 0,adjust = identity ):
    return (lambda **kwargs: kwargs)(count=count,initial_value=initial_value,adjust=adjust)

#Display the trackbar window.
def display_trackbar_window(window_name,draw_method,compute_values,**kwargs):
    args = {}
    last_args = {}
    adjust_fns = {}
    def nothing(*a,**k): pass
    def to_tuple(count,initial_value,adjust): return count,initial_value,adjust
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL|cv2.WINDOW_KEEPRATIO|cv2.WINDOW_GUI_EXPANDED)
    for (key,value) in kwargs.items():
        count,initial_value,adjust = to_tuple(**value)
        adjust_fns[key] = adjust
        cv2.createTrackbar(key, window_name,initial_value,count, nothing)
    while(1):
        k = cv2.waitKey(1) & 0xFF
        if k==27:
            break
        for key,value in kwargs.items():
            trackBarPos = cv2.getTrackbarPos(key,window_name)
            args[key] = adjust_fns[key](trackBarPos)
        if args == last_args: continue
        last_args = copy.deepcopy(args)
        result = compute_values(**args)
        img = draw_method(result)
        cv2.imshow(window_name,img)
    cv2.destroyWindow(window_name)  
    return last_args
