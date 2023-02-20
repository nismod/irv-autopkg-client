from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.envelope import Envelope
    from ..models.geometry import Geometry


T = TypeVar("T", bound="Boundary")


@attr.s(auto_attribs=True)
class Boundary:
    """Complete boundary information

    Attributes:
        name (str):
        name_long (str):
        admin_level (str):
        geometry (Geometry):
        envelope (Envelope):
    """

    name: str
    name_long: str
    admin_level: str
    geometry: "Geometry"
    envelope: "Envelope"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        name_long = self.name_long
        admin_level = self.admin_level
        geometry = self.geometry.to_dict()

        envelope = self.envelope.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "name_long": name_long,
                "admin_level": admin_level,
                "geometry": geometry,
                "envelope": envelope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.envelope import Envelope
        from ..models.geometry import Geometry

        d = src_dict.copy()
        name = d.pop("name")

        name_long = d.pop("name_long")

        admin_level = d.pop("admin_level")

        geometry = Geometry.from_dict(d.pop("geometry"))

        envelope = Envelope.from_dict(d.pop("envelope"))

        boundary = cls(
            name=name,
            name_long=name_long,
            admin_level=admin_level,
            geometry=geometry,
            envelope=envelope,
        )

        boundary.additional_properties = d
        return boundary

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
