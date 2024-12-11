# Run Cheat Commands

This mod runs cheat commands when starting TS4. Add them to a simple text file:
* testingcheats true  # Enable cheat commands
* death.toggle false  # Disable death
* ...


## Usage
Add or remove the commands from 'commands.txt'. 
* To disable a line make sure it starts with '#'.
* To enable a line remove the '#' at the beginning.

For 'toggle' commands always a 2nd parameter 'true/false' or 'on/off' should be supplied.

## commands.txt
The config file '/mod_data/run_cheat_commands/commands.txt' contains all commands with parameters which will be executed.

## commands.ini
The '/mod_data/run_cheat_commands/commands.ini' file defines how to execute the commands as TS4 has two flavors.

## Internals
The commands.txt file will be read and executed two times.
* First time when the 'Loading Screen' appears - there not all cheats work.
* Second time after the household is loaded, there all supported cheats should work
* Commands which are not in 'commands.ini' will be executed for both flavors and one will run fine.

## Cheat commands of other mods
Command line cheat commands are fully supported. 
To print the outfit of the current sim add `s4clib.print_outfit` to 'commands.txt'

## Limitations
* Pie menu cheats are not supported.
* Getting and using a sim_id is not supported. Even though `sims.get_sim_id_by_name "first names" "last names"` should work the result can't be accessed.

## Future / Ideas
Make the sim_id available and allow to loop over multiple sim_ids (e.g. complete 'Goth' family)


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.111.102, S4CL 3.9, TS4Lib 0.3.33.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
