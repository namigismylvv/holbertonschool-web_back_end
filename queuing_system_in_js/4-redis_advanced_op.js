import redis from "redis";

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on("connect", () => {
  console.log("Redis client connected to the server");

  // Create the hash
  createHash();

  // Display the hash
  displayHash();
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to create a hash in Redis
function createHash() {
  // Define the hash key
  const hashKey = "HolbertonSchools";

  // Delete the hash if it exists
  client.del(hashKey, (err) => {
    if (err) {
      console.error(err);
      return;
    }

    // Store hash values
    client.hset(hashKey, "Portland", "50", redis.print);
    client.hset(hashKey, "Seattle", "80", redis.print);
    client.hset(hashKey, "New York", "20", redis.print);
    client.hset(hashKey, "Bogota", "20", redis.print);
    client.hset(hashKey, "Cali", "40", redis.print);
    client.hset(hashKey, "Paris", "2", redis.print);
  });
}

// Function to display a hash from Redis
function displayHash() {
  // Define the hash key
  const hashKey = "HolbertonSchools";

  // Get all hash values
  client.hgetall(hashKey, (err, object) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(object);
  });
}
