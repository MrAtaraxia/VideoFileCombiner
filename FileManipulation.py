"""
FileManipulation.py
This file (currently) combines all of the Audio/Video files with the same name in the current directory using ffmpeg.

# I LIKE my notes of what I did while making the program.
# It shows me a glimpse into what I did today when I look back at this file later.
#
"""
from os import listdir, rename, system, remove, getcwd


def replace_whitespaces_with_underscores():
    """
    Replaces the whitespaces in the current directory with underscores
    FOR LATER : make it work on other directories? Does this work? How to get 'current directory'
    Changed it to ONLY use this directory!
    :return: None
    """
    # Removes the " " from the files and replaces them with "_" so I don't need quotes!
    for f in listdir(getcwd()):
        new_f = ""
        for _ in f:
            if _ == " ":
                new_f += "_"
            else:
                new_f += _
        if f != new_f:
            rename(f, new_f)  # (old, new)


def replace_underscores_with_whitespace():
    """
    Replaces the underscores in the current directory with whitespace (undoes the pervious one)
    FOR LATER : make it work on other directories? Does this work? How to get 'current directory'
    Changed it to ONLY use this directory!
    :return: None
    """
    # Removes the "_" from the files and replaces them with " " so I don't need quotes!
    for f in listdir(getcwd()):
        new_f = ""
        for _ in f:
            if _ == "_":
                new_f += " "
            else:
                new_f += _
        if f != new_f:
            rename(f, new_f)  # (old, new)


"""
def replace_a_with_b_in_c(replace, replace_with, file_to_modify):

    # Removes the "_" from the files and replaces them with " " so I don't need quotes!
    modified_file = ""
    for _ in file_to_modify:
        if _ == replace:
            modified_file += replace_with
        else:
            modified_file += _
    if file_to_modify != modified_file:
        rename(file_to_modify, modified_file)  # (old, new)
# """


def select_which_files():
    """
    FOR LATER : make it work on other directories? Does this work? How to get 'current directory'
    decides which files have an Audio and Video file that can be converted to a combined file.
    :return: list
    """

    # [] = converts the contained things into a list.
    files_in_directory = [f for f in listdir(getcwd())]
    #  onlyfiles = [f for f in listdir() if isfile(join(mypath, f))]

    # remove the ones that have already been converted.
    # how to qualify a substring and compare.

    # DONE : How to decide which files to 'convert' and remove the files that have already been converted.
    #
    looking_for_audio = "Audio.webm"
    looking_for_audio2 = "Audio.mp3"
    looking_for_video = "Video.webm"
    looking_for_video2 = "Video.mp4"
    files_to_convert = []

    for f in files_in_directory:
        if (f[-10:] == looking_for_audio) or (f[-9:] == looking_for_audio2):
            for f2 in files_in_directory:
                if (f2[-10:] == looking_for_video) or (f2[-9:] == looking_for_video2):
                    if f2[:-10] == f[:-10]:
                        files_to_convert.append(f[:-10])

    return files_to_convert


def combine_audio_and_video(to_convert_file):
    """
    Combines the audio and video files with the same name and then deletes those files.
    :param to_convert_file: string
    :return: none
    """
    command = r'cmd /k "ffmpeg.exe -i ' + \
              to_convert_file + "Audio.webm -i " + \
              to_convert_file + "Video.webm " + \
              to_convert_file + "Combined.mp4" + '&& exit"'  # Properly exited the cmd prompt!
    # ffmpeg.exe -i "82p2v.webm" -i "82p2.webm" output.mp4
    print(command)
    system(command)
    print("Files Combined!")
    remove(to_convert_file + "Audio.webm")
    remove(to_convert_file + "Video.webm")
    print("Original Files Deleted!")


# Actual does the work of combining the files:

# DONE : look into how to make it so that this 'stops' at some point...
# DONE : Do I want to keep the 'converted files around after or delete them afterwards?
# Decided to have the delete after they were converted.
# r before for raw string so that it 'should' work for more things
# command = r'cmd /k "Your Command Prompt Command"'

"""
args = ''
args.in_filename = "in_name"
args.out_filename = "out_name"



args = parser.parse_args()
total_duration = float(ffmpeg.probe(args.in_filename)['format']['duration'])
ffmpeg.audio()
"""


def replace_a_with_b_in_c(replace, replace_with, file_to_modify):
    file_modified = file_to_modify.replace(replace, replace_with)
    if file_modified != file_to_modify:
        rename(file_to_modify, file_modified)  # (old, new)


def actual_main():
    # Future things to do:
    # if I want to change it to work in other directories I can make something off of: getcwd()
    # but that might require "" for when I want to use ffmpeg so I might avoid that until I have a better understanding
    # of the ffmpeg package so I won't have to call it through command prompt.
    # replace_whitespaces_with_underscores()
    # I AM ANNOYED I DIDN"T KNOW THIS EXISTED... ANYWAY
    #
    # OH I could do it THAT WAY.
    # Move the Audio/Video files TO the current directory.
    # rename them. # replace the " " with "_"
    # convert/combine to combined.
    # rename back. # replace the "_" with " "
    # move the Combined file TO the original directory. Or wherever I want to move them to. a Combined folder?
    #

    for f in listdir(getcwd()):
        replace_a_with_b_in_c(" ", "_", f)
    files = select_which_files()
    print(files)
    for file in files:
        combine_audio_and_video(file)
    # replace_underscores_with_whitespace() # could put that in after to have it all be self contained.


if __name__ == "__main__":
    # I would probably want to do it with argpars if I want to have it do other directories... MEH...
    print("Combining Audio and Video webm Files in: " + getcwd())
    actual_main()
    # Put in questions to ask if they want to convert certain files?
