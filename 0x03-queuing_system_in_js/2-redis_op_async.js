import redis from 'redis';
import { promisify} from 'util'

// create a Redis client
const client = redis.createClient();

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});


client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = async (schoolName, value)=>{
    const reply = await setAsync(schoolName, value);
    console.log(`Reply: ${reply}`)
}

const  displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName);
        // console.log(`Reply: ${reply}`);
        console.log(value);
    } catch (error) {

        console.error(error);
    }
}
// const executeAsncFunction = async()=>{
//     await displaySchoolValue('Holberton');
//     await displaySchoolValue('HolbertonSanFrancisco');
//     await setNewSchool('HolbertonSanFrancisco', '100');
// }
// executeAsncFunction();
 displaySchoolValue('Holberton');
 setNewSchool('HolbertonSanFrancisco', '100');
 displaySchoolValue('HolbertonSanFrancisco');