def calcular_media(num1, num2, num3):
    return (num1 * 2 + num2 * 3 + num3 * 5) / 10
    
def main():
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    media = calcular_media(num_a,num_b,num_c)
    print(f'MEDIA = {media}')

main()
