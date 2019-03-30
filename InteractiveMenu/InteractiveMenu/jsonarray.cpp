#include "jsonobject.h"
#include "jsonvalue.h"
#include "jsonarray.h"
//#include <qstringlist.h"
#include <vector>

JsonArray::JsonArray()
    : d(0), a(0)
{
}

JsonArray::JsonArray(JsonPrivate::Data *data, JsonPrivate::Array *array)
    : d(data), a(array)
{
    /*
    Q_ASSERT(data);
    Q_ASSERT(array);
    d->ref.ref();
    */
}

void JsonArray::initialize()
{
    d = 0;
    a = 0;
}

JsonArray::~JsonArray()
{
    //if (d && !d->ref.deref())
    //    delete d;
}

JsonArray::JsonArray(const JsonArray &other)
{
    d = other.d;
    a = other.a;
    //if (d)
    //    d->ref.ref();
}

JsonArray &JsonArray::operator =(const JsonArray &other)
{
    /*
    if (d != other.d) {
        if (d && !d->ref.deref())
            delete d;
        d = other.d;
        if (d)
            d->ref.ref();
    }
    a = other.a;
    */
    return *this;
}

int JsonArray::size() const
{
    if (!d)
        return 0;

    return 0;// (int)a->length;
}

bool JsonArray::isEmpty() const
{
    if (!d)
        return true;

    return true;//!a->length;
}

JsonValue JsonArray::at(int i) const
{
    /*
    if (!a || i < 0 || i >= (int)a->length)
        return JsonValue(JsonValue::Undefined);
    */

    //return JsonValue(d, a, a->at(i));
    JsonValue jv;
    return jv;
}

JsonValue JsonArray::first() const
{
    return at(0);
}

JsonValue JsonArray::last() const
{
    //return at(a ? (a->length - 1) : 0);
    JsonValue jv;
    return jv;
}

void JsonArray::prepend(const JsonValue &value)
{
    insert(0, value);
}

void JsonArray::append(const JsonValue &value)
{
    //insert(a ? (int)a->length : 0, value);
}

void JsonArray::removeAt(int i)
{
    /*
    if (!a || i < 0 || i >= (int)a->length)
        return;

    detach2();
    a->removeItems(i, 1);
    ++d->compactionCounter;
    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(a->length) / 2u)
        compact();
    */
}

JsonValue JsonArray::takeAt(int i)
{
    /*
    if (!a || i < 0 || i >= (int)a->length)
        return JsonValue(JsonValue::Undefined);

    JsonValue v(d, a, a->at(i));
    removeAt(i); // detaches

    return v;
    */
    JsonValue jv;
    return jv;
}

void JsonArray::insert(int i, const JsonValue &value)
{
    /*
    Q_ASSERT (i >= 0 && i <= (a ? (int)a->length : 0));
    JsonValue val = value;

    bool compressed;
    int valueSize = JsonPrivate::Value::requiredStorage(val, &compressed);

    if (!detach2(valueSize + sizeof(JsonPrivate::Value)))
        return;

    if (!a->length)
        a->tableOffset = sizeof(JsonPrivate::Array);

    int valueOffset = a->reserveSpace(valueSize, i, 1, false);
    if (!valueOffset)
        return;

    JsonPrivate::Value &v = (*a)[i];
    v.type = (val.t == JsonValue::Undefined ? JsonValue::Null : val.t);
    v.latinOrIntValue = compressed;
    v.latinKey = false;
    v.value = JsonPrivate::Value::valueToStore(val, valueOffset);
    if (valueSize)
        JsonPrivate::Value::copyData(val, (char *)a + valueOffset, compressed);
        */
}

void JsonArray::replace(int i, const JsonValue &value)
{
    /*
    Q_ASSERT (a && i >= 0 && i < (int)(a->length));
    JsonValue val = value;

    bool compressed;
    int valueSize = JsonPrivate::Value::requiredStorage(val, &compressed);

    if (!detach2(valueSize))
        return;

    if (!a->length)
        a->tableOffset = sizeof(JsonPrivate::Array);

    int valueOffset = a->reserveSpace(valueSize, i, 1, true);
    if (!valueOffset)
        return;

    JsonPrivate::Value &v = (*a)[i];
    v.type = (val.t == JsonValue::Undefined ? JsonValue::Null : val.t);
    v.latinOrIntValue = compressed;
    v.latinKey = false;
    v.value = JsonPrivate::Value::valueToStore(val, valueOffset);
    if (valueSize)
        JsonPrivate::Value::copyData(val, (char *)a + valueOffset, compressed);

    ++d->compactionCounter;
    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(a->length) / 2u)
        compact();
        */
}

bool JsonArray::contains(const JsonValue &value) const
{
    for (int i = 0; i < size(); i++) {
        if (at(i) == value)
            return true;
    }
    return false;
}

JsonValueRef JsonArray::operator [](int i)
{
    /*
    Q_ASSERT(a && i >= 0 && i < (int)a->length);
    return JsonValueRef(this, i);
    */
    return JsonValueRef(this, i);
}

JsonValue JsonArray::operator[](int i) const
{
    return at(i);
}

bool JsonArray::operator==(const JsonArray &other) const
{
    /*
    if (a == other.a)
        return true;

    if (!a)
        return !other.a->length;
    if (!other.a)
        return !a->length;
    if (a->length != other.a->length)
        return false;

    for (int i = 0; i < (int)a->length; ++i) {
        if (JsonValue(d, a, a->at(i)) != JsonValue(other.d, other.a, other.a->at(i)))
            return false;
    }
    */
    return true;
}

bool JsonArray::operator!=(const JsonArray &other) const
{
    return !(*this == other);
}

void JsonArray::detach(uint reserve)
{
    /*
    Q_UNUSED(reserve)
    Q_ASSERT(!reserve);
    */
    detach2(0);
}

bool JsonArray::detach2(uint reserve)
{
    /*
    if (!d) {
        if (reserve >= JsonPrivate::Value::MaxSize) {
            qWarning("QJson: Document too large to store in data structure");
            return false;
        }
        d = new JsonPrivate::Data(reserve, JsonValue::Array);
        a = static_cast<JsonPrivate::Array *>(d->header->root());
        d->ref.ref();
        return true;
    }
    if (reserve == 0 && d->ref.load() == 1)
        return true;

    JsonPrivate::Data *x = d->clone(a, reserve);
    if (!x)
        return false;
    x->ref.ref();
    if (!d->ref.deref())
        delete d;
    d = x;
    a = static_cast<JsonPrivate::Array *>(d->header->root());
    */
    return true;
}

void JsonArray::compact()
{
    /*
    if (!d || !d->compactionCounter)
        return;

    detach2();
    d->compact();
    a = static_cast<JsonPrivate::Array *>(d->header->root());
    */
}
