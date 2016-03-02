class make_queue:

  def __init__(self):
    self.queue=[]

  def add_to_queue(self,item):
    self.queue.append(item)

  def remove_from_front(self):
    return self.queue.pop(0)
