import redis from 'redis'

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', ()=>{
    console.log('Redis client connected to the server');
});

// Event lister for connection Error
client.on('error', (err)=>{
    console.log(`Redis client not connected to the server: ${err}`);
});

//  Function to create a hash with specified values
const createHash = ()=>{
    client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}
const displayHash = ()=>{
    client.hgetall('HolbertonSchools', (err, reply)=>{
        if (err) {
            console.log(`Error retrieving hash: ${err}`);
            return;
        }
        console.log(reply);
    });
}
createHash();
displayHash();