using System;

using KoalaTeam.Chillin.Client;
using KS;
using KS.Commands;
using KS.Models;

using KSObject = KS.KSObject;

namespace Game
{
	public class AI : TurnbasedAI<World, KSObject>
	{
		public AI(World world) : base(world)
		{
		}

		public override void Decide()
		{
			for (int i = 0; i < World.Board.GetLength(0); i++)
				for (int j = 0; j < World.Board.GetLength(1); j++)
					if (World.Board[i, j] == ECell.Empty)
					{
						this.SendCommand(new Place() { X = (uint?)j, Y = (uint?)i });
						return;
					}
		}
	}
}
