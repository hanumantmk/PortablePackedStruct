from portable_packed_struct import *

print("#include \"PortablePackedStruct.h\"\n\n")

print(CLASS("TestEmbed", [
    FIELD("int", "intValue"),
    FIELD("short", "shortValue"),
]).cpp())

print(CLASS("TestClass", [
    UNION([
        STRUCT([
            FIELD("char", "type"),
            BITFIELD(FIELD("unsigned char", "bm"), [
                BITFIELDFIELD("unsigned", "refCounter", 1),
                BITFIELDFIELD("unsigned", "pada", 4),
                BITFIELDFIELD("unsigned", "shortStr", 1),
                BITFIELDFIELD("unsigned", "padb", 2),
            ]),
            UNION([
                FIELD("char", "oid", 12),
                STRUCT([
                    FIELD("char", "shortStrSize"),
                    FIELD("char", "shortStrStorage", 12),
                    FIELD("char", "nulTerminator"),
                ]),
                STRUCT([
                    UNION([
                        FIELD("char", "pad", 6),
                        FIELD("unsigned char", "binSubType"),
                        FIELD("char", "stringCache", 6),
                    ]),
                    UNION([
                        FIELD("long long", "longValue"),
                        FIELD("void *", "genericRcPtr"),
                        FIELD("double", "doubleValue"),
                        FIELD("bool", "boolValue"),
                        FIELD("int", "intValue"),
                        FIELD("long long", "dateValue"),
                    ])
                ])
            ])
        ]),
        PPSTRUCT("TestEmbed::Ptr", "te"),
        PPSTRUCT("TestEmbed::Ptr", "te_array", 2),
        FIELD("long long", "i64", 2),
    ])
]).cpp())

print(CLASS("DoubleClass", [
    FIELD("double", "doubleValue"),
]).cpp())