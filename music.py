import pyglet


flag = False


def change_source(number_alarm):
    global source
    global flag
    flag = True
    source = pyglet.media.load("file" + str(number_alarm) + ".mp3", streaming=False)


def start():
    global song
    global source
    global flag

    song = pyglet.media.Player()

    if not flag:
        source = pyglet.media.load("file1.mp3", streaming=False)
        song.queue(source=source)
        song.play()
    else:
        song.queue(source=source)
        song.play()


def stop():
    global song
    song.pause()
