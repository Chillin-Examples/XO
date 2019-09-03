package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class World extends KSObject
{
	protected ECell[][] board;
	
	// getters
	
	public ECell[][] getBoard()
	{
		return this.board;
	}
	
	
	// setters
	
	public void setBoard(ECell[][] board)
	{
		this.board = board;
	}
	
	
	public World()
	{
	}
	
	public static final String nameStatic = "World";
	
	@Override
	public String name() { return "World"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize board
		s.add((byte) ((board == null) ? 0 : 1));
		if (board != null)
		{
			for (int tmp0 = 0; tmp0 < 3; tmp0++)
			{
				for (int tmp1 = 0; tmp1 < 3; tmp1++)
				{
					s.add((byte) ((board[tmp0][tmp1] == null) ? 0 : 1));
					if (board[tmp0][tmp1] != null)
					{
						s.add((byte) (board[tmp0][tmp1].getValue()));
					}
				}
			}
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize board
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			board = new ECell[3][3];
			for (int tmp3 = 0; tmp3 < 3; tmp3++)
			{
				for (int tmp4 = 0; tmp4 < 3; tmp4++)
				{
					byte tmp5;
					tmp5 = s[offset];
					offset += Byte.BYTES;
					if (tmp5 == 1)
					{
						byte tmp6;
						tmp6 = s[offset];
						offset += Byte.BYTES;
						board[tmp3][tmp4] = ECell.of(tmp6);
					}
					else
						board[tmp3][tmp4] = null;
				}
			}
		}
		else
			board = null;
		
		return offset;
	}
}
