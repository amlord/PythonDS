from pythonds.basic.queue import Queue

__author__ = 'Lawrence'

def hotPotato(namelist, k):
    """
    Simulate the children's game Hot Potato. In this game children line up in a
    circle and pass an item from neighbor to neighbor as fast as they can. At a
    certain point in the game, the action is stopped and the child who has the
    item (the potato) is removed from the circle.
    :param namelist: A list of children's name involved in this game, required
                     to be nonempty.
    :param k: the position of child to be removed from the circular namelist
              counting from the front of the queue (The front one is assumed
              to be at position 0).

    :return: the name of the last person remaining after repetitive counting
             by k.
    """
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(k):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()