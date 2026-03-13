def list_roman_emperors(*args, **kwargs):
    successful = []
    unsuccessful = []
    for emperors, status in args:
        if emperors in kwargs:
            years = kwargs[emperors]
            if status:
                successful.append((emperors, years))
            else:
                unsuccessful.append((emperors, years))

    successful.sort(key=lambda x: (-x[1], x[0]))
    unsuccessful.sort(key=lambda x: (x[1], x[0]))

    result = []
    result.append(f"Total number of emperors: {len(args)}")

    if successful:
        result.append("Successful emperors:")
        for name, years in successful:
            result.append(f"****{name}: {years}")

    if unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, years in unsuccessful:
            result.append(f"****{name}: {years}")

    return "\n".join(result)