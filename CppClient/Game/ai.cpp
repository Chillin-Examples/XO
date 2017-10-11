#include "ai.h"

using namespace koala::chillin::client;
using namespace ks::models;


AI::AI(World *world): TurnbasedAI<World*>(world)
{
}

void AI::decide()
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (world->board()[i][j] == ECell::Empty)
            {
                ks::commands::Place cmd;
                cmd.x(j);
                cmd.y(i);
                sendCommand(&cmd);
                return ;
            }
}
