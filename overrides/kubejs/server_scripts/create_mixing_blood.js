ServerEvents.recipes(event => {
    event.recipes.create.mixing(
        Fluid.of('biomesoplenty:blood', 100),
        'alexsmobs:blood_sac'
    )
})