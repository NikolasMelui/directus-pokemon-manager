const fetch = require('node-fetch');

module.exports = function registerEndpoint(router, { services, exceptions }) {
  const { ItemsService } = services;
  const { ServiceUnavailableException } = exceptions;

  router.get('/:name', async (req, res, next) => {
    const recipeService = new ItemsService('pokemons', {
      schema: req.schema,
      accountability: req.accountability,
    });

    const { name } = req.params;

    try {
      const pokemon = (
        await recipeService.readByQuery({
          filter: { name },
        })
      ).pop();

      const { url } = pokemon;

      const response = await fetch(url);
      const result = await response.json();

      res.json(result);
    } catch (error) {
      return next(new ServiceUnavailableException(error.message));
    }
  });
};
