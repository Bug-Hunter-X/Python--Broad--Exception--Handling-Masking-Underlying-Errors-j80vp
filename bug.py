def function_with_uncommon_error(data):
    try:
        result = some_external_library_call(data)
        return result
    except SomeExternalLibraryException as e:
        # Handle this specific exception
        log_error(f"Error from external library: {e}")
        return None
    except Exception as e:
        # This is too broad and might mask other issues
        raise  # Re-raise the exception for higher level handling