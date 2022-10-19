from moviepy.editor import *

def add_text(text):
    clip = VideoFileClip("clip.mp4")
    char_length = 19
    char_height = 25
    left_right_margins = 130
    top_bottom_margins = 30
    print("Clip size: " + str(clip.size))

    def calculate_width():
        chars_in_line = round( ( clip.w - left_right_margins ) / char_length )
        print("chars in line: " + str( chars_in_line))
        # Cate caractere incap intr-un rand
        # am lungimea totala clip.w - 130
        # am lungimea unui caracter: char_length
        if len(text) < chars_in_line:
            print("single line")
            return ( 1 + len(text) ) * char_length, text
        else:
            t = text[:chars_in_line] + '\n' + text[chars_in_line:]
            #lines = round(1 + len(text) / chars_in_line)
            return clip.w - left_right_margins, t
        
        


    def calculate_height():
        lines = len(text.split('\n'))
        print("lines: " + str(lines))
        return char_height * lines + top_bottom_margins, text

    w, text = calculate_width()
    h, t = calculate_height()
    text_clip = (TextClip(t.upper(), font="NimbusSans-Bold", fontsize = 24, size=(w,h), color='white', stroke_width=10, bg_color='#81A840', kerning=2)
                    .margin(top=15, bottom=15, left=15, right=15, opacity=0)
                    .set_position(("center", "bottom")))
                    #.set_position((10, 10)))


    screensize = (clip.w, clip.h)
    both = ( CompositeVideoClip([clip,text_clip], size=screensize).fadein(1).set_duration(10))
    both.write_videofile("clip-with-text.mp4", fps=clip.fps)

add_text("aaaaabbbbbcccccdddddeeeeefffffggggg")
#add_text("aaaaabbbbb")
