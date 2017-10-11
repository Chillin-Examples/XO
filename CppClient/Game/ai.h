#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::TurnbasedAI<ks::models::World*>
{
public:
    AI(ks::models::World *world);

    void decide();
};

#endif // AI_H
