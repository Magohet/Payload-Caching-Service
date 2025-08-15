from typing import Self

from sqlalchemy.exc import DataError, IntegrityError

from core.types import ExceptionDetail

__all__ = [
    "ExceptionDetail",
    "SQLAlchemyExceptionParser",
]

error_codes = {
    DataError: {
        "22000": "data_exception",
        "2202E": "array_subscript_error",
        "22021": "character_not_in_repertoire",
        "22008": "datetime_field_overflow",
        "22012": "division_by_zero",
        "22005": "error_in_assignment",
        "2200B": "escape_character_conflict",
        "22022": "indicator_overflow",
        "22015": "interval_field_overflow",
        "2201E": "invalid_argument_for_logarithm",
        "22014": "invalid_argument_for_ntile_function",
        "22016": "invalid_argument_for_nth_value_function",
        "2201F": "invalid_argument_for_power_function",
        "2201G": "invalid_argument_for_width_bucket_function",
        "22018": "invalid_character_value_for_cast",
        "22007": "invalid_datetime_format",
        "22019": "invalid_escape_character",
        "2200D": "invalid_escape_octet",
        "22025": "invalid_escape_sequence",
        "22P06": "nonstandard_use_of_escape_character",
        "22010": "invalid_indicator_parameter_value",
        "22023": "invalid_parameter_value",
        "22013": "invalid_preceding_or_following_size",
        "2201B": "invalid_regular_expression",
        "2201W": "invalid_row_count_in_limit_clause",
        "2201X": "invalid_row_count_in_result_offset_clause",
        "2202H": "invalid_tablesample_argument",
        "2202G": "invalid_tablesample_repeat",
        "22009": "invalid_time_zone_displacement_value",
        "2200C": "invalid_use_of_escape_character",
        "2200G": "most_specific_type_mismatch",
        "22004": "null_value_not_allowed",
        "22002": "null_value_no_indicator_parameter",
        "22003": "numeric_value_out_of_range",
        "2200H": "sequence_generator_limit_exceeded",
        "22026": "string_data_length_mismatch",
        "22001": "string_data_right_truncation",
        "22011": "substring_error",
        "22027": "trim_error",
        "22024": "unterminated_c_string",
        "2200F": "zero_length_character_string",
        "22P01": "floating_point_exception",
        "22P02": "invalid_text_representation",
        "22P03": "invalid_binary_representation",
        "22P04": "bad_copy_file_format",
        "22P05": "untranslatable_character",
        "2200L": "not_an_xml_document",
        "2200M": "invalid_xml_document",
        "2200N": "invalid_xml_content",
        "2200S": "invalid_xml_comment",
        "2200T": "invalid_xml_processing_instruction",
        "22030": "duplicate_json_object_key_value",
        "22031": "invalid_argument_for_sql_json_datetime_function",
        "22032": "invalid_json_text",
        "22033": "invalid_sql_json_subscript",
        "22034": "more_than_one_sql_json_item",
        "22035": "no_sql_json_item",
        "22036": "non_numeric_sql_json_item",
        "22037": "non_unique_keys_in_a_json_object",
        "22038": "singleton_sql_json_item_required",
        "22039": "sql_json_array_not_found",
        "2203A": "sql_json_member_not_found",
        "2203B": "sql_json_number_not_found",
        "2203C": "sql_json_object_not_found",
        "2203D": "too_many_json_array_elements",
        "2203E": "too_many_json_object_members",
        "2203F": "sql_json_scalar_required",
        "2203G": "sql_json_item_cannot_be_cast_to_target_type",
    },
    IntegrityError: {
        "23000": "integrity_constraint_violation",
        "23001": "restrict_violation",
        "23502": "not_null_violation",
        "23503": "foreign_key_violation",
        "23505": "unique_violation",
        "23514": "check_violation",
        "23P01": "exclusion_violation",
    },
}


class SQLAlchemyExceptionParser:
    def __init__(self) -> None:
        self.exception_detail = None

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type in error_codes:
            exception_description = error_codes[exc_type][exc_val.orig.sqlstate]
            exception = [
                ExceptionDetail(
                    type=exception_description,
                    msg=exception_description.replace("_", " ").capitalize(),
                    # input=value,
                    # loc=[key]
                ).model_dump(mode="json")
                # for key, value in exc_val.params.items()
                # if key in exc_val.orig.pgresult.error_message.decode()
            ]
            self.exception_detail = exception
            return True
        return False
