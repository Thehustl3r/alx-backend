import kue from 'kue'

const queue = kue.createQueue({name: 'push_notification_code'});

// Object containing  job data
const jobData = {
    phoneNumber: '+2507885545',
    message: 'Hello, world!'
}


const job = queue.create('push_notification_code',jobData);
job.save((err)=>{
    if (err){
        console.error('Notification job failed')
    }
    console.log(`Notification job created: ${job.id}`);

    // handle job completed
    job.on('complete', ()=>{
    console.log('Notification job completed');
});

})

job.on('failed', ()=> {
    console.log('Notification job failed');
});

const sendNotification = (phoneNumber, message) =>{
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
queue.process('push_notification_code', (job, done)=>{
    const {phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message);
    done();
})