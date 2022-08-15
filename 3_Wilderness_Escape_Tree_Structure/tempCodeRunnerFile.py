# Take Input from the User
user_choice = input("What is your name? ")
print(user_choice)

######
# VARIABLES FOR TREE
story_piece = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""

choice_a = """

The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!
"""

choice_a_1 = """

The bear returns and tells you it's been a rough week. After making 
peace with a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""

choice_a_2 = """

The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
"""

choice_b = """

You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you
"""

choice_b_1 = """

The bear is unamused. After smelling 
the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.

"""

choice_b_2 = """

The bear understands and apologizes for startling you. Your new friend 
shows you a path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""

choice_a = TreeNode(choice_a)
choice_a_1 = TreeNode(choice_a_1)
choice_a_2 = TreeNode(choice_a_2)

choice_b = TreeNode(choice_b)
choice_b_1 = TreeNode(choice_b_1)
choice_b_2 = TreeNode(choice_b_2)



story_root = TreeNode(story_piece)
story_root.add_child(choice_a)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

story_root.add_child(choice_b)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)



######
# TESTING AREA
story_root.traverse()