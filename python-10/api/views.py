from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def lambda_function(request):
    numbers = request.data['question']

    occurrences = calc_occurrences(numbers)

    ordered = order_by_occurrence(occurrences)

    response = generate_response(ordered)

    data = {'solution': response}

    return Response(data=data, status=status.HTTP_200_OK)


def generate_response(ordered):
    response = []
    for num, occurrence in ordered.items():
        response += [num] * occurrence
    return response


def order_by_occurrence(occurrences):
    ordered = {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1], reverse=True)}
    return ordered


def calc_occurrences(numbers):
    solution = dict()
    for num in numbers:
        occurrences = numbers.count(num)
        solution[num] = occurrences
    return solution
