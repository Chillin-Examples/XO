#ifndef _KS_MODELS_H_
#define _KS_MODELS_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace models
{

enum class ECell
{
	Empty = 0,
	X = 1,
	O = 2,
};


class World : public KSObject
{

protected:

	std::array<std::array<ECell, 3>, 3> __board;

	bool __has_board;


public: // getters

	inline std::array<std::array<ECell, 3>, 3> board() const
	{
		return __board;
	}
	

public: // reference getters

	inline std::array<std::array<ECell, 3>, 3> &ref_board() const
	{
		return (std::array<std::array<ECell, 3>, 3>&) __board;
	}
	

public: // setters

	inline void board(const std::array<std::array<ECell, 3>, 3> &board)
	{
		__board = board;
		has_board(true);
	}
	

public: // has_attribute getters

	inline bool has_board() const
	{
		return __has_board;
	}
	

public: // has_attribute setters

	inline void has_board(const bool &has_board)
	{
		__has_board = has_board;
	}
	

public:

	World()
	{
		has_board(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "World";
	}
	
	virtual inline const std::string name() const
	{
		return "World";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			for (unsigned int tmp0 = 0; tmp0 < 3; tmp0++)
			{
				for (unsigned int tmp1 = 0; tmp1 < 3; tmp1++)
				{
					s += '\x01';
					unsigned char tmp3 = (unsigned char) __board[tmp0][tmp1];
					auto tmp4 = reinterpret_cast<char*>(&tmp3);
					s += std::string(tmp4, sizeof(unsigned char));
				}
			}
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize board
		__has_board = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_board)
		{
			for (unsigned int tmp5 = 0; tmp5 < 3; tmp5++)
			{
				for (unsigned int tmp6 = 0; tmp6 < 3; tmp6++)
				{
					offset++;
					unsigned char tmp7;
					tmp7 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					__board[tmp5][tmp6] = (ECell) tmp7;
				}
			}
		}
		
		return offset;
	}
};

} // namespace models

} // namespace ks

#endif // _KS_MODELS_H_
