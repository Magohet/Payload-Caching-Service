from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_snake

__all__ = ["ImmutableDTO", "MutableDTO", "MUTABLE_MODEL_CONFIG", "IMMUTABLE_MODEL_CONFIG"]

BASE_MODEL_CONFIG = dict(
    str_strip_whitespace=True,
    use_enum_values=True,
    from_attributes=True,
    alias_generator=to_snake,
    allow_inf_nan=False,
    ser_json_timedelta="iso8601",
    ser_json_bytes="base64",
    validate_return=True,
    coerce_numbers_to_str=True,
    regex_engine="python-re",
    use_attribute_docstrings=True,
    extra="forbid",
    populate_by_name=True,
)

MUTABLE_MODEL_CONFIG = ConfigDict(**BASE_MODEL_CONFIG, frozen=False)
IMMUTABLE_MODEL_CONFIG = ConfigDict(**BASE_MODEL_CONFIG, frozen=True)


class MutableDTO(BaseModel):
    model_config = MUTABLE_MODEL_CONFIG


class ImmutableDTO(BaseModel):
    model_config = IMMUTABLE_MODEL_CONFIG
