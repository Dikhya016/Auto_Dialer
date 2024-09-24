
from twilio.rest import Client
import threading
import time,datetime
from contacts.models import CallRecords

def make_call(account_sid, auth_token,name, from_, to, twiml,uid):
    client = Client(account_sid, auth_token)
    try:
        call = client.calls.create(
            twiml=twiml,
            to=to,
            from_=from_
        )
        call_result=0
        while True:
            call = client.calls(call.sid).fetch()
            if call.status == 'completed':
                print("Call completed. (User answered)")
                call_result=1
                break
            elif call.status == 'busy':
                print('User rejected the call')
                call_result=2
                break
            elif call.status == 'no-answer':
                print('User did not pick up the call')
                call_result=3
                break
            else:
                print(f"Current call status: {call.status}")
                time.sleep(5)  # Wait for 5 seconds before polling again

        # Fetch the call details again after completion
        call = client.calls(call.sid).fetch()

        call_time_stamp=call.start_time+datetime.timedelta(minutes=330)  # convert to IST from UTC
        call_dict={
            1: "Answered",
            2: "Rejected / Busy",
            3: "Unanswered"
        }
        record=CallRecords(user_id=uid,username=name,call_timestamp=call_time_stamp,duration=call.duration,phonenum=to,call_cost=str(call.price)+call.price_unit,call_result=call_dict[call_result])
        record.save()

    except Exception as e:
        print("An error occurred:", e)

def dial_all(uid,msg,phs):

    account_sid = 'add your twilio sid'
    auth_token = 'add your auth_token'
    from_number = 'add your twilio no.'
   
    twiml = '<Response><Say voice="woman">'+msg+'</Say></Response>'

    threads = []
    for name,to_number in phs.items():
        thread = threading.Thread(target=make_call, args=(account_sid, auth_token,name, from_number, to_number, twiml,uid))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
