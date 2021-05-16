module.exports = function registerEndpoint(router) {
	router.get('/', (req, res) => res.send('Hello, World!'));
	router.get('/new', (req, res) => res.send('New endpoint!'));
};