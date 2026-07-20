from typing import List

from _recipe_utils import Recipe

# Define the categories display order, optional
categories_sort: List[str] = ["News", "Magazines", "Online Magazines"]

recipes: List[Recipe] = [
    # ------------------- Indian -------------------
    Recipe(
        recipe="the-hindu",
        slug="the-hindu",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        tags=["india"],
        # daily, mornings IST
        enable_on=onlyat_hours(list(range(5, 12)), 5.5),
    ),
    Recipe(
        recipe="indian-express",
        slug="indian-express",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        tags=["india"],
        enable_on=onlyat_hours(list(range(5, 12)), 5.5),
    ),
    Recipe(
        recipe="deccan-herald",
        slug="deccan-herald",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        tags=["india", "bangalore"],
        enable_on=onlyat_hours(list(range(5, 12)), 5.5),
    ),
    Recipe(
        recipe="frontline",
        slug="frontline",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        tags=["india"],
        # fortnightly magazine — checking once a week (Saturdays) is plenty
        enable_on=onlyon_weekdays([5], 5.5),
    ),
    # ---------------- International (free, ship with newsrack) ----------------
    Recipe(
        recipe="guardian",
        slug="guardian",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
    ),
    Recipe(
        recipe="thediplomat",
        name="The Diplomat",
        slug="the-diplomat",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["asia"],
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], 5.5),
    ),
    Recipe(
        recipe="thirdpole",
        slug="thirdpole",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["asia", "climate"],
        enable_on=onlyat_hours(list(range(5, 20)), 5.5),
    ),
    Recipe(
        recipe="restofworld",
        slug="restofworld",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["technology"],
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], 5.5),
    ),
    Recipe(
        recipe="mit-tech-review",
        slug="mit-tech-review-feed",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["technology"],
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], 5.5),
    ),
    Recipe(
        recipe="quanta-magazine",
        slug="quanta-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["science"],
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4], 5.5),
    ),
    Recipe(
        recipe="lithub",
        slug="lithub",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        tags=["literature", "books"],
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4], 5.5),
    ),
]
