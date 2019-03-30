#ifndef JSONVALUE_H
#define JSONVALUE_H

#include <string>
#include <vector>

class JsonArray;
class JsonObject;

namespace JsonPrivate {
    class Data;
    class Base;
    class Object;
    class Header;
    class Array;
    class Value;
    class Entry;
}

class JsonValue
{
public:
    enum Type {
        Null =  0x0,
        Bool = 0x1,
        Double = 0x2,
        String = 0x3,
        Array = 0x4,
        Object = 0x5,
        Undefined = 0x80
    };

    JsonValue(Type = Null);
    JsonValue(bool b);
    JsonValue(double n);
    JsonValue(int n);
    JsonValue(const std::string &s);

    JsonValue(const JsonArray &a);
    JsonValue(const JsonObject &o);

    ~JsonValue();

    JsonValue(const JsonValue &other);
    JsonValue &operator =(const JsonValue &other);

    JsonValue(JsonValue &&other)
        : ui(other.ui),
          d(other.d),
          t(other.t)
    {
        other.ui = 0;
        other.d = nullptr;
        other.t = Null;
    }

    JsonValue &operator =(JsonValue &&other)
    {
        swap(other);
        return *this;
    }

    void swap(JsonValue &other)
    {
        std::swap(ui, other.ui);
        std::swap(d, other.d);
        std::swap(t, other.t);
    }

    //static JsonValue fromVariant(const QVariant &variant);
    //QVariant toVariant() const;

    Type type() const;
    inline bool isNull() const { return type() == Null; }
    inline bool isBool() const { return type() == Bool; }
    inline bool isDouble() const { return type() == Double; }
    inline bool isString() const { return type() == String; }
    inline bool isArray() const { return type() == Array; }
    inline bool isObject() const { return type() == Object; }
    inline bool isUndefined() const { return type() == Undefined; }

    bool toBool(bool defaultValue = false) const;
    int toInt(int defaultValue = 0) const;
    double toDouble(double defaultValue = 0) const;
    std::string toString() const;
    std::string toString(const std::string &defaultValue) const;
    JsonArray toArray() const;
    JsonArray toArray(const JsonArray &defaultValue) const;
    JsonObject toObject() const;
    JsonObject toObject(const JsonObject &defaultValue) const;

    const JsonValue operator[](const std::string &key) const;
    const JsonValue operator[](int i) const;

    bool operator==(const JsonValue &other) const;
    bool operator!=(const JsonValue &other) const;

private:
    // avoid implicit conversions from char * to bool
    inline JsonValue(const void *) {}
    friend class JsonPrivate::Value;
    friend class JsonArray;
    friend class JsonObject;

    JsonValue(JsonPrivate::Data *d, JsonPrivate::Base *b, const JsonPrivate::Value& v);
    void stringDataFromQStringHelper(const std::string &str);

    void detach();

    union {
        int ui;
        bool b;
        double dbl;
        std::vector<std::string> stringData;
        JsonPrivate::Base *base;
    };
    JsonPrivate::Data *d; // needed for Objects and Arrays
    Type t;
};

class JsonValueRef
{
public:
    JsonValueRef(JsonArray *array, int idx)
        : a(array), is_object(false), index(idx) {}
    JsonValueRef(JsonObject *object, int idx)
        : o(object), is_object(true), index(idx) {}

    inline operator JsonValue() const { return toValue(); }
    JsonValueRef &operator = (const JsonValue &val);
    JsonValueRef &operator = (const JsonValueRef &val);

    inline JsonValue::Type type() const { return toValue().type(); }
    inline bool isNull() const { return type() == JsonValue::Null; }
    inline bool isBool() const { return type() == JsonValue::Bool; }
    inline bool isDouble() const { return type() == JsonValue::Double; }
    inline bool isString() const { return type() == JsonValue::String; }
    inline bool isArray() const { return type() == JsonValue::Array; }
    inline bool isObject() const { return type() == JsonValue::Object; }
    inline bool isUndefined() const { return type() == JsonValue::Undefined; }

    inline bool toBool() const { return toValue().toBool(); }
    inline int toInt() const { return toValue().toInt(); }
    inline double toDouble() const { return toValue().toDouble(); }
    inline std::string toString() const { return toValue().toString(); }
    JsonArray toArray() const;
    JsonObject toObject() const;

    inline bool toBool(bool defaultValue) const { return toValue().toBool(defaultValue); }
    inline int toInt(int defaultValue) const { return toValue().toInt(defaultValue); }
    inline double toDouble(double defaultValue) const { return toValue().toDouble(defaultValue); }
    inline std::string toString(const std::string &defaultValue) const { return toValue().toString(defaultValue); }

    inline bool operator==(const JsonValue &other) const { return toValue() == other; }
    inline bool operator!=(const JsonValue &other) const { return toValue() != other; }

private:
    JsonValue toValue() const;

    union {
        JsonArray *a;
        JsonObject *o;
    };
    uint is_object : 1;
    int index : 31;
};

#endif // JSONVALUE_H
