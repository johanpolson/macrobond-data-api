from typing import Generic, Sequence, TypeVar, overload

from macrobond_data_api.common.types import (
    MetadataAttributeInformation,
    MetadataValueInformationItem,
    RevisionInfo,
)

_TypeVar = TypeVar("_TypeVar")


class _ReprHtmlSequence(Sequence[_TypeVar], Generic[_TypeVar]):
    __slots__ = ("items",)

    items: Sequence[_TypeVar]

    def __init__(self, items: Sequence[_TypeVar]) -> None:
        super().__init__()
        self.items = items

    @overload
    def __getitem__(self, i: int) -> _TypeVar:
        ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[_TypeVar]:
        ...

    def __getitem__(self, key):  # type: ignore
        return _ReprHtmlSequence(self.items[key]) if isinstance(key, slice) else self.items[key]

    def __len__(self) -> int:
        return len(self.items)

    def _ipython_display_(self) -> None:
        # pylint: disable=import-outside-toplevel
        from IPython.display import display  # type: ignore
        import pandas  # type: ignore

        # pylint: enable=import-outside-toplevel

        if len(self.items) > 1 and len(set((type(x) for x in self.items))) == 1:
            t = type(self.items[0])
            if t in (MetadataAttributeInformation, MetadataValueInformationItem, RevisionInfo):
                display(pandas.concat([x.to_pd_data_frame() for x in self.items]))  # type: ignore
                return

        for x in self.items:
            display(x)
