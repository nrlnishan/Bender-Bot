#!/usr/bin/env python

import os

BOT_COMMAND = "bender"

BOT_OPTION_NEW = "new"
BOT_OPTION_SAVE = "save"
BOT_OPTION_DISCARD = "discard"
BOT_OPTION_LIST = "list"
BOT_OPTION_EXIT = "exit"
BOT_OPTION_HELP = "help"

BOT_ATTR_TAGS = "--tags"

BOT_UNICODE = u"\U0001F916"

file_list = []
user_contents = ""
is_content_mode = False

available_robots_message = "Hi there! Currently we only have 'Bender' available as your personal Robot.He is the lazy one. Just type 'Bender' or 'bender' to call him. \n"


def main():
	configure()
	init_bot()


def configure():

	save_folder_name = "bot savefiles"
	cur_dir = os.path.abspath(os.path.dirname(__file__))
	save_file_path = os.path.join(cur_dir,save_folder_name)

	# Creating folder for save files if not present
	if not os.path.isdir(save_file_path):
		os.makedirs(save_folder_name)
		os.chdir(save_file_path)
	else:
		# Listing all the save files name present in save folder
		os.chdir(save_file_path)

		global file_list
		file_list = [f for f in os.listdir(save_file_path) if os.path.isfile(os.path.join(save_file_path,f))]


def init_bot():

	prompt = "> "
	global user_contents

	print_welcome_message()

	while True:

		user_input = input(prompt)

		if is_content_mode:
			# Incase the line starts with Save or Discard command
			if user_input.lower().startswith(BOT_COMMAND):

				user_input_arr = user_input.strip().lower().split()
				parse_result = parse_commands(user_input_arr)
				
				# If the command is invalid in content mode, it is regarded as content
				if parse_result == -1:
					user_contents += user_input + "\n"
				elif parse_result == 0:
					print_exit_message
					break

			# The user is still in content mode
			else:
				user_contents += user_input + "\n"
		else:
			# If this is not content_mode & first command it bot command
			user_input_arr = user_input.strip().lower().split()

			try:

				if user_input_arr[0] == BOT_COMMAND:
				
					parse_result = parse_commands(user_input_arr)
				
					# Exit Condition
					if parse_result == 0:
						print_exit_message()
						break

					# Invalid command condition
					elif parse_result == -1:
						invalid_command_msg = "{} Ain't doing that. Bite my shiny metal a$$. \n".format(BOT_UNICODE)
						print(invalid_command_msg)
				else:
					print(available_robots_message)
			except:
				print(available_robots_message)


def parse_commands(options_arr):

	global is_content_mode
	global user_contents

	"""
	-1: Invalid commands
	 0: Exit
	 1: Success commands
	"""

	try:

		if options_arr[1] == BOT_OPTION_NEW:

			message = "{} Start writing anything. After you have finished, execute save command in new line. \n".format(BOT_UNICODE)
			print(message)

			is_content_mode = True
			user_contents = ""
			return 1

		elif options_arr[1] == BOT_OPTION_EXIT:
			is_content_mode = False
			user_contents = ""
			return 0

		elif options_arr[1] == BOT_OPTION_DISCARD:

			message = "{} Discarding written content \n".format(BOT_UNICODE)
			print(message)

			is_content_mode = False
			user_contents = ""
			return 1

		elif options_arr[1] == BOT_OPTION_SAVE:

			try:

				attr = options_arr[2]

				is_valid = validate_tag(attr)

				if is_valid:

					actual_tag_name = attr[1:]

					tag_exists = check_if_tags_exists(actual_tag_name)
					file_name = actual_tag_name + ".txt"

					if tag_exists:
						f = open(file_name,"a+")
						f.write("\n")
					else:
						f = open(file_name,"w+")

					f.write(user_contents)
					f.flush()
					f.close()

					if not tag_exists:
						global file_list
						file_list.append(file_name)

					is_content_mode = False
					user_contents = ""

					print("{} Saved {}! Bender rocks! \n".format(BOT_UNICODE,attr))

				else:

					print("{} Give me hashtag baby!! \n".format(BOT_UNICODE))

				is_content_mode = False

			except:

				print("{} Need hashtags too baby!!! \n".format(BOT_UNICODE))

		elif options_arr[1] == BOT_OPTION_LIST:

			try:
				attr = options_arr[2]

				if attr == BOT_ATTR_TAGS:
					print_saved_tags("")
				else:
					attr = attr[1:]

					tag_exists = check_if_tags_exists(attr)

					if tag_exists:
						file_name = attr + ".txt"
						file = open(file_name,"r")
						file_contents = file.read()
						print(file_contents)
						file.close()

					else:

						print("{} I did my best, but couldn't find anything for #{} \n".format(BOT_UNICODE,attr))
			except:

				print("{} List what? \n".format(BOT_UNICODE))
			
		elif options_arr[1] == BOT_OPTION_HELP:
			print_bot_help_message()

		else:
			return -1

	except IndexError:

		# If no command is provided
		print("{} I'm here baby! What do you want? \n".format(BOT_UNICODE))


def validate_tag(tag):
	""" Chceks if tag is valid. Tag should not be empty and should start with '#' character """

	tag = tag.strip().lower()
	return len(tag) > 1 and tag.startswith("#")


def print_bot_help_message():

	print ("""
----------------------------------------------------------------------
{} Shut up and get to the point

[new]: 
- Create new content
- Usage: bender new

[save] [Argument]:
- Saves or Appends what you write for given #hashtag as an argument
- Usage: bender save #mytodos

[list] [Argument]:
- List all the saved items 

Argument:
	1. --tags: List all the available tags which you have saved
	2. [#hashtag]: List the contents for given hashtag

	Usage:
	bender list --tags, bender list #mytodos

[exit]: 
- Exit out of script
Usage: bender exit
----------------------------------------------------------------------
""".format(BOT_UNICODE))

def check_if_tags_exists(tag):

	for item in file_list:
		filename = item[0:-4]
		if tag == filename:
			return True
	return False


def print_saved_tags(tag_to_match):

	counter = 0

	if tag_to_match:

		for item in file_list:
			tag = item[0:-4]

			if tag == tag_to_match:
				counter += 1

				print("#{}".format(tag))
	else:

		for item in file_list:

			print("#{}".format(item[0:-4]))
			counter += 1

	print("\n{} tags found \n".format(counter))


# Welcome message to be displayed when the script starts
def print_welcome_message():

	print ("""
### WELCOME TO PLANET EXPRESS ###

Hi! I am Professor Farnsworth.

Here at Planet Express, we are currently focused in saving whatever comes to your mind. Have some to-do's or some fancy ideas? Tell Robot to remember it for you.

We have 'Bender' as your personal Robot. Type 'Bender' or 'bender' to call him.
""")

def print_exit_message():

	exit_message = "{} Bender needs beer. Bye ya'll. \n".format(BOT_UNICODE)
	print(exit_message)



# Start point for the script
if __name__ == '__main__':
	main()
