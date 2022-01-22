# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

letter_body = None
names = None
with open('./Input/Letters/starting_letter.txt', mode='r') as f:
    letter_body = f.readlines()

with open("./Input/Names/invited_names.txt", mode="r") as f:
    names = f.readlines()

Mails = []

for name in names:
    if name == "" or name == '\n' or name == " ":
        continue
    name = list(name)
    if name[-1] == '\n':
        name.pop()
    name = ''.join(name)
    body = ''.join(letter_body)
    body = body.replace('[name]', str(name))

    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as f:
        f.write(body)
