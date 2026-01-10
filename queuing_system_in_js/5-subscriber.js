import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Define the channel
const channel = 'holberton school channel';

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
  
  // Subscribe to the channel
  client.subscribe(channel);
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Handle message events
client.on('message', (receivedChannel, message) => {
  console.log(message);
  
  // If the message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
