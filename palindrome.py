import json

def lambda_handler(event, context):
    print(event)
    numbers = event["numbers"]
    response = json.dumps({"palindrome": palindrom(numbers[0], numbers[1])})
    return {
        "statusCode": 200,
        "body": response,
    }


def palindrom(num, rev):
    try:
        temp = num
        if num == 0:
            return "Not valid for palindrome"
        else:
            while (num > 0):
                dig = num % 10
                rev = rev * 10 + dig
                num = num // 10
            if (temp == rev):
                return temp
            else:
                raise ValueError
    except ValueError:
        return "It is not a palindrome number"
