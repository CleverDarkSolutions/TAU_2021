const request = require('supertest');
const app = require('../server');

describe('Item API', () => {
  let itemId;

  test('should create a new item', async () => {
    const res = await request(app)
      .post('/items')
      .send({ name: 'Item 1', price: 10.99 });

    expect(res.statusCode).toBe(201);
    expect(res.body.name).toBe('Item 1');
    expect(res.body.price).toBe(10.99);

    itemId = res.body.id;
  });

  test('should get all items', async () => {
    const res = await request(app).get('/items');

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveLength(1);
    expect(res.body[0].name).toBe('Item 1');
    expect(res.body[0].price).toBe(10.99);
  });

  test('should get a single item', async () => {
    const res = await request(app).get(`/items/${itemId}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Item 1');
    expect(res.body.price).toBe(10.99);
  });

  test('should update an item', async () => {
    const res = await request(app)
      .put(`/items/${itemId}`)
      .send({ name: 'Updated Item', price: 15.99 });

    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Updated Item');
    expect(res.body.price).toBe(15.99);
  });

  test('should delete an item', async () => {
    const res = await request(app).delete(`/items/${itemId}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Updated Item');
    expect(res.body.price).toBe(15.99);
  });

  test('should return 404 for a non-existent item', async () => {
    const res = await request(app).get(`/items/${itemId}`);

    expect(res.statusCode).toBe(404);
    expect(res.body.message).toBe('Item not found');
  });
});