# Kelly Dimick
# 10/24/2026
# 7.2 Assignment

def city_country(city, country, population=None, language=None):
    """Return a city and country with optional population and language."""
    result = f"{city.title()}, {country.title()}"
    if population is not None:
        result += f" - population {population}"
    if language is not None:
        result += f", {language.title()}"
    return result


if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("auckland", "new zealand", 1_463_000))
    print(city_country("sao paulo", "brazil", 12_330_000, "portuguese"))
