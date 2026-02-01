# Horse Mod - Attachment Editor Patch
This patch provides the necessary modifications to enable the [Attachment Editor debug tool](https://pzwiki.net/wiki/Attachment_Editor) for the horses. The reason this is needed is because custom [AnimSets](https://pzwiki.net/wiki/AnimSet) are not possible in the game, due to an [ActionGroup](https://pzwiki.net/wiki/ActionGroup) being needed, which can't be loaded in from mods by the game.

This patch requires you to run the `setup.py` script, which will do the following:
1. Copy the latest AnimSets from the Horse Mod into a new AnimSet named `horse`. On top of that, an idle AnimNode was specifically created and only available in this mod to act as the idle animation in the editor. The files themselves are copied so you can properly test the horse mod in-game without deactivating this patch.
2. It will copy the `buck` vanilla ActionGroup into a new ActionGroup named `horse`, the one used by the horse animations.
3. It will modify the `animset` entry in the animal definition to use the new `horse` ActionGroup instead of the `buck` one in the Horse Mod.

What this achieves is that instead of using the `buck` ActionGroup for the horse animations, it will now use the newly manually installed `horse` ActionGroup, which can be recognized by the Attachment Editor tool.

See the [documentation](https://pz-horseteam.github.io/horsemod) on how to add attachments to horses.

## Installation
1. Make sure you have Python and Git installed on your system.
2. Download or clone this repository to your local machine.
3. Modify the `config.ini` file to point to your [game media folder](https://pzwiki.net/wiki/Game_files#Media_folder).
4. Run the `setup.py` script.
5. Launch the game and activate the "Horse Mod - Attachment Editor Patch" mod from the mods menu.
6. Launch a save and use the Attachment Editor tool on a horse to find the attachment points coordinates.
