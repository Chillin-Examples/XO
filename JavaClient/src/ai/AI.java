package ai;

import team.koala.chillin.client.TurnbasedAI;
import ks.KSObject;
import ks.models.*;
import ks.commands.*;


public class AI extends TurnbasedAI<World, KSObject> {
	
	public AI(World world) {
		super(world);
	}

	@Override
	public void decide() {
		for(int i = 0; i < world.getBoard().length; i++)
			for(int j = 0; j < world.getBoard()[0].length; j++)
				if (world.getBoard()[i][j] == ECell.Empty) {
					final int placeX = j;
					final int placeY = i;
					this.sendCommand(new Place() {{ x = placeX; y = placeY; }});
					return;
				}
	}
}
