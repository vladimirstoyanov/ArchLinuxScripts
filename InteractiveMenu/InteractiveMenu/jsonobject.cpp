#include "jsonobject.h"
#include "jsonvalue.h"
#include "jsonarray.h"
#include <vector>


JsonObject::JsonObject()
    : d(0), o(0)
{
}

JsonObject::JsonObject(JsonPrivate::Data *data, JsonPrivate::Object *object)
    : d(data), o(object)
{
    /*
    Q_ASSERT(d);
    Q_ASSERT(o);
    d->ref.ref();
    */
}

void JsonObject::initialize()
{
    d = 0;
    o = 0;
}

JsonObject::~JsonObject()
{
    /*
    if (d && !d->ref.deref())
        delete d; */
}

JsonObject::JsonObject(const JsonObject &other)
{
    d = other.d;
    o = other.o;
    //if (d)
      //  d->ref.ref();
}

JsonObject &JsonObject::operator =(const JsonObject &other)
{
    /*
    if (d != other.d) {
        if (d && !d->ref.deref())
            delete d;
        d = other.d;
        if (d)
            d->ref.ref();
    }
    o = other.o;
    */

    return *this;
}




/*!
    Returns a list of all keys in this object.

    The list is sorted lexographically.
 */
std::vector<std::string> JsonObject::keys() const
{
    std::vector<std::string> keys;
    /*
    if (o) {
        keys.reserve(o->length);
        for (uint i = 0; i < o->length; ++i) {
            JsonPrivate::Entry *e = o->entryAt(i);
            keys.push_back(e->key());
        }
    }
    */
    return keys;
}

int JsonObject::size() const
{
    /*
    if (!d)
        return 0;

    return o->length;
    */
    return 0;
}

bool JsonObject::isEmpty() const
{
    /*
    if (!d)
        return true;

    return !o->length;
    */
    return true;
}

JsonValue JsonObject::value(const std::string &key) const
{
    /*
    if (!d)
        return JsonValue(JsonValue::Undefined);

    bool keyExists;
    int i = o->indexOf(key, &keyExists);
    if (!keyExists)
        return JsonValue(JsonValue::Undefined);

    return JsonValue(d, o, o->entryAt(i)->value);
    */

    JsonValue jv;
    return jv;
}

JsonValue JsonObject::operator [](const std::string &key) const
{
    return value(key);
}

JsonValueRef JsonObject::operator [](const std::string &key)
{
    /*
    // ### somewhat inefficient, as we lookup the key twice if it doesn't yet exist
    bool keyExists = false;
    int index = o ? o->indexOf(key, &keyExists) : -1;
    if (!keyExists) {
        iterator i = insert(key, JsonValue());
        index = i.i;
    }
    */
    //return JsonValueRef(this, index);
}

JsonObject::iterator JsonObject::insert(const std::string &key, const JsonValue &value)
{
    /*
    if (value.t == JsonValue::Undefined) {
        remove(key);
        return end();
    }
    JsonValue val = value;

    bool latinOrIntValue;
    int valueSize = JsonPrivate::Value::requiredStorage(val, &latinOrIntValue);

    bool latinKey = JsonPrivate::useCompressed(key);
    int valueOffset = sizeof(JsonPrivate::Entry) + JsonPrivate::std::stringSize(key, latinKey);
    int requiredSize = valueOffset + valueSize;

    if (!detach2(requiredSize + sizeof(JsonPrivate::offset))) // offset for the new index entry
        return iterator();

    if (!o->length)
        o->tableOffset = sizeof(JsonPrivate::Object);

    bool keyExists = false;
    int pos = o->indexOf(key, &keyExists);
    if (keyExists)
        ++d->compactionCounter;

    uint off = o->reserveSpace(requiredSize, pos, 1, keyExists);
    if (!off)
        return end();

    JsonPrivate::Entry *e = o->entryAt(pos);
    e->value.type = val.t;
    e->value.latinKey = latinKey;
    e->value.latinOrIntValue = latinOrIntValue;
    e->value.value = JsonPrivate::Value::valueToStore(val, (char *)e - (char *)o + valueOffset);
    JsonPrivate::copyString((char *)(e + 1), key, latinKey);
    if (valueSize)
        JsonPrivate::Value::copyData(val, (char *)e + valueOffset, latinOrIntValue);

    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(o->length) / 2u)
        compact();
    */
    //return iterator(this, pos);
}

void JsonObject::remove(const std::string &key)
{
    /*
    if (!d)
        return;

    bool keyExists;
    int index = o->indexOf(key, &keyExists);
    if (!keyExists)
        return;

    detach2();
    o->removeItems(index, 1);
    ++d->compactionCounter;
    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(o->length) / 2u)
        compact();
    */
}

JsonValue JsonObject::take(const std::string &key)
{
    /*
    if (!o)
        return JsonValue(JsonValue::Undefined);

    bool keyExists;
    int index = o->indexOf(key, &keyExists);
    if (!keyExists)
        return JsonValue(JsonValue::Undefined);

    JsonValue v(d, o, o->entryAt(index)->value);
    detach2();
    o->removeItems(index, 1);
    ++d->compactionCounter;
    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(o->length) / 2u)
        compact();
    */
    //return v;
    JsonValue jv;
    return jv;
}

bool JsonObject::contains(const std::string &key) const
{
    /*
    if (!o)
        return false;

    bool keyExists;
    o->indexOf(key, &keyExists);
    return keyExists;
    */
    return false;
}

bool JsonObject::operator==(const JsonObject &other) const
{
    /*
    if (o == other.o)
        return true;

    if (!o)
        return !other.o->length;
    if (!other.o)
        return !o->length;
    if (o->length != other.o->length)
        return false;

    for (uint i = 0; i < o->length; ++i) {
        JsonPrivate::Entry *e = o->entryAt(i);
        JsonValue v(d, o, e->value);
        if (other.value(e->key()) != v)
            return false;
    }

    return true;
    */
    return false;
}

bool JsonObject::operator!=(const JsonObject &other) const
{
    return !(*this == other);
}

JsonObject::iterator JsonObject::erase(JsonObject::iterator it)
{
    /*
    Q_ASSERT(d && d->ref.load() == 1);
    if (it.o != this || it.i < 0 || it.i >= (int)o->length)
        return iterator(this, o->length);

    int index = it.i;

    o->removeItems(index, 1);
    ++d->compactionCounter;
    if (d->compactionCounter > 32u && d->compactionCounter >= unsigned(o->length) / 2u)
        compact();

    // iterator hasn't changed
    return it;
    */
}

JsonObject::iterator JsonObject::find(const std::string &key)
{
    /*
    bool keyExists = false;
    int index = o ? o->indexOf(key, &keyExists) : 0;
    if (!keyExists)
        return end();
    detach2();
    return iterator(this, index);
        */
}


JsonObject::const_iterator JsonObject::constFind(const std::string &key) const
{
    /*
    bool keyExists = false;
    int index = o ? o->indexOf(key, &keyExists) : 0;
    if (!keyExists)
        return end();
    return const_iterator(this, index);
    */
}

void JsonObject::detach(uint reserve)
{
    /*
    Q_UNUSED(reserve)
    Q_ASSERT(!reserve);
    */
    detach2(reserve);
}

bool JsonObject::detach2(uint reserve)
{
    /*
    if (!d) {
        if (reserve >= JsonPrivate::Value::MaxSize) {
            qWarning("QJson: Document too large to store in data structure");
            return false;
        }
        d = new JsonPrivate::Data(reserve, JsonValue::Object);
        o = static_cast<JsonPrivate::Object *>(d->header->root());
        d->ref.ref();
        return true;
    }
    if (reserve == 0 && d->ref.load() == 1)
        return true;

    JsonPrivate::Data *x = d->clone(o, reserve);
    if (!x)
        return false;
    x->ref.ref();
    if (!d->ref.deref())
        delete d;
    d = x;
    o = static_cast<JsonPrivate::Object *>(d->header->root());
    */
    return true;
}

void JsonObject::compact()
{
    /*
    if (!d || !d->compactionCounter)
        return;

    detach2();
    d->compact();
    o = static_cast<JsonPrivate::Object *>(d->header->root());
    */
}

std::string JsonObject::keyAt(int i) const
{
    /*
    Q_ASSERT(o && i >= 0 && i < (int)o->length);

    JsonPrivate::Entry *e = o->entryAt(i);
    return e->key();
    */
}

JsonValue JsonObject::valueAt(int i) const
{
    /*
    if (!o || i < 0 || i >= (int)o->length)
        return JsonValue(JsonValue::Undefined);

    JsonPrivate::Entry *e = o->entryAt(i);
    return JsonValue(d, o, e->value);
    */
}

void JsonObject::setValueAt(int i, const JsonValue &val)
{
    /*
    Q_ASSERT(o && i >= 0 && i < (int)o->length);

    JsonPrivate::Entry *e = o->entryAt(i);
    insert(e->key(), val);
    */
}
