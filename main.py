def es_expresion_regular_valida(expresion):
    def validar_expresion(expresion):
        stack = []

        for char in expresion:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False

        return len(stack) == 0

    if validar_expresion(expresion):
        i = 0
        while i < len(expresion):
            char = expresion[i]
            if char == '*' or char == '|' or char == '.':
                if i == 0 or i == len(expresion) - 1:
                    return False
                prev_char = expresion[i - 1]
                next_char = expresion[i + 1]
                if prev_char in ['*', '|', '.'] or next_char in ['*', '|', '.']:
                    return False
            i += 1
        return True
    else:
        return False

def main():
    expresion = input("Introduce una expresión regular: ")
    if es_expresion_regular_valida(expresion):
        print(f"'{expresion}' es una expresión regular válida.")
    else:
        print(f"'{expresion}' no es una expresión regular válida.")

if __name__ == "__main__":
    main()
