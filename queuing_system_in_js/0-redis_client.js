import { createClient } from "redis";

// Create Redis client
const client = createClient();

// Handle connection events
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Connect to the Redis server
client.connect().catch(console.error);
