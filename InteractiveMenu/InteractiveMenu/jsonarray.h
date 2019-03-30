#ifndef JSONARRAY_H
#define JSONARRAY_H

#include "jsonvalue.h"
//#include <QtCore/qiterator.h>




class JsonArray
{
public:
    JsonArray();

    ~JsonArray();

    JsonArray(const JsonArray &other);
    JsonArray &operator =(const JsonArray &other);

    JsonArray(JsonArray &&other)
        : d(other.d),
          a(other.a)
    {
        other.d = nullptr;
        other.a = nullptr;
    }

    JsonArray &operator =(JsonArray &&other)
    {
        swap(other);
        return *this;
    }

    //static JsonArray fromStringList(const StringList &list);
    //static JsonArray fromVariantList(const VariantList &list);
    //QVariantList toVariantList() const;

    int size() const;
    inline int count() const { return size(); }

    bool isEmpty() const;
    JsonValue at(int i) const;
    JsonValue first() const;
    JsonValue last() const;

    void prepend(const JsonValue &value);
    void append(const JsonValue &value);
    void removeAt(int i);
    JsonValue takeAt(int i);
    inline void removeFirst() { removeAt(0); }
    inline void removeLast() { removeAt(size() - 1); }

    void insert(int i, const JsonValue &value);
    void replace(int i, const JsonValue &value);

    bool contains(const JsonValue &element) const;
    JsonValueRef operator[](int i);
    JsonValue operator[](int i) const;

    bool operator==(const JsonArray &other) const;
    bool operator!=(const JsonArray &other) const;

    void swap(JsonArray &other)
    {
        std::swap(d, other.d);
        std::swap(a, other.a);
    }

    class const_iterator;

    class iterator {
    public:
        JsonArray *a;
        int i;
        typedef std::random_access_iterator_tag  iterator_category;
        typedef int difference_type;
        typedef JsonValue value_type;
        typedef JsonValueRef reference;
        //typedef JsonValueRefPtr pointer;

        inline iterator() : a(nullptr), i(0) { }
        explicit inline iterator(JsonArray *array, int index) : a(array), i(index) { }

        inline JsonValueRef operator*() const { return JsonValueRef(a, i); }

        inline JsonValueRef operator[](int j) const { return JsonValueRef(a, i + j); }

        inline bool operator==(const iterator &o) const { return i == o.i; }
        inline bool operator!=(const iterator &o) const { return i != o.i; }
        inline bool operator<(const iterator& other) const { return i < other.i; }
        inline bool operator<=(const iterator& other) const { return i <= other.i; }
        inline bool operator>(const iterator& other) const { return i > other.i; }
        inline bool operator>=(const iterator& other) const { return i >= other.i; }
        inline bool operator==(const const_iterator &o) const { return i == o.i; }
        inline bool operator!=(const const_iterator &o) const { return i != o.i; }
        inline bool operator<(const const_iterator& other) const { return i < other.i; }
        inline bool operator<=(const const_iterator& other) const { return i <= other.i; }
        inline bool operator>(const const_iterator& other) const { return i > other.i; }
        inline bool operator>=(const const_iterator& other) const { return i >= other.i; }
        inline iterator &operator++() { ++i; return *this; }
        inline iterator operator++(int) { iterator n = *this; ++i; return n; }
        inline iterator &operator--() { i--; return *this; }
        inline iterator operator--(int) { iterator n = *this; i--; return n; }
        inline iterator &operator+=(int j) { i+=j; return *this; }
        inline iterator &operator-=(int j) { i-=j; return *this; }
        inline iterator operator+(int j) const { return iterator(a, i+j); }
        inline iterator operator-(int j) const { return iterator(a, i-j); }
        inline int operator-(iterator j) const { return i - j.i; }
    };
    friend class iterator;

    class const_iterator {
    public:
        const JsonArray *a;
        int i;
        //typedef std::random_access_iterator_tag  iterator_category;
        //typedef qptrdiff difference_type;
        typedef JsonValue value_type;
        typedef JsonValue reference;
        //typedef JsonValuePtr pointer;

        inline const_iterator() : a(nullptr), i(0) { }
        explicit inline const_iterator(const JsonArray *array, int index) : a(array), i(index) { }

        inline const_iterator(const iterator &o) : a(o.a), i(o.i) {}

        inline JsonValue operator*() const { return a->at(i); }

        inline JsonValue operator[](int j) const { return a->at(i+j); }
        inline bool operator==(const const_iterator &o) const { return i == o.i; }
        inline bool operator!=(const const_iterator &o) const { return i != o.i; }
        inline bool operator<(const const_iterator& other) const { return i < other.i; }
        inline bool operator<=(const const_iterator& other) const { return i <= other.i; }
        inline bool operator>(const const_iterator& other) const { return i > other.i; }
        inline bool operator>=(const const_iterator& other) const { return i >= other.i; }
        inline const_iterator &operator++() { ++i; return *this; }
        inline const_iterator operator++(int) { const_iterator n = *this; ++i; return n; }
        inline const_iterator &operator--() { i--; return *this; }
        inline const_iterator operator--(int) { const_iterator n = *this; i--; return n; }
        inline const_iterator &operator+=(int j) { i+=j; return *this; }
        inline const_iterator &operator-=(int j) { i-=j; return *this; }
        inline const_iterator operator+(int j) const { return const_iterator(a, i+j); }
        inline const_iterator operator-(int j) const { return const_iterator(a, i-j); }
        inline int operator-(const_iterator j) const { return i - j.i; }
    };
    friend class const_iterator;

    // stl style
    inline iterator begin() { detach2(); return iterator(this, 0); }
    inline const_iterator begin() const { return const_iterator(this, 0); }
    inline const_iterator constBegin() const { return const_iterator(this, 0); }
    inline iterator end() { detach2(); return iterator(this, size()); }
    inline const_iterator end() const { return const_iterator(this, size()); }
    inline const_iterator constEnd() const { return const_iterator(this, size()); }
    iterator insert(iterator before, const JsonValue &value) { insert(before.i, value); return before; }
    iterator erase(iterator it) { removeAt(it.i); return it; }

    // more Qt
    typedef iterator Iterator;
    typedef const_iterator ConstIterator;

    // convenience
    inline JsonArray operator+(const JsonValue &v) const
    { JsonArray n = *this; n += v; return n; }
    inline JsonArray &operator+=(const JsonValue &v)
    { append(v); return *this; }
    inline JsonArray &operator<< (const JsonValue &v)
    { append(v); return *this; }

    // stl compatibility
    inline void push_back(const JsonValue &t) { append(t); }
    inline void push_front(const JsonValue &t) { prepend(t); }
    inline void pop_front() { removeFirst(); }
    inline void pop_back() { removeLast(); }
    inline bool empty() const { return isEmpty(); }
    typedef int size_type;
    typedef JsonValue value_type;
    typedef value_type *pointer;
    typedef const value_type *const_pointer;
    typedef JsonValueRef reference;
    typedef JsonValue const_reference;
    typedef int difference_type;

private:
    friend class JsonPrivate::Data;
    friend class JsonValue;
    friend class JsonDocument;

    JsonArray(JsonPrivate::Data *data, JsonPrivate::Array *array);
    void initialize();
    void compact();
    // ### Qt 6: remove me and merge with detach2
    void detach(uint reserve = 0);
    bool detach2(uint reserve = 0);

    JsonPrivate::Data *d;
    JsonPrivate::Array *a;
};

#endif // JSONARRAY_H
