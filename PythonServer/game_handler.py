# -*- coding: utf-8 -*-

# python imports
from __future__ import division

# chillin imports
from chillin_server import TurnbasedGameHandler
from chillin_server.gui import scene_actions

# project imports
from ks.models import World, ECell


class MyTurnbasedGameHandler(TurnbasedGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return

        self.last_command = (side_name, command)
        print("command: %s" % (self.last_command, ))


    def on_initialize(self):
        print("initialize")

        self.world = World()
        self.world.board = [[ECell.Empty for _ in range(3)] for _ in range(3)]

        self.last_command = (None, None)
        self.last_move = None
        self.num_filled_cells = 0


    def on_initialize_gui(self):
        print("initialize gui")

        self.CELL_SIZE = 1
        self.CELL_OFFSET = -3 / 2 * self.CELL_SIZE

        self.scene.add_action(scene_actions.ChangeCamera(
            ref = self.scene.rm.get('MainCamera'),
            clear_flag = scene_actions.ECameraClearFlag.SolidColor,
            background_color = scene_actions.Vector4(x=1, y=1, z=1, w=1),
            is_orthographic = True,
            orthographic_size = 2,
            min_position = scene_actions.Vector3(x=-2, y=-2, z=-10),
            max_position = scene_actions.Vector3(x=2, y=2, z=-10),
            min_rotation = scene_actions.Vector2(x=0, y=0),
            max_rotation = scene_actions.Vector2(x=0, y=0),
            min_zoom = 1,
            max_zoom = 3
        ))

        # Draw lines
        for i in range(1, 3):
            start = self._get_scene_position(i, 0, get_center=False)
            end = self._get_scene_position(i, 3, get_center=False)
            self._draw_line(scene_actions.Vector4(x=0, y=0, z=0), (start['x'], start['y']), (end['x'], end['y']))
            self._draw_line(scene_actions.Vector4(x=0, y=0, z=0), (start['y'], start['x']), (end['y'], end['x']))

        self.scene.add_action(scene_actions.EndCycle())
        self.scene.apply_actions()


    def on_process_cycle(self):
        print("process: %s %s" % (self.current_cycle, self.turn_allowed_sides))

        side_name, command = self.last_command
        self.last_command = (None, None)

        if command and self.world.board[command.y][command.x] == ECell.Empty:
            self.num_filled_cells += 1
            self.world.board[command.y][command.x] = ECell.X if side_name == 'X' else ECell.O
            self.last_move = {
                'x': command.x,
                'y': command.y,
                'side': side_name
            }

            # check end-game
            for i in range(3):
                if self.world.board[i][0] != ECell.Empty and self.world.board[i][0] == self.world.board[i][1] == self.world.board[i][2]:
                    self.end_game(side_name)
                    return
                if self.world.board[0][i] != ECell.Empty and self.world.board[0][i] == self.world.board[1][i] == self.world.board[2][i]:
                    self.end_game(side_name)
                    return

            if self.world.board[0][0] != ECell.Empty and self.world.board[0][0] == self.world.board[1][1] == self.world.board[2][2]:
                self.end_game(side_name)
                return

            if self.world.board[0][2] != ECell.Empty and self.world.board[0][2] == self.world.board[1][1] == self.world.board[2][0]:
                self.end_game(side_name)
                return

            if self.num_filled_cells == 9:
                self.end_game()


    def on_update_clients(self):
        print("update clients")
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print("update gui")

        if self.last_move:
            if self.last_move['side'] == 'O':
                self._draw_O(self.last_move['x'], self.last_move['y'])
            elif self.last_move['side'] == 'X':
                self._draw_X(self.last_move['x'], self.last_move['y'])

        self.last_move = None

        self.scene.add_action(scene_actions.EndCycle())
        self.scene.apply_actions()


    def _draw_O(self, x, y):
        scene_pos = self._get_scene_position(x, y)

        ref = self.scene.rm.new()
        self.scene.add_action(scene_actions.CreateBasicObject(
            ref = ref,
            type = scene_actions.EBasicObjectType.Ellipse2D,
        ))
        self.scene.add_action(scene_actions.ChangeTransform(
            ref = ref,
            position = scene_actions.Vector3(x=scene_pos['x'], y=scene_pos['y']),
        ))
        self.scene.add_action(scene_actions.ChangeEllipse2D(
            ref = ref,
            duration_cycles = 1,
            fill_color = scene_actions.Vector4(x=1, y=0, z=0, w=1),
            x_radius = 0.3,
            y_radius = 0.3,
        ))


    def _draw_X(self, x, y):
        scene_pos = self._get_scene_position(x, y)
        self._draw_line(scene_actions.Vector4(x=0, y=0, z=1), (scene_pos['x'] - 0.3, scene_pos['y'] + 0.3), (scene_pos['x'] + 0.3, scene_pos['y'] - 0.3))
        self._draw_line(scene_actions.Vector4(x=0, y=0, z=1), (scene_pos['x'] - 0.3, scene_pos['y'] - 0.3), (scene_pos['x'] + 0.3, scene_pos['y'] + 0.3))


    def _draw_line(self, color, start, end):
        line_ref = self.scene.rm.new()
        self.scene.add_action(scene_actions.CreateBasicObject(
            ref = line_ref,
            type = scene_actions.EBasicObjectType.Line,
        ))
        self.scene.add_action(scene_actions.ChangeLine(
            ref = line_ref,
            fill_color = color,
            vertices = [scene_actions.Vector2(x=start[0], y=start[1]), scene_actions.Vector2(x=end[0], y=end[1])],
            width = 0.1,
            end_cap_vertices = 90,
            duration_cycles = 1,
        ))


    def _get_scene_position(self, x, y, get_center=True):
        addition = self.CELL_SIZE / 2 if get_center else 0

        return {
            'x': x * self.CELL_SIZE + self.CELL_OFFSET + addition,
            'y': -(y * self.CELL_SIZE + self.CELL_OFFSET + addition)
        }


GameHandler = MyTurnbasedGameHandler
