# Dynopoly Internal Development Build 8

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- The events are now shown in a separate card.
  - The button has been repositioned and renamed to "OK".
  - The line issues have been fixed
  - The rule algo file no longer imports the offer module.
- "Misonic Project" is now called "Dynopoly".
- In the side bar, the label "Misonic Project" now shows "Current Player Info" instead.
- The window title is now "Dynopoly".
- Player now has 3 conditions to getting out of jail:
  - roll doubles
  - pay fine
  - get a lucky roll
- You can now buy a house and a hotel.
- Paying rent no longer crashes the game.
- The bar field has been added.
  - It takes the balance away and makes you drunk for a few turns.
- The player could now get drunk.
  - ~~In that case, there is a chance the player might buy a property even if you said no.~~ removed
  - Or they could pay rent to another player even though they own the property.
  - Or they move to the wrong field.
- On the player info, you can see how drunk the current player is.
- A bug where the game crashed when you're drunk and the owner of the field is non-existant has been fixed.
- Price and rent are now listed on the offers.
- Income taxes got fixed.
- Bankruptcy introduced.
- Investments bought are assigned to the player
- Game loop bug fixed when player lands on their own property
- There is an effort in fixing "drunk rent crashes".
- The game would now check for *some* winning conditions.
- The winning conditions are random.
- The property damage event has been fixed.
- The "Pass field without spending money" condition is stricter.
- There are efforts in adding trade dialogs.
- The code could be shrunk a little.
- The trade dialogs are working now.
  - You'd have to give consent now.
- The icon by Tech-FZ has been included.
- The successful trade is now a possible winning condition.
- The readme has another introduction sentence.
- The gitignore has been updated to exclude PyInstaller-made folders and files.
- There is now doc for PyInstaller.
- A section for running the game has been added.
- The documentation now describes the nano procedure.
- The GPL license has been added.
    
## Known issues

- The rules aren't shown yet.
- Birthdays crash the game, so they won't be initiated.
- People won't be put to jail when they don't land on "Go to jail". This is because the event can't be randomised.
- go to jail now crashes the game due to changes in the player.mo_to method (will be fixed: Makala)
- changes to button class may cause issues (might need to create an inheritance class for seperate buttons)
- investment fields are not changing names on purchase even though ownership changes
  ~~ - infinite glitch occurs when player lands on their own investment. ~~ Fixed
- Some winning conditions haven't been implemented yet.
- ~~Passing Start without spending money is easier than it should be.~~ Fixed by Tech-FZ
- ~~Trading doesn't work.~~ ~~If your opponent wants to buy the house, you automatically give consent.~~ ~~When you give consent and sell an investment, the game crashes.~~ Fixed by Tech-FZ

## Potential improvements:

- placing game mechanics into a class to be easier to generate during game states such as trading and rolling
- Sometimes, being drunk causes the game to crash.

# Misonic Project Internal Development Build 7

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- added display card to aask player if they want to buy the property in question
- changed button class to accept keyword arguments for passed functions
- The event selector has been prepared and in use.
- The free parking variable is in rule_algo.
- The rule UI is becoming useful.

  - Events are printed in the terminal.
  - Events can now be shown... in only one line.

- The free parking money could now be retrieved.
  - Income tax has been fixed.

## Known issues

- The rules aren't shown yet.
- Birthdays crash the game, so they won't be initiated.
- People won't be put to jail when they don't land on "Go to jail". This is because the event can't be randomised.
- ~~The events aren't shown in the game itself **as intended**.~~ (Partially) fixed by Tech-FZ
- ~~Houses in investments can be damaged.~~ Fixed by Tech-FZ
- Houses and hotels can change and stay at their price at the same time! (Same with free parking)
- ~~Houses and hotels can change and stay at their price at the same time!~~ Fixed by Tech-FZ
- go to jail now crashes the game due to changes in the player.mo_to method (will be fixed: Makala)
- changes to button class may cause issues (might need to create an inheritance class for seperate buttons)
- pay rent function not working as intended and freezes game

# Misonic Project Internal Development Build 6

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- Some code has been restructured.
- That means a fix for the player logic had to be made.
- The rule UI file is now the sidebar file in `universal`.
- The players can move again.
- The ownership issues have been fixed.
- The investment issues have been fixed.
- The dynamic rules are in development.
  - The house and hotel prices are now variables which can be changed.
  - The events "Shop closure", "Housing crisis" and "Housing abundance" have been prepared.
  - The events "Birthday" and "Come out of jail" have been prepared.
  - The jailbreak event is now random. You don't have 100 % luck anymore.
  - The jail event is there.
- The rule card is in preparation.
- If you get to jail, you should have to have luck going out without doing anything (but your chances are 100 % right now because the jailbreak function is yet to be updated).
- An empty else-clause for those who stay in jail has been added.
- The rules are now displayed again, even if a player is there.

## Known issues

- ~~The players aren't moving at all.~~ Fixed by MakalaMabotja

# Misonic Project Internal Development Build 5

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- The jail has been re-implemented.
- Investments are now on the board.
- Streets can now be bought.
- Streets should now be treated properly.
- Investments should now work.
- "Roll dice" spamming will now be handled with a "Slow down, please!" on the terminal. Also, the spamming issue has been fixed completely.
- The dicing system is more dynamic now.
- The second player is being shown.
- The second player works as a computer.
- The after-turn steps have been moved to a separate function to make automation of the computer easier.
- Added new movement mechinism to avoid rolling outside of the list of available fields
- Added bounce movement for player token movement
- Street ownership intialized to bank
- Bank defined a player to treat ownership the same across the board
- Go to jail now has mechanism for sending player to jail
- Handled redrawing of both player when one player is moving
- Change of ownership for streets need to be correct coded
- fixed typo error in gotojail mechanism
- added $200 to player balance on passing start field
- "free" spaces need to be fixed to avoid added balance to non-existing owner

## Known issues

- ~~Spamming "Roll dice" can cause the game to crash with an IndexError.~~ Fixed by Nicolas and Mizuki

# Misonic Project Internal Development Build 4

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- The buttons and dices are now defined outside of the loop.
- The rule UI on the right has changed its background colour to grey.
- The movement is basically working.
- An unnecessary comma has been removed from the button script.
- Changes to the field container have been conducted to make fixing the game easier.
- Git will now ignore pycache.
- The player card UI has been added to the right.
- The field placement had to be re-added.
- The still faulty movement had to be fixed as well.
- The player movement is behaving properly now.
- The win condition thing has been added.

## Known issues

- ~~The button doesn't work yet.~~ Resolved by Nicolas

# Misonic Project Internal Development Build 3

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- The dice is in preparation.
- The dice could be rolled (no initiator yet).
- A button class in in the works.
- The button class is close to being ready.
- A button for rolling the dice is displayed in the game.

## Known issues

- The button doesn't work yet.

# Misonic Project Internal Development Build 2

- The player has been prepared.
- The field generator has been rewritten.
- A transactions file has been prepared.
- Makala Mabotja has been credited for the idea and the code.
- The player logic has been extended.
- A circular import has been removed.

# Misonic Project Internal Development Build 1

- A basic Pygame code from the Pygame documentation has been copied over as a base.
- The contributors file has been made.
- Some probably required files have been created and the ui for rules and so on has been prepared
- A dev env setup guide is in the works.
- A minor issue has been corrected within that dev env setup guide.
- The dev env setup guide is fairly finished (for) now.
- The first text is being displayed.
- The field function is sort of there.
- The game layout has been prepared and should no longer require major changes.
