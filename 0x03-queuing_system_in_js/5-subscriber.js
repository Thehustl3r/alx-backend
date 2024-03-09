import redis from 'redis'

// Create a Redis client
const subscriber = redis.createClient();

// Event listener for successful connection
subscriber.on('connect', ()=>{
    console.log('Redis client connected to the server');
});

// Event lister for connection Error
subscriber.on('error', (err)=>{
    console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the 'holberton school channell'
subscriber.subscribe('holberton school channel');

// Event listener for messages received on the channel
subscriber.on('message', (channel, message)=>{
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});