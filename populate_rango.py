import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Recipe, FavouriteRecipe, UserProfile, User


def populate():

    BBQ_recipes = [
        {'title': 'Best Steak Marinade in Existence',
         'ingredients': """1/3 cup soy sauce.
1/2 cup olive oil.
1/3 cup fresh lemon juice.
1/4cup Worcestershire sauce.
1.5 tablespoons garlic powder.
3 tablespoons dried basil.
1.5 tablespoons dried parsley flakes.
1 teaspoon ground white pepper.
1/4 teaspoon hot pepper sauce (Optional).
1 teaspoon dried minced garlic (Optional).
         """,
         'directions': """
         Place the soy sauce, olive oil, lemon juice, Worcestershire sauce, garlic powder, basil, parsley, and pepper in a blender. Add hot pepper sauce and garlic, if desired. 
         Blend on high speed for 30 seconds until thoroughly mixed.Pour marinade over desired type of meat. Cover, and refrigerate for up to 8 hours. Cook meat as desired.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5968118.jpg&w=958&h=1274&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Summer Grilled Cabbage',
         'ingredients': """1 large head cabbage, cored and cut into 8 wedges
8 teaspoons butter
1/4 cup water
1/2 teaspoon garlic powder, or to taste
1/2 teaspoon seasoned salt, or to taste
ground black pepper to taste
""",
         'directions': """Preheat an outdoor grill for medium-high heat and lightly oil grate.
Arrange the cabbage wedges into the bottom of a large metal baking dish. Pour the water into the dish. Place a teaspoon of butter on each cabbage wedge. Season liberally with garlic powder, seasoned salt, and pepper. Cover the dish with aluminum foil.
Place the dish on the preheated grill; cook until cabbage is tender, about 30 minutes.""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F8711239.jpg&q=85',
         'likes': 26},
        {'title': 'Grilled Salmon',
         'ingredients': """
         1.5 pounds salmon fillets
         lemon pepper to taste
         garlic powder to taste
         salt to taste
         1/3 cup soy sauce
         1/3 cup brown sugar
         1/3 cup water
         1/4 cup vegetable oil
         """,
         'directions': """
         Season salmon fillets with lemon pepper, garlic powder, and salt.
         In a small bowl, stir together soy sauce, brown sugar, water, and vegetable oil until sugar is dissolved. Place fish in a large resealable plastic bag with the soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours.
         Preheat grill for medium heat.
         Lightly oil grill grate. Place salmon on the preheated grill, and discard marinade. Cook salmon for 6 to 8 minutes per side, or until the fish flakes easily with a fork.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4537394.jpg&w=958&h=958&c=sc&poi=face&q=85',
         'likes': 23}]

    Bread_recipes = [
        {'title': 'Strawberry Bread',
         'ingredients': """
2 cups fresh strawberries
3 cups all-purpose flour
2 cups white sugar
1 tablespoon ground cinnamon
1 teaspoon salt
1 teaspoon baking soda
1.25 cups vegetable oil
4 eggs, beaten
1.25 cups chopped pecans
         """,
         'directions': """
        Preheat oven to 350 degrees F (175 degrees C). Butter and flour two 9 x 5-inch loaf pans.
        Slice strawberries and place in medium-sized bowl. Sprinkle lightly with sugar, and set aside while preparing batter.
        Combine flour, sugar, cinnamon, salt and baking soda in large bowl; mix well. Blend oil and eggs into strawberries. Add strawberry mixture to flour mixture, blending until dry ingredients are just moistened. Stir in pecans. Divide batter into pans.
        Bake in preheated oven until a tester inserted in the center comes out clean, 45 to 50 minutes (test each loaf separately). Let cool in pans on wire rack for 10 minutes. Turn loaves out of pans, and allow to cool before slicing.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5470594.jpg&w=767&h=767&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Whole Wheat Beer Bread ',
         'ingredients': """1/2 cups all-purpose flour
1/2 cups whole wheat flour
1/2 teaspoons baking powder
1/2 teaspoons salt
1/3 cup packed brown sugar
1 (12 fluid ounce) can or bottle beer
""",
         'directions': """Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9x5 inch loaf pan.
In a large mixing bowl, combine all-purpose flour, whole wheat flour, baking powder, salt and brown sugar. Pour in beer, stir until a stiff batter is formed. It may be necessary to mix dough with your hands. Scrape dough into prepared loaf pan.
Bake in preheated oven for 50 to 60 minutes, until a toothpick inserted into center of the loaf comes out clean.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F128314.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Garlic Naan',
         'ingredients': """
        1/2 cup warm water
        1 teaspoon white sugar
        1 (.25 ounce) package active dry yeast
        For the Garlic Butter:
        1/4 cup butter
        2 cloves garlic, minced
        1/4 cup plain yogurt
        2 cups bread flour, or more as needed
        1 teaspoon kosher salt
        1/4 cup chopped cilantro (Optional)
         """,
         'directions': """
        Combine water, sugar, and yeast in a bowl. Let stand until yeast softens and forms a creamy foam, about 15 minutes.
        In the meantime, heat butter in a pan over medium heat until melted and sizzling. Quickly mix in garlic. Remove garlic butter from heat and set aside until ready to use.
        Add yogurt, bread flour, salt, and 1 tablespoon of the garlic butter to the yeast mixture. Stir with a wooden spoon until a shaggy dough forms. Knead by hand until dough pulls away from the sides of the bowl, adding more water or flour as needed. Turn dough out onto the counter and continue kneading into a smooth ball, 3 to 4 minutes.
        Place dough in a large bowl. Coat with a few more drizzles of garlic butter. Cover and let rise until doubled in volume, about 2 hours.
        Punch down dough and turn out onto the counter. Shape into a rough rectangle and cut into 6 pieces. Roll each piece into a ball and lightly dust with flour. Cover with plastic wrap and proof until slightly puffy, 15 to 20 minutes.
        Roll each piece into an oval about 1/8 inch thick. Sprinkle some cilantro on top and press lightly to adhere.
        Preheat a cast iron skillet until very, very hot, about 5 minutes. Cook each naan until large bubbles form, 1 to 2 minutes. Flip over, press gently, and cook until bubbles on the bottom are charred, 2 to 3 minutes more.
        Brush naan with more garlic butter before serving.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6599025.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Breakfast_and_Brunch_recipes = [
        {'title': 'Breakfast Cups',
         'ingredients': """cooking spray
18 refrigerated biscuits (unbaked)
8 ounces breakfast sausage
7 large eggs
1/2 cup milk
salt and ground black pepper to taste
1 cup mild shredded Cheddar cheese
         """,
         'directions': """
Preheat oven to 400 degrees F (200 degrees C). Grease 18 muffin cups with cooking spray.
Roll out biscuit dough on a lightly floured surface to form 5-inch rounds. Place each round in the prepared muffin cups, pressing into the base and sides to form a dough cup.
Cook and stir sausage in a skillet over medium-high heat until browned and cooked through, 5 to 10 minutes; drain fat. Spoon sausage into dough cups.
Whisk eggs, milk, salt, and pepper together in a bowl until well-beaten. Pour egg mixture into each dough cup, filling each just below the top of the biscuit dough. Sprinkle Cheddar cheese on top of egg mixture.
Bake in the preheated oven until eggs are set and biscuit dough is golden, 15 to 18 minutes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F1784092.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Easy Shakshuka',
         'ingredients': """1 tablespoon olive oil
2 cloves garlic, minced
1 onion, cut into 2 inch pieces
1 green bell pepper, cut into 2 inch pieces
1 (28 ounce) can whole peeled plum tomatoes with juice
1 teaspoon paprika, or to taste
2 slices pickled jalapeno pepper, finely chopped
4 eggs
4 (6 inch) pita bread (Optional)
""",
         'directions': """Heat the vegetable oil in a deep skillet over medium heat. Stir in the garlic, onion, and bell pepper; cook and stir until the onion has softened and turned translucent, about 5 minutes. Add the canned tomatoes, paprika and jalapenos; stir, using the back of a spoon to break up the tomatoes. Simmer for about 25 minutes.
Crack an egg into a small bowl, then gently slip the egg into the tomato sauce. Repeat with the remaining eggs. Cook the eggs until the whites are firm and the yolks have thickened but are not hard, 2 1/2 to 3 minutes. If the tomato sauce gets dry, add a few tablespoons of water. Remove the eggs with a slotted spoon, place onto a warm plate, and serve with the tomato sauce and pita bread.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F400925.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Lemon-Ricotta Cornmeal Waffles',
         'ingredients': """
        1 cup all-purpose flour
        1/2 cup cornmeal
        1/4 cup white sugar
        1/2 teaspoons baking powder
        1/2 teaspoon baking soda
        1/4 teaspoon salt
        3/4 cup half-and-half
        1/2cup ricotta cheese
        2 large eggs
        2 tablespoons melted butter
        1 teaspoon lemon extract
        cooking spray

         """,
         'directions': """
        Preheat a waffle iron according to manufacturer's instructions.
        Whisk flour, cornmeal, sugar, baking powder, baking soda, and salt together in a large mixing bowl.
        Whisk half-and-half, ricotta cheese, eggs, melted butter, and lemon extract together in a separate bowl until smooth. Pour into the flour mixture and mix until thoroughly combined.
        Coat the preheated waffle iron with cooking spray. Pour batter into waffle iron in batches and cook until crisp and golden brown and the iron stops steaming, about 5 minutes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6879705.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Desserts_recipes = [
        {'title': 'Strawberry-Rhubarb Buckle',
         'ingredients': """1/2 cups diced fresh rhubarb
 1/2 cups diced fresh strawberries
1/2 cup white sugar
1 tablespoon lemon juice
3 tablespoons water, divided
2 tablespoons cornstarch
         """,
         'directions': """
         Combine rhubarb, strawberries, 1/2 cup sugar, lemon juice and 1 tablespoon of water in a saucepan. Cook, covered, over medium-low heat, stirring occasionally until mixture begins to boil, about 5 minutes. Reduce heat to low.
        In a small bowl, stir together remaining 2 tablespoons of water with cornstarch until cornstarch is dissolved. Add mixture to the saucepan and continue cooking fruit until mixture begins to thicken, about 2 minutes. Remove from stove and set aside to cool.
        Preheat the oven to 350 degrees F (175 degrees C). Spray a 9-inch deep dish pie pan with non-stick cooking spray, and place on a baking sheet.
        Beat 1/2 cup of butter and 1/2 cup of sugar with an electric mixer in a bowl until light and fluffy. Beat in egg, vanilla extract, and yogurt. Add flour, baking powder, baking soda, and salt; mix until just combined. Spread 2/3 of the batter into the prepared pan. Pour strawberry-rhubarb filling on top of the batter. Spread remaining 1/3 of the batter in small mounds atop the filling. Set aside.
        Combine brown sugar, 1/4 cup flour, and 2 tablespoons of butter in a small bowl. Mix using a fork, a pastry blender, or your hands, until the mixture resembles coarse crumbs. Sprinkle on top of the batter and filling.
        Bake in the preheated oven until the cake topping is nicely browned, about 35 minutes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6614329.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'One Bowl Chocolate Cake III',
         'ingredients': """2 cups white sugar
3/4 cups all-purpose flour
3/4 cup unsweetened cocoa powder
1/2 teaspoons baking powder
1/2 teaspoons baking soda
1 teaspoon salt
2 eggs
1 cup milk
1/2 cup vegetable oil
2 teaspoons vanilla extract
1 cup boiling water
""",
         'directions': """Preheat oven to 350 degrees F (175 degrees C). Grease and flour two nine inch round pans.
In a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda and salt. Add the eggs, milk, oil and vanilla, mix for 2 minutes on medium speed of mixer. Stir in the boiling water last. Batter will be thin. Pour evenly into the prepared pans.
Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick. Cool in the pans for 10 minutes, then remove to a wire rack to cool completely.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4554958.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'The Best Lemon Bars',
         'ingredients': """
        1 cup butter, softened
        1/2 cup white sugar
        2 cups all-purpose flour
        4 eggs
        1/2 cups white sugar
        1/4 cup all-purpose flour
        2 lemons, juiced
         """,
         'directions': """
        Preheat oven to 350 degrees F (175 degrees C).
        In a medium bowl, blend together softened butter, 2 cups flour and 1/2 cup sugar. Press into the bottom of an ungreased 9x13 inch pan.
        Bake for 15 to 20 minutes in the preheated oven, or until firm and golden. In another bowl, whisk together the remaining 1 1/2 cups sugar and 1/4 cup flour. Whisk in the eggs and lemon juice. Pour over the baked crust.
        Bake for an additional 20 minutes in the preheated oven. The bars will firm up as they cool. For a festive tray, make another pan using limes instead of lemons and adding a drop of green food coloring to give a very pale green. After both pans have cooled, cut into uniform 2 inch squares and arrange in a checker board fashion.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F3598469.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Dinner_Recipes_recipes = [
        {'title': 'Chicken, Apple, and Brussels Sprout Sheet Pan Dinner',
         'ingredients': """2 cups Brussels sprouts, halved
1 red apple, cut into 1-inch cubes
1 (4 ounce) package pancetta
2 tablespoons olive oil, divided
1 teaspoon minced fresh rosemary
6 skinless, boneless chicken thighs
salt and ground black pepper to taste
         """,
         'directions': """
        Preheat the oven to 425 degrees F (220 degrees C).
        Toss Brussels sprouts, apple, and pancetta with 1 tablespoon olive oil and rosemary in a bowl. Spread into a single layer on a sheet pan.
        Leave space on the pan for the chicken thighs. Toss chicken with the remaining 1 tablespoon oil in the same bowl; place on the sheet pan. Sprinkle salt and pepper on top.
        Bake in the preheated oven, stirring the Brussels sprouts mixture every 15 minutes, until chicken is no longer pink in the center and the juices run clear, 40 to 45 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5078300.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Tennessee Meatloaf',
         'ingredients': """1/2 cup ketchup
1/4cup brown sugar
2 tablespoons cider vinegar
Meatloaf:
cooking spray
1 onion, chopped
1/2 green bell pepper, chopped
2 cloves garlic, minced
2 large eggs, lightly beaten
1 teaspoon dried thyme
1 teaspoon seasoned salt
1/2 teaspoon ground black pepper
2 teaspoons prepared mustard
2 teaspoons Worcestershire sauce
1/2 teaspoon hot pepper sauce (such as Tabasco®)
1/2 cup milk
2/3 cup quick cooking oats
1 pound ground beef
1/2 pound ground pork
1/2 pound ground veal
""",
         'directions': """Combine ketchup, brown sugar, and cider vinegar in a bowl; mix well.
Preheat oven to 350 degrees F (175 degrees C). Spray two 9x5-inch loaf pans with cooking spray or line with aluminum foil for easier cleanup (see Cook's Note).
Place onion and green pepper in covered microwave container and cook until softened, 1 to 2 minutes. Set aside to cool.
In large mixing bowl, combine garlic, eggs, thyme, seasoned salt, black pepper, mustard, Worcestershire sauce, hot sauce, milk, and oats. Mix well. Stir in cooked onion and green pepper. Add ground beef, pork, and veal. With gloved hands, work all ingredients together until completely mixed and uniform.
Divide meatloaf mixture in half and pat half of mixture into each prepared loaf pan. Brush loaves with half of the glaze; set remainder of glaze aside.
Bake in preheated oven for 50 minutes. Remove pans from oven; carefully drain fat. Brush loaves with remaining glaze. Return to oven and bake for 10 minutes more. Remove pans from oven and allow meatloaf to stand for 15 minutes before slicing.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F1092268.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Tasty Baked Mac n Cheese',
         'ingredients': """
        1 (16 ounce) package elbow macaroni
        1/2 teaspoon salt
        3/4 cup butter, softened - divided
        1 cup sour cream
        1 tablespoon cream cheese, softened
        1 (8 ounce) package shredded sharp Cheddar cheese
        1 egg yolk
        2 tablespoons all-purpose flour
        1/2 teaspoon salt
        1/2 teaspoon ground cayenne pepper
        1 cup milk
        1 (8 ounce) package shredded mild Cheddar cheese
         """,
         'directions': """
        Preheat oven to 375 degrees F (190 degrees C). Line a 9x13-inch baking dish with parchment paper.
        Bring a large pot of water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally until almost cooked through and firm to the bite, about 7 minutes. Drain and transfer to a large bowl. Sprinkle macaroni with 1/2 teaspoon salt and stir 1/2 cup butter into the pasta.
        Mix 1/4 cup butter, sour cream, cream cheese, sharp Cheddar cheese, and egg yolk together in a bowl. Stir flour, 1/2 teaspoon salt, cayenne pepper, and milk into the sour cream mixture.
        Spread 1/4 cup sour cream sauce over bottom of prepared baking dish. Stir remaining sour cream sauce into macaroni. Pour macaroni into baking dish atop sauce layer; sprinkle mild Cheddar cheese over the casserole.
        Bake in the preheated oven until heated through and cheese topping has melted, about 15 minutes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6100203.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Everyday_Cooking_recipes = [
        {'title': 'Stove Pot Roast With Mashed Potatoes',
         'ingredients': """Pot Roast:
1 (3 pound) beef chuck roast
salt and ground black pepper to taste
4 (10.5 ounce) cans condensed beef broth (such as Campbell's®)
1 cup water
1 white onion, cut into large wedges
5 cloves garlic
1 (16 ounce) package carrots, peeled
1 sprig fresh rosemary
Mashed Potatoes:
5 pounds Yukon Gold potatoes, peeled and diced
1 (12 ounce) can evaporated milk, or as needed
1/2 cup butter
salt to taste
         """,
         'directions': """
        Season chuck roast with salt and black pepper; sear in a large, deep skillet or Dutch oven over medium heat until browned, about 10 minutes per side.
        Pour beef broth and water into the skillet with roast. Arrange onion wedges and garlic cloves around the meat. Spread carrots atop roast and place sprig of rosemary atop carrots. Turn heat to medium-low and simmer until tender, about 6 hours.
        Cover potatoes with water in a large pot and bring to a boil; reduce heat to low and simmer until tender, about 30 minutes. Drain. Mash potatoes with butter and half the evaporated milk until smooth; slowly mash remaining evaporated milk into potatoes to achieve the desired consistency. Season with salt.
        Remove 1 or 2 cloves of garlic from skillet and mash cloves on top of the roast; serve with mashed potatoes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F949315.jpg&w=330&h=330&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Instant Pot® Chicken and Dumplings',
         'ingredients': """1/2 tablespoon olive oil
1 cup diced onion
1/2 cup diced carrot
1/2 cup diced celery
1 bay leaf
4 cups low-sodium chicken broth
1 pound boneless, skinless chicken thighs
1 pound bone-in chicken breasts, skin removed
1/2 teaspoon thyme (Optional)
1/2 teaspoon dried marjoram
1 teaspoon salt (Optional)
1/4 teaspoon freshly ground black pepper
2 tablespoons unsalted butter, softened
2 tablespoons all-purpose flour
salt and ground black pepper to taste (Optional)
1/2 cup frozen petite peas
1/2 cup frozen cut green beans
Dumplings:
1 cup all-purpose flour
1 teaspoon baking powder
1/2 teaspoon salt (Optional)
2 tablespoons cold unsalted butter
1 tablespoon chopped fresh flat-leaf parsley
1/2 cup buttermilk
""",
         'directions': """Pour the olive oil into a multi-functional pressure cooker (such as an Instant Pot®) and select the Saute function. Cook onion, carrot, celery, and bay leaf until the vegetables are soft and the onion has turned translucent, about 5 minutes.
Add chicken broth, chicken thighs, chicken breasts, thyme, marjoram, salt, and pepper. Close and lock the lid. Select high pressure according to manufacturer's instructions; set timer for 9 minutes. Allow 10 to 15 minutes for pressure to build.
Release pressure carefully using the quick-release method according to manufacturer's instructions, about 5 minutes. Carefully remove the chicken pieces with tongs and place them in a bowl to cool slightly; discard bay leaf.
Mash butter with the flour to make a smooth paste; set aside.
Combine flour, baking powder, and salt in a bowl for the dumplings. Cut in cold butter until mixture is the texture of cornmeal. Stir in parsley and set aside.
Shred cooled chicken and return to the pot. Taste the broth and adjust the seasoning if needed. Add peas and green beans. Stir in the flour-butter paste. Select Saute function to bring broth back to a boil.
Pour buttermilk into the dumpling mixture and stir until combined. Drop the dumpling dough by heaping spoonfuls on top of the stew; a small cookie scoop works well.
Cover pot with the lid, leaving the steam vent open. Select Slow Cooker function and simmer on Low, covered, until dumplings are cooked through, 10 to 12 minutes. A skewer inserted in the center of a dumpling should come out clean.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F7242436.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Taco Meat',
         'ingredients': """
        1 pound lean ground beef
        1/2 teaspoon onion powder
        1/2 teaspoon garlic salt
        1/2 teaspoon celery salt
        1/2 teaspoon ground cumin
        1 (8 ounce) can tomato sauce, or more to taste
         """,
         'directions': """
        Heat a large skillet over medium-high heat. Cook and stir beef in the hot skillet until browned and crumbly, 5 to 7 minutes.
        Season beef with onion powder, garlic salt, celery salt, and cumin. Pour tomato sauce over the beef, stir to coat, and simmer until thickened, slightly, about 5 minutes.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5281437.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Lunch_Recipes_recipes = [
        {'title': 'Virgina Tuna Salad',
         'ingredients': """1 egg
1 (5 ounce) can tuna, drained and flaked
3 tablespoons mayonnaise
2 stalks celery, chopped
2 tablespoons sweet pickle relish
1 pinch ground black pepper
         """,
         'directions': """
         Place egg in a saucepan and cover with cold water. Bring water to a boil and immediately remove from heat. Cover and let egg stand in hot water for 10 to 12 minutes. Remove from hot water; cool for 5 minutes. Peel and chop into bite-sized pieces.
        In a medium bowl, mix together tuna and mayonnaise. Mix in egg, celery, relish, and black pepper.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F44694.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Spicy Grilled Cheese Sandwich',
         'ingredients': """2 tablespoons butter or margarine
4 slices white bread
2 slices American cheese
1 roma (plum) tomato, thinly sliced
1/4 small onion, chopped
1 jalapeno pepper, chopped
""",
         'directions': """Heat a large skillet over low heat. Spread butter or margarine onto one side of two slices of bread. Place both pieces buttered side down in the skillet. Lay a slice of cheese on each one, and top with slices of tomato, onion and jalapeno. Butter one side of the remaining slices of bread, and place on top buttered side up. When the bottom of the sandwiches are toasted, flip and fry until brown on the other side.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5434462.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Chicago-Inspired Italian Beef Sandwich',
         'ingredients': """
        1/2 pounds boneless beef chuck, cut into 2-inch pieces
        salt and ground black pepper to taste
        1 tablespoon vegetable oil
        6 cloves garlic, sliced
        2 tablespoons white vinegar
        1 tablespoon dried oregano
        1/2 teaspoons salt, or to taste
        1 teaspoon dried thyme
        1 teaspoon dried rosemary
        1 teaspoon freshly ground black pepper
        1 bay leaf
        1/4 teaspoon red pepper flakes, or to taste
        3 cups chicken broth, or as needed
        4 ciabatta rolls, sliced in half
        1 cup chopped giardiniera (pickled Italian vegetables)
        2 teaspoons chopped fresh flat-leaf parsley
         """,
         'directions': """
        Season beef with a pinch of salt and black pepper. Heat vegetable oil in a heavy pot over high heat. Cook and stir beef in hot oil until browned, 5 to 8 minutes.
        Stir garlic, vinegar, oregano, 1 1/2 teaspoons salt, thyme, rosemary, 1 teaspoon black pepper, bay leaf, and red pepper flakes into beef. Pour enough chicken broth into beef mixture to cover the meat by 1 inch and bring to a simmer.
        Cover pot with a lid, reduce heat to low, and simmer until meat is fork-tender, 1 to 1 1/2 hours.
        Transfer meat with a strainer or slotted spoon to a separate pot; pour about 1/4 cup of meat broth into pot. Use a wooden spoon to gently break meat into smaller chunks. Cover pot with a lid or aluminum foil and keep warm.
        Skim excess grease from top of broth remaining in the first pot; season with salt and pepper to taste. Cover pot with a lid or aluminum foil and keep broth warm.
        Lay halves of a roll out on a work surface and spoon 2 to 3 tablespoons meat broth over each half. Top bottom half of roll with a generous portion of meat and a spoonful of pickled vegetables. Place tops on sandwich. Repeat with remaining buns, broth, meat, and pickled vegetables to make 3 more sandwiches.
        Spoon hot meat broth into ramekins and top each ramekin with 1/2 teaspoon parsley. Serve sandwiches with hot broth for dipping.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F1100724.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    Main_Dishes_recipes = [
        {'title': 'Cardamom Maple Salmon',
         'ingredients': """1/2 teaspoons salt
1 teaspoon paprika
1 teaspoon ground cardamom
1 teaspoon ground coriander
1/2 easpoon ground black pepper
1/4 cup grapeseed oil
2 tablespoons maple syrup
1 (2 pound) salmon fillet, cut into 3-inch pieces
         """,
         'directions': """
        Stir salt, paprika, cardamom, coriander, and black pepper together in a bowl. Add oil and maple syrup and stir until evenly combined.
        Preheat a non-stick frying pan over medium-high heat, about 350 degrees F (175 degrees C).
        Dredge salmon pieces through the maple syrup mixture until evenly coated on all sides.
        Cook salmon in the preheated pan until fish flakes easily with a fork, 5 to 7 minutes per side
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F1122494.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Spicy Pork Tenderloin with Apples and Sweet Potatoes',
         'ingredients': """cooking spray
1 tablespoon ground ginger
1 tablespoon light brown sugar
1 teaspoon chipotle chili powder, or to taste
salt and ground black pepper to taste
2 (1 1/2 pound) pork tenderloins
4 apples, peeled and cut into 8 pieces each
1 large sweet potato, peeled and cut into 1 1/2-inch pieces
4 tablespoons butter, cut into small pieces
1/2 cups apple cider
1 lime, juiced
1/2 teaspoon granulated garlic
1/2 teaspoon ground ginger
1/8 teaspoon chipotle chile powder
1/8 teaspoon garam masala
salt and ground black pepper to taste
aluminum foil
""",
         'directions': """Preheat the oven to 425 degrees F (220 degrees C). Spray a 9x13-inch baking dish with cooking spray.
Mix together 1 tablespoon ginger, brown sugar, 1 teaspoon chili powder, salt, and pepper in a bowl to create a rub. Rub combined seasonings on all sides of the pork tenderloins, using the entire amount.
Place apples and sweet potatoes in the bottom of the prepared pan; dot with butter.
Mix together apple cider, lime juice, garlic, 1/2 teaspoon ginger, 1/8 teaspoon chili powder, garam masala, salt, and pepper in a bowl. Pour over apples and sweet potatoes and place tenderloins on top.
Bake in the preheated oven for 20 minutes. Ladle cooking liquid over apples and sweet potatoes, turn tenderloins over, and continue baking until pork is slightly pink at the center, about 20 minutes longer. A meat thermometer placed in the center of the thickest tenderloin should read 145 degrees F (63 degrees C).
Remove apples and sweet potatoes to a serving platter using a slotted spoon. Place tenderloins on top and cover with aluminum foil.
Pour cooking liquid from the baking dish into a 1-quart saucepan. Heat over medium-high heat until liquid comes to a boil. Boil, stirring occasionally, until the mixture is reduced by one half, 10 to 15 minutes.
Drizzle sauce over pork, apples, and sweet potatoes. Slice tenderloins and serve.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F7251995.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Als Burmese Chicken Curry',
         'ingredients': """
        1 teaspoon butter, or as needed
        8 shallots, thinly sliced
        3 tablespoons red curry paste, or more to taste
        2 tablespoons hot curry powder
        1 tablespoon ground red chile pepper
        1/2 pounds chicken thighs
        1 lemongrass, smashed and cut into 1-inch pieces
        10 bird's eye chile peppers, chopped, or to taste
        1 tablespoon ground coriander
        2 kaffir lime leaves, or to taste
        3 tablespoons fish sauce
        water to cover
        1 (14 ounce) can coconut milk
        4 tomatoes, quartered
        1/2 small bunch fresh cilantro, chopped, or to taste
         """,
         'directions': """
        Melt butter in a wok over medium heat. Add shallots and fry until golden, about 10 minutes. Remove shallots and set aside. Add curry paste to the wok and toast until fragrant, about 3 minutes. Stir in curry powder and ground chile. Add chicken and cook, stirring, until lightly browned, about 5 minutes. Stir in lemongrass, chiles peppers, coriander, and lime leaves.
        Pour in fish sauce and enough water to cover chicken. Add coconut milk; cook for 10 minutes. Toss in tomatoes and cook until starting to soften, about 10 minutes more. Reduce heat to low and simmer until flavors blend, 2 to 3 hours.
        Remove lemongrass and lime leaves. Garnish curry with the fried shallots and cilantro.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F7062050.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'likes': 20},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'likes': 50},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'likes': 18}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'likes': 15},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'likes': 10}]

    cats = {'BBQ': {'recipes': BBQ_recipes,  'likes': 64},
            'Bread': {'recipes': Bread_recipes, 'likes': 32},
            'Breakfast and Brunch': {'recipes': Breakfast_and_Brunch_recipes,  'likes': 16},
            'Desserts': {'recipes': Desserts_recipes, 'likes': 32},
            'Dinner': {'recipes': Dinner_Recipes_recipes, 'likes': 32},
            'Everyday Cooking': {'recipes': Everyday_Cooking_recipes, 'likes': 32},
            'Lunch': {'recipes': Lunch_Recipes_recipes, 'likes': 32},
            'Main Dishes': {'recipes': Main_Dishes_recipes, 'likes': 32},
            }

    # favs = {'user': 'mockusername', 'recipe': 'Best Steak Marinade in Existence'}

    for cat, cat_data in cats.items():
        c = add_cat(cat, likes=cat_data['likes'])
        for r in cat_data['recipes']:
            add_recipe(c, r['title'], r['ingredients'], r['directions'], r['url'], likes=r['likes'])

    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            print(f'- {c}: {r}')

    # add_user_profile()
    # create_favourite_recipe()

    # add_to_favourite_recipe(favs['user'], favs['title'])


def add_recipe(cat, title, ingredients, directions, url, likes=0):
    r = Recipe.objects.get_or_create(category=cat, title=title)[0]
    r.ingredients = ingredients
    r.directions = directions
    r.url = url
    r.likes = likes
    r.save()
    return r


def add_cat(name, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.save()
    return c


# def add_user_profile():
#     user = User.objects.get(id=1)
#     up = UserProfile.objects.create(user=user)
#     up.save()

def create_favourite_recipe():
    user = User.objects.get(id=1)
    user_profile = UserProfile.objects.get(user=user)
    favourite_recipe = FavouriteRecipe.objects.get_or_create(user=user_profile)[
        0]
    recipe = Recipe.objects.get(id=12)
    recipe.favouriteRecipe.add(favourite_recipe)


# def add_to_favourite_recipe(username, title):
#     r = Recipe.objects.get_or_create(title=title)[0]
#     u = User.objects.get_or_create(username=username)[0]
#     up = UserProfile.objects.get_or_create(user=u)[0]
#     f = FavouriteRecipe.objects.get_or_create(user=up)[0]
#     r.favouriteRecipe = f
#
#     return f


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
