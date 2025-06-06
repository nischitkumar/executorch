# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class StablehloSliceOptions(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StablehloSliceOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStablehloSliceOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def StablehloSliceOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed
        )

    # StablehloSliceOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StablehloSliceOptions
    def StartIndices(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # StablehloSliceOptions
    def StartIndicesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # StablehloSliceOptions
    def StartIndicesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloSliceOptions
    def StartIndicesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # StablehloSliceOptions
    def LimitIndices(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # StablehloSliceOptions
    def LimitIndicesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # StablehloSliceOptions
    def LimitIndicesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloSliceOptions
    def LimitIndicesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # StablehloSliceOptions
    def Strides(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # StablehloSliceOptions
    def StridesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # StablehloSliceOptions
    def StridesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloSliceOptions
    def StridesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0


def StablehloSliceOptionsStart(builder):
    builder.StartObject(3)


def Start(builder):
    StablehloSliceOptionsStart(builder)


def StablehloSliceOptionsAddStartIndices(builder, startIndices):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(startIndices), 0
    )


def AddStartIndices(builder, startIndices):
    StablehloSliceOptionsAddStartIndices(builder, startIndices)


def StablehloSliceOptionsStartStartIndicesVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def StartStartIndicesVector(builder, numElems: int) -> int:
    return StablehloSliceOptionsStartStartIndicesVector(builder, numElems)


def StablehloSliceOptionsAddLimitIndices(builder, limitIndices):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(limitIndices), 0
    )


def AddLimitIndices(builder, limitIndices):
    StablehloSliceOptionsAddLimitIndices(builder, limitIndices)


def StablehloSliceOptionsStartLimitIndicesVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def StartLimitIndicesVector(builder, numElems: int) -> int:
    return StablehloSliceOptionsStartLimitIndicesVector(builder, numElems)


def StablehloSliceOptionsAddStrides(builder, strides):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(strides), 0
    )


def AddStrides(builder, strides):
    StablehloSliceOptionsAddStrides(builder, strides)


def StablehloSliceOptionsStartStridesVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def StartStridesVector(builder, numElems: int) -> int:
    return StablehloSliceOptionsStartStridesVector(builder, numElems)


def StablehloSliceOptionsEnd(builder):
    return builder.EndObject()


def End(builder):
    return StablehloSliceOptionsEnd(builder)
