#ifndef _KS_COMMANDS_H_
#define _KS_COMMANDS_H_

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


namespace commands
{

class Place : public KSObject
{

protected:

	unsigned int __x;
	unsigned int __y;

	bool __has_x;
	bool __has_y;


public: // getters

	inline unsigned int x() const
	{
		return __x;
	}
	
	inline unsigned int y() const
	{
		return __y;
	}
	

public: // reference getters

	inline unsigned int &ref_x() const
	{
		return (unsigned int&) __x;
	}
	
	inline unsigned int &ref_y() const
	{
		return (unsigned int&) __y;
	}
	

public: // setters

	inline void x(const unsigned int &x)
	{
		__x = x;
		has_x(true);
	}
	
	inline void y(const unsigned int &y)
	{
		__y = y;
		has_y(true);
	}
	

public: // has_attribute getters

	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
	}
	

public: // has_attribute setters

	inline void has_x(const bool &has_x)
	{
		__has_x = has_x;
	}
	
	inline void has_y(const bool &has_y)
	{
		__has_y = has_y;
	}
	

public:

	Place()
	{
		has_x(false);
		has_y(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Place";
	}
	
	virtual inline const std::string name() const
	{
		return "Place";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			unsigned int tmp1 = __x;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(unsigned int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			unsigned int tmp4 = __y;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(unsigned int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize x
		__has_x = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_x)
		{
			__x = *((unsigned int*) (&s[offset]));
			offset += sizeof(unsigned int);
		}
		
		// deserialize y
		__has_y = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_y)
		{
			__y = *((unsigned int*) (&s[offset]));
			offset += sizeof(unsigned int);
		}
		
		return offset;
	}
};

} // namespace commands

} // namespace ks

#endif // _KS_COMMANDS_H_
