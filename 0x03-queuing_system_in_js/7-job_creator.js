import kue from 'kue';

// Create queues named push_notification_code and push_notification_code_2
const queue = kue.createQueue({
  redis: {
    // Configure your Redis connection details here if needed
  },
  name: 'push_notification_code_2',
});

// Array containing notification data
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];
  // Blacklist array
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0); // Track initial progress
  
    if (blacklistedNumbers.includes(phoneNumber)) {
      const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
      return done(err);
    }
  
    job.progress(50); // Track progress after blacklist check
  
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
    // Simulate processing (replace with your actual notification sending logic)
    setTimeout(() => {
      job.progress(100); // Track complete progress
      done();
    }, 1000); // Simulate 1 second processing time
  }
// Function to create a notification job
function createNotificationJob(queue, jobData) {
  const job = queue.create('push_notification_code_2', jobData);

  job.save((err) => {
    if (err) {
      console.error(`Notification job failed: ${err.message}`);
      return;
    }
    console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.error(`Notification job ${job.id} failed: ${err.message}`);
  });

  // Track job progress (implementation depends on your job processing logic)
  // This part is for demonstration purposes only and might require additional configuration
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
}

// Loop through jobs array and create jobs
jobs.forEach((jobData) => {
  createNotificationJob(queue, jobData);
});
