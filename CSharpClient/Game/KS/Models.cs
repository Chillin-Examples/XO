using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Models
{
	public enum ECell
	{
		Empty = 0,
		X = 1,
		O = 2,
	}
	
	public partial class World : KSObject
	{
		public ECell?[,] Board { get; set; }
		

		public World()
		{
		}
		
		public new const string NameStatic = "World";
		
		public override string Name() => "World";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Board
			s.Add((byte)((Board == null) ? 0 : 1));
			if (Board != null)
			{
				for (uint tmp0 = 0; tmp0 < 3; tmp0++)
				{
					for (uint tmp1 = 0; tmp1 < 3; tmp1++)
					{
						s.Add((byte)((Board[tmp0, tmp1] == null) ? 0 : 1));
						if (Board[tmp0, tmp1] != null)
						{
							s.Add((byte)((byte)Board[tmp0, tmp1]));
						}
					}
				}
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Board
			byte tmp2;
			tmp2 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp2 == 1)
			{
				Board = new ECell?[3, 3];
				for (uint tmp3 = 0; tmp3 < 3; tmp3++)
				{
					for (uint tmp4 = 0; tmp4 < 3; tmp4++)
					{
						byte tmp5;
						tmp5 = (byte)s[(int)offset];
						offset += sizeof(byte);
						if (tmp5 == 1)
						{
							byte tmp6;
							tmp6 = (byte)s[(int)offset];
							offset += sizeof(byte);
							Board[tmp3, tmp4] = (ECell)tmp6;
						}
						else
							Board[tmp3, tmp4] = null;
					}
				}
			}
			else
				Board = null;
			
			return offset;
		}
	}
} // namespace KS.Models
