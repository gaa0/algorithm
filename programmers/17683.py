import datetime


def solution(m, musicinfos):
    answer = ''
    max_playtime = 0
    replace_list = [('C#', '2'),
                    ('D#', '4'),
                    ('F#', '7'),
                    ('G#', '9'),
                    ('A#', 'a'),
                    ('C', '1'),
                    ('D', '3'),
                    ('E', '5'),
                    ('F', '6'),
                    ('G', '8'),
                    ('A', '0'),
                    ('B', 'b')]
    for k, v in replace_list:
        m = m.replace(k, v)
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        start = datetime.datetime.strptime(start, '%H:%M')
        end = datetime.datetime.strptime(end, '%H:%M')
        playtime = (end - start).seconds // 60
        for k, v in replace_list:
            music = music.replace(k, v)

        if playtime <= len(music):
            music = music[:playtime]
        else:
            music = music * (playtime // len(music)) + music[:(playtime % len(music))]

        if m in music and playtime > max_playtime:
            answer = title
            max_playtime = playtime

        if answer == '':
            answer = '(None)'

    return answer


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
