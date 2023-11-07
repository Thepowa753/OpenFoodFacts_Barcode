import requests
from dto.FoodDto import FoodDto


def openfoodfacts(barcode: str) -> FoodDto:
    response = requests.get(
        f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"
    )
    if response.status_code == 200:
        parsed = response.json().get("product")
        if parsed:
            return FoodDto(
                Barcode=barcode,
                Name=parsed.get("product_name"),
                Image=parsed.get("image_front_url"),
                Categories=parsed.get("categories"),
                EN_categories=parsed.get("categories_tags"),
                Ingredients=parsed.get("ingredients_text"),
                Packaging=parsed.get("packaging"),
            )
        else:
            return FoodDto(Barcode=barcode, Error="No barcode found...")
    else:
        return FoodDto(Barcode=barcode, Error="API returned errors...")


def main():
    parsedDTO = openfoodfacts(input("Enter a product barcode: "))
    print(parsedDTO)


if __name__ == "__main__":
    main()
