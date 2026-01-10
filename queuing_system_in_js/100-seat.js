import express from "express";
import redis from "redis";
import { promisify } from "util";
import kue from "kue";

// Create Express server
const app = express();
const port = 1245;

// Create Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Kue queue
const queue = kue.createQueue();

// Initialize variables
let reservationEnabled = true;

// Redis functions
async function reserveSeat(number) {
  return await setAsync("available_seats", number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync("available_seats");
  return seats;
}

// Set initial available seats
(async () => {
  await reserveSeat(50);
})();

// Express routes
app.get("/available_seats", async (_req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get("/reserve_seat", (_req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservation are blocked" });
  }

  const job = queue.create("reserve_seat", {}).save((err) => {
    if (err) {
      return res.json({ status: "Reservation failed" });
    }
    res.json({ status: "Reservation in process" });
  });

  job.on("complete", () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on("failed", (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get("/process", async (_req, res) => {
  res.json({ status: "Queue processing" });

  queue.process("reserve_seat", async (_job, done) => {
    try {
      // Get current available seats
      const currentSeats = parseInt(await getCurrentAvailableSeats());

      // Check if seats are available
      if (currentSeats <= 0) {
        done(new Error("Not enough seats available"));
        return;
      }

      // Reserve a seat
      const newAvailableSeats = currentSeats - 1;
      await reserveSeat(newAvailableSeats);

      // If no more seats, disable reservations
      if (newAvailableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (error) {
      done(error);
    }
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
