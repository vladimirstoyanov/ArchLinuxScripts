#include "jsonobject.h"
#include "jsonvalue.h"
#include "jsonarray.h"
//#include <qurl.h>
//#include <quuid.h>
//#include <qvariant.h>
#include <vector>//#include <qstringlist.h>
//#include <qdebug.h>


JsonValue::JsonValue(Type type)
    : ui(0), d(0), t(type)
{
}

/*!
    \internal
 */
JsonValue::JsonValue(JsonPrivate::Data *data, JsonPrivate::Base *base, const JsonPrivate::Value &v)
    : d(0)
{
    //t = (Type)(uint)v.type;
    switch (t) {
    case Undefined:
    case Null:
        dbl = 0;
        break;
    case Bool:
        //b = v.toBoolean();
        break;
    case Double:
        //dbl = v.toDouble(base);
        break;
    case String: {
        //std::string s = v.toString(base);
        //stringData = s.data_ptr();
        //stringData->ref.ref();
        break;
    }
    case Array:
    case Object:
        d = data;
        //this->base = v.base(base);
        break;
    }
    //if (d)
      //  d->ref.ref();
}

JsonValue::JsonValue(bool b)
    : d(0), t(Bool)
{
    this->b = b;
}

JsonValue::JsonValue(double n)
    : d(0), t(Double)
{
    this->dbl = n;
}

JsonValue::JsonValue(int n)
    : d(0), t(Double)
{
    this->dbl = n;
}


JsonValue::JsonValue(const std::string &s)
    : d(0), t(String)
{
    //stringDataFromQStringHelper(s);
}


/*
void JsonValue::stringDataFromQStringHelper(const QString &string)
{
    stringData = *(QStringData **)(&string);
    stringData->ref.ref();
}
*/

JsonValue::JsonValue(const JsonArray &a)
    : d(a.d), t(Array)
{
    /*
    base = a.a;
    if (d)
        d->ref.ref(); */
}

JsonValue::JsonValue(const JsonObject &o)
    : d(o.d), t(Object)
{
    /*
    base = o.o;
    if (d)
        d->ref.ref();
        */
}

JsonValue::~JsonValue()
{
    //if (d && !d->ref.deref())
      //  delete d;
}

JsonValue::JsonValue(const JsonValue &other)
{
    /*
    t = other.t;
    d = other.d;
    ui = other.ui;
    if (d)
        d->ref.ref();

    if (t == String && stringData)
        stringData->ref.ref();
      */
}

JsonValue &JsonValue::operator =(const JsonValue &other)
{
    JsonValue copy(other);
    swap(copy);
    return *this;
}


JsonValue::Type JsonValue::type() const
{
    return t;
}

/*!
    Converts the value to a bool and returns it.

    If type() is not bool, the \a defaultValue will be returned.
 */
bool JsonValue::toBool(bool defaultValue) const
{
    if (t != Bool)
        return defaultValue;
    return b;
}

/*!
    \since 5.2
    Converts the value to an int and returns it.

    If type() is not Double or the value is not a whole number,
    the \a defaultValue will be returned.
 */
int JsonValue::toInt(int defaultValue) const
{
    if (t == Double && int(dbl) == dbl)
        return int(dbl);
    return defaultValue;
}

/*!
    Converts the value to a double and returns it.

    If type() is not Double, the \a defaultValue will be returned.
 */
double JsonValue::toDouble(double defaultValue) const
{
    if (t != Double)
        return defaultValue;
    return dbl;
}

/*!
    Converts the value to a QString and returns it.

    If type() is not String, the \a defaultValue will be returned.
 */
std::string JsonValue::toString(const std::string &defaultValue) const
{
    /*
    if (t != String)
        return defaultValue;
    stringData->ref.ref(); // the constructor below doesn't add a ref.
    QStringDataPtr holder = { stringData };
    return QString(holder);
    */
    return "";
}

/*!
    Converts the value to a QString and returns it.

    If type() is not String, a null QString will be returned.

    \sa QString::isNull()
 */
std::string JsonValue::toString() const
{
    /*
    if (t != String)
        return QString();
    stringData->ref.ref(); // the constructor below doesn't add a ref.
    QStringDataPtr holder = { stringData };
    return QString(holder);
    */
    return "";
}

/*!
    Converts the value to an array and returns it.

    If type() is not Array, the \a defaultValue will be returned.
 */
JsonArray JsonValue::toArray(const JsonArray &defaultValue) const
{
    /*
    if (!d || t != Array)
        return defaultValue;

    return JsonArray(d, static_cast<JsonPrivate::Array *>(base));
    */
    JsonArray ja;
    return ja;
}

JsonArray JsonValue::toArray() const
{
    return toArray(JsonArray());
}

JsonObject JsonValue::toObject(const JsonObject &defaultValue) const
{
    /*
    if (!d || t != Object)
        return defaultValue;

    return JsonObject(d, static_cast<QJsonPrivate::Object *>(base));
    */
    JsonObject jo;
    return jo;
}

JsonObject JsonValue::toObject() const
{
    return toObject(JsonObject());
}

const JsonValue JsonValue::operator[](const std::string &key) const
{
    if (!isObject())
        return JsonValue(JsonValue::Undefined);

    //return toObject().value(key);
    JsonValue jv;
    return jv;
}

const JsonValue JsonValue::operator[](int i) const
{
    /*
    if (!isArray())
        return QJsonValue(QJsonValue::Undefined);

    return toArray().at(i);
    */

    JsonValue jv;
    return jv;
}

bool JsonValue::operator==(const JsonValue &other) const
{
    if (t != other.t)
        return false;

    switch (t) {
    case Undefined:
    case Null:
        break;
    case Bool:
        return b == other.b;
    case Double:
        return dbl == other.dbl;
    case String:
        return toString() == other.toString();
    case Array:
        if (base == other.base)
            return true;
        //if (!base)
        //    return !other.base->length;
        //if (!other.base)
        //    return !base->length;
       // return QJsonArray(d, static_cast<QJsonPrivate::Array *>(base))
        //        == QJsonArray(other.d, static_cast<QJsonPrivate::Array *>(other.base));
    case Object:
        if (base == other.base)
            return true;
        //if (!base)
        //    return !other.base->length;
        //if (!other.base)
        //    return !base->length;
        //return QJsonObject(d, static_cast<QJsonPrivate::Object *>(base))
        //        == QJsonObject(other.d, static_cast<QJsonPrivate::Object *>(other.base));
    }
    return true;
}

bool JsonValue::operator!=(const JsonValue &other) const
{
    return !(*this == other);
}

void JsonValue::detach()
{
    /*
    if (!d)
        return;

    JsonPrivate::Data *x = d->clone(base);
    x->ref.ref();
    if (!d->ref.deref())
        delete d;
    d = x;
    base = static_cast<QJsonPrivate::Object *>(d->header->root());
    */
}


JsonValueRef &JsonValueRef::operator =(const JsonValue &val)
{
    /*
    if (is_object)
        o->setValueAt(index, val);
    else
        a->replace(index, val);
    */
    return *this;
}

JsonValueRef &JsonValueRef::operator =(const JsonValueRef &ref)
{
    /*
    if (is_object)
        o->setValueAt(index, ref);
    else
        a->replace(index, ref);
    */
    return *this;
}

JsonArray JsonValueRef::toArray() const
{
   //return toValue().toArray();
}

JsonObject JsonValueRef::toObject() const
{
    //return toValue().toObject();
}
