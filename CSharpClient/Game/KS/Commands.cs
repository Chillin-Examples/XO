using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Commands
{
	public partial class Place : KSObject
	{
		public uint? X { get; set; }
		public uint? Y { get; set; }
		

		public Place()
		{
		}
		
		public new const string NameStatic = "Place";
		
		public override string Name() => "Place";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize X
			s.Add((byte)((X == null) ? 0 : 1));
			if (X != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)X));
			}
			
			// serialize Y
			s.Add((byte)((Y == null) ? 0 : 1));
			if (Y != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)Y));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize X
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				X = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				X = null;
			
			// deserialize Y
			byte tmp1;
			tmp1 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp1 == 1)
			{
				Y = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				Y = null;
			
			return offset;
		}
	}
} // namespace KS.Commands
