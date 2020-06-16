import sys

def print_hanged_man(turns,out=sys.stdout):
	if turns == 9:
		out.write("9 turns left\n")
		out.write("  --------  \n")
	if turns == 8:
		out.write("8 turns left\n")
		out.write("  --------  \n")
		out.write("     O      \n")
	if turns == 7:
		out.write("7 turns left\n")
		out.write("  --------  \n")
		out.write("     O      \n")
		out.write("     |      \n")
	if turns == 6:
		out.write("6 turns left\n")
		out.write("  --------  \n")
		out.write("     O      \n")
		out.write("     |      \n")
		out.write("    /       \n")
	if turns == 5:
		out.write("5 turns left\n")
		out.write("  --------  \n")
		out.write("     O      \n")
		out.write("     |      \n")
		out.write("    / \     \n")
	if turns == 4:
		out.write("4 turns left\n")
		out.write("  --------  \n")
		out.write("   \ O      \n")
		out.write("     |      \n")
		out.write("    / \     \n")
	if turns == 3:
		out.write("3 turns left\n")
		out.write("  --------  \n")
		out.write("   \ O /    \n")
		out.write("     |      \n")
		out.write("    / \     \n")
	if turns == 2:
		out.write("2 turns left\n")
		out.write("  --------  \n")
		out.write("   \ O /|   \n")
		out.write("     |      \n")
		out.write("    / \     \n")
	if turns == 1:
		out.write("1 turn left\n")
		out.write("Last breaths counting, Take care!\n")
		out.write("  --------  \n")
		out.write("   \ O_|/   \n")
		out.write("     |      \n")
		out.write("    / \     \n")
	if turns == 0:
		out.write("You loose!\n")
		out.write("You let a kind man die\n")
		out.write("  --------  \n")
		out.write("     O_|    \n")
		out.write("    /|\      \n")
		out.write("    / \     \n")
		return True
	return False
