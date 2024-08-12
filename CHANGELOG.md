# Misonic Project Internal Development Build 6

## Attention

This build is not intended for submission, but rather for the developers to keep track of development while working on the game.

## Changes

- Some code has been restructured.
- That means a fix for the player logic had to be made.
- The players can move again.
- The dynamic rules are in development.
    - The house and hotel prices are now variables which can be changed.
    - The events "Shop closure", "Housing crisis" and "Housing abundance" have been prepared.
    - The events "Birthday" and "Come out of jail" have been prepared.
- The rule card is in preparation.

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
