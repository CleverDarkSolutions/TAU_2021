const express = require('express');
const asyncHandler = require('express-async-handler');
const supertest = require('supertest');
const { Pool } = require('pg');

const app = express();
const PORT = 3000;

// PostgreSQL connection
const pool = new Pool({
  user: 'your_postgres_username',
  password: 'your_postgres_password',
  host: 'your_postgres_host',
  port: 5432,
  database: 'your_postgres_database',
});

// Middleware to parse JSON
app.use(express.json());

// GET all items
app.get('/items', asyncHandler(async (req, res) => {
  const client = await pool.connect();
  const result = await client.query('SELECT * FROM items');
  const data = result.rows;
  client.release();
  res.json(data);
}));

// GET single item
app.get('/items/:id', asyncHandler(async (req, res) => {
  const { id } = req.params;
  const client = await pool.connect();
  const result = await client.query('SELECT * FROM items WHERE id = $1', [id]);
  const data = result.rows[0];
  client.release();
  if (data) {
    res.json(data);
  } else {
    res.status(404).json({ message: 'Item not found' });
  }
}));

// POST create item
app.post('/items', asyncHandler(async (req, res) => {
  const { name, price } = req.body;
  const client = await pool.connect();
  const result = await client.query('INSERT INTO items (name, price) VALUES ($1, $2) RETURNING *', [name, price]);
  const createdItem = result.rows[0];
  client.release();
  res.status(201).json(createdItem);
}));

// PUT update item
app.put('/items/:id', asyncHandler(async (req, res) => {
  const { id } = req.params;
  const { name, price } = req.body;
  const client = await pool.connect();
  const result = await client.query('UPDATE items SET name = $1, price = $2 WHERE id = $3 RETURNING *', [name, price, id]);
  const updatedItem = result.rows[0];
  client.release();
  if (updatedItem) {
    res.json(updatedItem);
  } else {
    res.status(404).json({ message: 'Item not found' });
  }
}));

// DELETE item
app.delete('/items/:id', asyncHandler(async (req, res) => {
  const { id } = req.params;
  const client = await pool.connect();
  const result = await client.query('DELETE FROM items WHERE id = $1 RETURNING *', [id]);
  const deletedItem = result.rows[0];
  client.release();
  if (deletedItem) {
    res.json(deletedItem);
  } else {
    res.status(404).json({ message: 'Item not found' });
  }
}));

// Start the server
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

module.exports = app;
