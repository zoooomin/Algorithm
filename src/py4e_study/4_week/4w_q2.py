a = '''Yeah yeah
The last few months
I've been workin' on me baby
There's so much trauma in my life
I've been so cold to the ones
who loved me baby
I look back now and I realize
And I remember when I held you
You begged me
with your drowning eyes to stay
And I regret I didn't tell you
Now I can't keep you
from loving him
You made up your mind
Say I love you girl
but I'm out of time
Say I'm there for you
but I'm out of time
Say that I'll care for you
but I'm out of time
Said I'm too late
to make you mine
out of time Ah
If he mess up just a little
Baby you know my line
If you don't trust him a little
Then come right back girl
come right back
Give me one chance just a little
Baby I'll treat you right
And I'll love you
like I shoulda loved you
all the time
And I remember when I held you
Held you baby
You begged me
with your drowning eyes to stay
Never again baby
And I regret I didn't tell you
Hey
Now I can't keep you
from loving him
You made up your mind Uh
Say I love you girl
but I'm out of time
Say I'm there for you
but I'm out of time
Say that I'll care for you
but I'm out of time
Said I'm too late
to make you mine
out of time Ah
Ooh singin' out of time
Said I had you to myself
but I'm out of time
Say that I'll care for you
but I'm out of time
But I'm too late
to make you mine
out of time
Out of time
Out of time
Don't you dare touch that dial
Because like the song says
you are out of time
You're almost there
but don't panic
There's still more music to come
Before you're completely
engulfed in the blissful embrace
of that little light you see
in the distance
Soon you'll be healed
forgiven and refreshed
Free from all trauma
pain guilt and shame
You may even forget your own name
But before you dwell in
that house forever
Here's thirty minutes
of easy listening
to some slow tracks
On 103.5 Dawn FM'''


def count_word(a, param):
    f = open('work.txt','w')
    f.write(a)
    f.close()
    text = a.lower()
    print(text.count(param))

count_word(a,'you')