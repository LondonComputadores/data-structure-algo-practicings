"""
    O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par
      de números que somados batam com o valor da variável target.

    Ele pode ser escrito em um algoritmo que roda no tempo O(n).

    Exemplos

    Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu
      programa deve retornar:

    [-2, 11]

    O motivo é bastante simples:

    -2 + 11 = 9
"""

# Two Sum

# My solution attempt:
  
def solution(numbers, target_sum):
    numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
    num_iter = iter(numbers)
    target_sum = [9]
    for i,j in range(len(numbers)):
        numbers[i].next(num_iter)
        numbers[j].next(num_iter)
        if i + numbers[j] == target_sum:
            return []
        else:
             print('Try another way!!!')
             
# My solution attempt 2:
   
def solution(numbers, target_sum):
    numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
    num_iter = iter(numbers)
    target_sum = [9]
    for i in range(len(numbers)):
        numbers2 = next(num_iter)
        if i + numbers2 == target_sum:
            return [i, numbers2]
        print('Try another way 4!!!')

# Their Solution

def solution(numbers, target_sum):
	for number1_index in range(len(numbers)):
		number1 = numbers[number1_index]
		   
		for number2_index in range(number1_index + 1, len(numbers)):
			if number1 + numbers[number2_index] == target_sum:
				return [number1, numbers[number2_index]]
	return []