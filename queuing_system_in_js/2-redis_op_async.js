import redis from "redis";
import { promisify } from "util";

// Create Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Handle connection events
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis using async/await
async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log("Reply: OK");
}

// Function to display the value for a school using async/await
async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

// Main function to run all operations
async function main() {
  await displaySchoolValue("Holberton");
  await setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");

  // Close the Redis connection
  client.quit();
}

// Execute the main function
main();
