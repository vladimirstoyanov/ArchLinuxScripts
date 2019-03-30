#ifndef JSONOBJECT_H
#define JSONOBJECT_H

#include "jsonvalue.h"
#include <string>
//#include <QtCore/qiterator.h>
//#ifdef Q_COMPILER_INITIALIZER_LISTS
//#include <QtCore/qpair.h>
//#include <initializer_list>
//#endif

class  JsonObject
{
public:
    JsonObject();

    ~JsonObject();

    JsonObject(const JsonObject &other);
    JsonObject &operator =(const JsonObject &other);

    JsonObject(JsonObject &&other)
        : d(other.d), o(other.o)
    {
        other.d = nullptr;
        other.o = nullptr;
    }

    JsonObject &operator =(JsonObject &&other)
    {
        swap(other);
        return *this;
    }

    void swap(JsonObject &other)
    {
        std::swap(d, other.d);
        std::swap(o, other.o);
    }


    std::vector<std::string> keys() const;
    int size() const;
    inline int count() const { return size(); }
    inline int length() const { return size(); }
    bool isEmpty() const;

    JsonValue value(const std::string &key) const;
    JsonValue operator[] (const std::string &key) const;
    JsonValueRef operator[] (const std::string &key);

    void remove(const std::string &key);
    JsonValue take(const std::string &key);
    bool contains(const std::string &key) const;

    bool operator==(const JsonObject &other) const;
    bool operator!=(const JsonObject &other) const;

    class const_iterator;

    class iterator
    {
        friend class const_iterator;
        friend class JsonObject;
        JsonObject *o;
        int i;

    public:
        typedef std::random_access_iterator_tag iterator_category;
        typedef int difference_type;
        typedef JsonValue value_type;
        typedef JsonValueRef reference;

        inline std::string key() const { return o->keyAt(i); }
        inline JsonValueRef value() const { return JsonValueRef(o, i); }
        inline JsonValueRef operator*() const { return JsonValueRef(o, i); }

        inline bool operator==(const iterator &other) const { return i == other.i; }
        inline bool operator!=(const iterator &other) const { return i != other.i; }

        inline iterator &operator++() { ++i; return *this; }
        inline iterator operator++(int) { iterator r = *this; ++i; return r; }
        inline iterator &operator--() { --i; return *this; }
        inline iterator operator--(int) { iterator r = *this; --i; return r; }
        inline iterator operator+(int j) const
        { iterator r = *this; r.i += j; return r; }
        inline iterator operator-(int j) const { return operator+(-j); }
        inline iterator &operator+=(int j) { i += j; return *this; }
        inline iterator &operator-=(int j) { i -= j; return *this; }

    public:
        inline bool operator==(const const_iterator &other) const { return i == other.i; }
        inline bool operator!=(const const_iterator &other) const { return i != other.i; }
    };
    friend class iterator;

    class const_iterator
    {
        friend class iterator;
        const JsonObject *o;
        int i;

    public:
        typedef std::random_access_iterator_tag iterator_category;
        typedef int difference_type;
        typedef JsonValue value_type;
        typedef JsonValue reference;
        inline const_iterator(const iterator &other)
            : o(other.o), i(other.i) {}

        inline std::string key() const { return o->keyAt(i); }
        inline JsonValue value() const { return o->valueAt(i); }
        inline JsonValue operator*() const { return o->valueAt(i); }
        inline bool operator==(const const_iterator &other) const { return i == other.i; }
        inline bool operator!=(const const_iterator &other) const { return i != other.i; }

        inline const_iterator &operator++() { ++i; return *this; }
        inline const_iterator operator++(int) { const_iterator r = *this; ++i; return r; }
        inline const_iterator &operator--() { --i; return *this; }
        inline const_iterator operator--(int) { const_iterator r = *this; --i; return r; }
        inline const_iterator operator+(int j) const
        { const_iterator r = *this; r.i += j; return r; }
        inline const_iterator operator-(int j) const { return operator+(-j); }
        inline const_iterator &operator+=(int j) { i += j; return *this; }
        inline const_iterator &operator-=(int j) { i -= j; return *this; }

        inline bool operator==(const iterator &other) const { return i == other.i; }
        inline bool operator!=(const iterator &other) const { return i != other.i; }
    };
    friend class const_iterator;

    iterator erase(iterator it);

    // more Qt
    typedef iterator Iterator;
    typedef const_iterator ConstIterator;
    iterator find(const std::string &key);
    const_iterator find(const std::string &key) const { return constFind(key); }
    const_iterator constFind(const std::string &key) const;
    iterator insert(const std::string &key, const JsonValue &value);

    // STL compatibility
    typedef JsonValue mapped_type;
    typedef std::string key_type;
    typedef int size_type;

    inline bool empty() const { return isEmpty(); }

private:
    friend class JsonPrivate::Data;
    friend class JsonValue;
    friend class QJsonDocument;
    friend class JsonValueRef;


    JsonObject(JsonPrivate::Data *data, JsonPrivate::Object *object);
    void initialize();

    void detach(uint reserve = 0);
    bool detach2(uint reserve = 0);
    void compact();

    std::string keyAt(int i) const;
    JsonValue valueAt(int i) const;
    void setValueAt(int i, const JsonValue &val);

    JsonPrivate::Data *d;
    JsonPrivate::Object *o;
};

#endif // JsonObject_H
