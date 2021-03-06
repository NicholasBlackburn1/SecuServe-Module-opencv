"""
this class is for hopefully geting opencv camera to thread correctly
"""
import imports

class ThreadingClass:
  # initiate threading class
  def __init__(self, name):
    self.cap = imports.cv2.VideoCapture(name, imports.cv2.CAP_GSTREAMER)

	# define an empty queue and thread
    self.q = imports.queue.Queue()
    t = imports.threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read the frames as soon as they are available
  # this approach removes OpenCV's internal buffer and reduces the frame lag
  def _reader(self):
    while True:
      ret, frame = self.cap.read() # read the frames and ---
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()
        except imports.queue.Empty:
          pass
      self.q.put(frame) # --- store them in a queue (instead of the buffer)

  def read(self):
    return self.q.get() # fetch frames from the queue one by one

  def release(self):
    return self.cap.release() # release the hw resource