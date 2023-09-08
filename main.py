import subprocess
char_to_emoji = {
    'a': ':regional_indicator_a:',
    'b': ':regional_indicator_b:',
    'c': ':regional_indicator_c:',
    'd': ':regional_indicator_d:',
    'e': ':regional_indicator_e:',
    'f': ':regional_indicator_f:',
    'g': ':regional_indicator_g:',
    'h': ':regional_indicator_h:',
    'i': ':regional_indicator_i:',
    'j': ':regional_indicator_j:',
    'k': ':regional_indicator_k:',
    'l': ':regional_indicator_l:',
    'm': ':regional_indicator_m:',
    'n': ':regional_indicator_n:',
    'o': ':regional_indicator_o:',
    'p': ':regional_indicator_p:',
    'q': ':regional_indicator_q:',
    'r': ':regional_indicator_r:',
    's': ':regional_indicator_s:',
    't': ':regional_indicator_t:',
    'u': ':regional_indicator_u:',
    'v': ':regional_indicator_v:',
    'w': ':regional_indicator_w:',
    'x': ':regional_indicator_x:',
    'y': ':regional_indicator_y:',
    'z': ':regional_indicator_z:',
}
def ironmaceHatesMe(text):
    text = text.lower()  # Convert text to lowercase
    lines = text.split('|')  # Split text into lines at '|' characters
    transformed_lines = []

    for line in lines:
        transformed_text = []
        for char in line:
            if char in char_to_emoji:
                transformed_text.append(char_to_emoji[char])
            else:
                transformed_text.append(char)  # Keep non-alphabetical characters as-is
        transformed_lines.append(''.join(transformed_text))

    return '\n'.join(transformed_lines) 
if __name__ == '__main__':
    out = ironmaceHatesMe(input('Text: '))
    subprocess.run('clip', input=out.encode('utf-8'), check=True)
