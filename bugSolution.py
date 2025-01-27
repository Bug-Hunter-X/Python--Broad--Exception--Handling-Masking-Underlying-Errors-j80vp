def function_with_improved_error_handling(data):
    try:
        result = some_external_library_call(data)
        return result
    except SomeExternalLibraryException as e:
        log_error(f"Specific error from external library: {e}")
        # Consider returning an appropriate value instead of None
        return None 
    except ValueError as e:
        log_error(f"ValueError: {e}")
        raise  # Reraise for upper handling
    except TypeError as e:
        log_error(f"TypeError: {e}")
        raise # Reraise for upper handling
    except Exception as e:
        log_error(f"An unexpected error occurred: {e}")
        raise # Reraise for upper handling