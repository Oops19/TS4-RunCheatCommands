#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import ast
import copy
import os
from time import sleep
from typing import Dict

from run_cheat_commands.modinfo import ModInfo
from ts4lib.libraries.ts4folders import TS4Folders
from ts4lib.utils.singleton import Singleton
import services
import sims4
import sims4.commands
from zone import Zone
from zone_manager import ZoneManager

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommandArgument, CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)
log.enable()
log.debug(f"Starting {ModInfo.get_identity().name} v{ModInfo.get_identity().version} ")


class RunCheatCommands(object, metaclass=Singleton):
    def __init__(self):
        ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
        self.ini_file = os.path.join(ts4f.data_folder, 'commands.ini')
        self.commands_file = os.path.join(ts4f.data_folder, 'commands.txt')
        self.default_config = {
            'execute_commands': {},
            'client_cheat_commands': {},
        }
        self.config = {
            'execute_commands': {},
            'client_cheat_commands': {},
        }
        self.cheated = False
        self.output = None
        self.client_id = 1

    def read_ini(self):
        """
        Read the user supplied commands,
        :return:
        """
        config: Dict = copy.deepcopy(self.default_config)
        if os.path.exists(self.commands_file):
            try:
                with open(self.ini_file, 'rt', encoding='UTF-8') as fp:
                    data = ast.literal_eval(fp.read())
                    config = {**self.config, **data}
            except Exception as e:
                log.error(f"Error reading 'commands.ini': {e}")
        else:
            log.info(f"No config file {self.ini_file} - using default settings.")
        log.debug(f"Settings: {config}")
        self.config = config

    def read_commands(self):
        """
        Read the user supplied commands,
        :return:
        """
        if os.path.exists(self.commands_file):
            try:
                with open(self.commands_file, 'rt', encoding='UTF-8') as fp:
                    commands = fp.read()
                    log.debug(f"Commands:\n{commands}")
                    for command in commands.split("\n"):
                        command = command.split('#', 1)[0].strip()
                        if command == '':
                            continue
                        self._parse_command(command)
            except Exception as e:
                log.error(f"Error executing 'commands.txt': {e}", throw=True)
        else:
            log.info(f"Commands file {self.commands_file} not found.")

    def _parse_command(self, command: str):
        for execute_command in self.config.get('execute_commands'):
            if command.startswith(execute_command):
                self.execute_command(command)
                return
        for client_cheat_command in self.config.get('client_cheat_commands'):
            if command.startswith(client_cheat_command):
                self.client_cheat_command(command)
                return

        # Commands which are not in commands.ini:
        if self.output:
            self.execute_command(command)
            self.client_cheat_command(command)
        else:
            self.execute_command(command)
            self.client_cheat_command(command)

    def set_client_id(self, output: CommonConsoleCommandOutput = None):
        try:
            self.client_id = services.client_manager().get_first_client().id
        except:
            self.client_id = 1

    def execute_command(self, command: str):
        try:
            if self.output:
                self.output(f"execute_command: '{command}' ...")
            else:
                log.debug(f"execute_command: '{command}' ...")
            sims4.commands.execute(command, self.client_id)
            sleep(0.01)
        except Exception as e:
            log.warn(f"Error '{e}' executing '{command}'")

    def client_cheat_command(self, command: str):
        # if not self.client_id: 'Invoking client command with invalid context. ...
        if self.output:
            self.output(f"client_cheat_command: '{command}' ...")
        else:
            log.debug(f"client_cheat_command: '{command}' ...")
        sims4.commands.client_cheat(command, self.client_id)
        sleep(0.01)

    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), ZoneManager, ZoneManager.start.__name__)
    def o19_inj_zone_manager_start(original, self, *args, **kwargs):
        """
        class ZoneManager(IndexedManager):
            def start(self):
        """
        log.debug(f'o19_inj_zone_manager_start()')
        rv = original(self, *args, **kwargs)
        if RunCheatCommands().cheated is False:
            log.debug(f"Applying cheat commands ...")
            RunCheatCommands().read_ini()
            RunCheatCommands().set_client_id()
            RunCheatCommands().read_commands()
            log.debug(f"All cheats applied")
            # Not all cheats can be applied at this stage
            # RunCheatCommands().cheated = True
        return rv

    """
    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def o19_handle_event_2(event_data: S4CLZoneLateLoadEvent):
        log.debug(f'o19_handle_event_2()')
        if RunCheatCommands().cheated is False:
            log.debug(f"Applying cheat commands ...")
            RunCheatCommands().read_ini()
            RunCheatCommands().set_client_id()
            RunCheatCommands().read_commands()
            log.debug(f"All cheats applied")
            # RunCheatCommands().cheated = True

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def o19_handle_event_2(event_data: S4CLZoneEarlyLoadEvent):
        log.debug(f'o19_handle_event_1()')
        if RunCheatCommands().cheated is False:
            log.debug(f"Applying cheat commands ...")
            RunCheatCommands().read_ini()
            RunCheatCommands().set_client_id()
            RunCheatCommands().read_commands()
            log.debug(f"All cheats applied")
            # RunCheatCommands().cheated = True
    """

    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Zone, Zone.on_loading_screen_animation_finished.__name__)
    def o19_inj_zone_on_loading_screen_animation_finished(original, self, *args, **kwargs):
        """
        class Zone:
            def on_loading_screen_animation_finished(self):
        """
        log.debug(f'o19_inj_zone_on_loading_screen_animation_finished()')
        rv = original(self, *args, **kwargs)
        if RunCheatCommands().cheated is False:
            log.debug(f"Applying cheat commands ...")
            RunCheatCommands().read_ini()
            RunCheatCommands().set_client_id(None)
            RunCheatCommands().read_commands()
            log.debug(f"All cheats applied.")
            RunCheatCommands().cheated = True
        return rv

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.rcc.ini', 'Reload the INI file.')
    def o19_run_cheat_commands_txt(output: CommonConsoleCommandOutput):
        try:
            output('Loading the INI file')
            RunCheatCommands().read_ini()
            output('OK')
        except Exception as e:
            output(f"Oops: {e}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.rcc.run', 'Load and execute the cheats commands (commands.txt).')
    def o19_run_cheat_commands_txt(output: CommonConsoleCommandOutput):
        try:
            output('Loading and running all cheats.')
            RunCheatCommands().set_client_id()
            RunCheatCommands().read_commands()
            output('OK')
        except Exception as e:
            output(f"Oops: {e}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.rcc.test', "Run a single cheat command. E.g. e o19.rcc testing_cheats true. To add more than one parameter use \"\" (not '') around them.",
                          command_arguments=(
                                  CommonConsoleCommandArgument('type', 'string', "'e' or 'c' for 'execute()' or 'client_cheat()'", is_optional=False),
                                  CommonConsoleCommandArgument('command', 'string', 'The command to be run, optionally use \"\" to add 1-n parameters.', is_optional=False),
                                  CommonConsoleCommandArgument('parameter', 'string', 'The command parameter(s), if any.', is_optional=True, default_value=''),
                              )
                          )
    def o19_run_cheat_commands_test(output: CommonConsoleCommandOutput, command_type: str, command: str, parameter: str = ''):
        """
        To test whether execute() or cheat_command() should be used. If there is no output except of 'OK' this may be really tricky.
        Add the command later to commands.ini.
        """
        try:
            RunCheatCommands().set_client_id()
            if parameter:
                command = f"{command} {parameter}"
            output(f"Running '{command_type}' ({command})")
            if command_type == 'e':
                RunCheatCommands().execute_command(command)
            elif command_type == 'c':
                RunCheatCommands().client_cheat_command(command)
            else:
                output(f"Unknown type '{command_type}'. Only 'e' (execute_command) and 'c' (client_cheat_command) are supported.")
                return
            output('OK')
        except Exception as e:
            output(f"Oops: {e}")
