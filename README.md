
#  Wondering what you need to wear on a hiking trip? HERE is your answer

[!NOTE] Install dependencies
```
pip install -r requirements.txt
```

[!IMPORTANT] Run this program in the terminal command line by typing in the command and pressing Enter:
```
python3 app.py
```

When you're on your way to a hike, ask yourself, "What do I need to wear? And how will I remember what I wore to tweak it next time, if I need to?" Pull this program out, grab your clothing and enter an action: "add", "delete", "update", or "quit". 

If you enter "add", you will be prompted to enter the generic name (like 'shoes', 'pants' etc) and the function of the clothing (like 'upper all-weather outer layer' for a rain jacket). Once you enter these values, a new Clothing object will be created and added to the table.

If you enter "delete", you will be prompted to enter the ID of the clothing to delete. If the clothing exists in the database, it will be deleted.

If you enter "update", you will be prompted to enter the ID of the clothing to update, and then the new function for the clothing. If the clothing exists in the database, its function will be updated.

After each action is completed, the program will return you to the main prompt and wait for your next action. If you enter any other input, the program will exit.

Want something more on the technical background? [technical description](hiking-application/technical description.md)
