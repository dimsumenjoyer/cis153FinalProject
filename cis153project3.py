'''
Victor Van
00319912
CIS153: Project 3
11/1/2023, Due: 11/22/2023
'''

#example = {(requester, resource): number_of_accessed} 

import re

def parse_lines():
    with open("access_log.txt", "r") as file:
        find_requester_time_resource = "^(\S+) - - \[.+\] \"[A-Z]+ (\S+) "
        requester_time_resource = {}
        requesters = {} # {requester : number of requests they made}
        resources = {} # {resource : number of requests for each resource}
        for line in file:
            find_stuff = re.compile(find_requester_time_resource)
            stuff = find_stuff.findall(line)
            if len(stuff) > 0:
                requester, resource = stuff[0]
                if stuff[0] in requester_time_resource:
                    requester_time_resource[stuff[0]] += 1
                else:
                    requester_time_resource[stuff[0]] = 1
                if requester in requesters:
                    requesters[requester] += 1
                else:
                    requesters[requester] = 1
                if resource in resources:
                    resources[resource] += 1
                else:
                    resources[resource] = 1
        return requester_time_resource, requesters, resources

def find_most_requested_resource(resources):
    if resources:
        most_requested_resource = max(resources, key = resources.get)
        return most_requested_resource, resources[most_requested_resource]
    else:
        return None

def find_most_active_requester(requesters):
    if requesters:
        most_requester = max(requesters, key = requesters.get)
        return most_requester, requesters[most_requester]
    else:
        return None

def find_requester_of_most_accessed_resource(requester_time_resource, most_accessed_resource):
    most_requests = 0
    most_requester = None
    for (requester, resource), requests in requester_time_resource.items():
        if resource == most_accessed_resource and requests > most_requests:
            most_requests = requests
            most_requester = requester
    return most_requester, most_requests

def find_requester_resource():
    requester_time_resource, requesters, resources = parse_lines()
    most_resource, request_count_of_most_requested_resource = find_most_requested_resource(resources)
    requester_of_most_accessed_resource, requests = find_requester_of_most_accessed_resource(requester_time_resource, most_resource)
    most_requester, request_count_from_most_requester = find_most_active_requester(requesters)
    print(f"Requester with most requests: {most_requester} - {request_count_from_most_requester} requests.")
    print(f"Top requester of most requested resource: {requester_of_most_accessed_resource} - {requests} requests.")
    print(f"Most requested resource: {most_resource} - {request_count_of_most_requested_resource} total requests.")
    return

find_requester_resource()