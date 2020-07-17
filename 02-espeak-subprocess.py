from subprocess import call

talk = 'Olá mundo, vamos sintetizar a voz com python'

call(["espeak", talk])