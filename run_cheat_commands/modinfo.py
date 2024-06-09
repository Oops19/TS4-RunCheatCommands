#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    """ Mod info. """
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'RunCheatCommands'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'run_cheat_commands'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.0.6-1'


r'''
TODO v2.x
    Support sim_id / sim_name within scripts
v1.0.6-1
    No code changes in the mod. No need to update when using v1.0.6
    NEW: The default config (The Sims 4/mod_data/run_cheat_commands/commands.txt) is now unlocking all 'locked' CAS items including EP12 (High School Years).
    Misc:
        Compile script updated
        The compile and version info is added to 'The Sims 4/mod_documentation/run_cheat_commands/version.txt'
v1.0.6
    Tested with TS4 v1.107
    Cheats will be applied on every zone-load as TS4 seems to reset some cheats.
v1.0.5
    Update README for new TS4 version.
v1.0.4
    Add more execute and client_cheat commands
v1.0.3
    Fix uncaught exception
v1.0.2
    Support for thesims4tools
v1.0.1
    Make MTS links no longer click-able
v1.0.0
    Tested version
v0.0.1
    Initial version
'''