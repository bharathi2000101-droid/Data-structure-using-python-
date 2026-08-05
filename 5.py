class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def append(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if not self.head:
            print("0")
            return
        
        terms = []
        temp = self.head
        while temp:
            coeff = temp.coeff
            power = temp.power
            
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
                
            temp = temp.next
            
        result_str = terms[0]
        for term in terms[1:]:
            if term.startswith("-"):
                result_str += f" - {term[1:]}"
            else:
                result_str += f" + {term}"
                
        print(result_str)


def add_polynomials(p, q):
    p_ptr = p.head
    q_ptr = q.head
    result = Polynomial()

    while p_ptr is not None and q_ptr is not None:
        if p_ptr.power == q_ptr.power:
            sum_coeff = p_ptr.coeff + q_ptr.coeff
            if sum_coeff != 0:
                result.append(sum_coeff, p_ptr.power)
            p_ptr = p_ptr.next
            q_ptr = q_ptr.next
        elif p_ptr.power < q_ptr.power:
            result.append(p_ptr.coeff, p_ptr.power)
            p_ptr = p_ptr.next
        else:
            result.append(q_ptr.coeff, q_ptr.power)
            q_ptr = q_ptr.next

    while p_ptr is not None:
        result.append(p_ptr.coeff, p_ptr.power)
        p_ptr = p_ptr.next

    while q_ptr is not None:
        result.append(q_ptr.coeff, q_ptr.power)
        q_ptr = q_ptr.next

    return result


if __name__ == "__main_":
    poly1 = Polynomial()
    poly1.append(2, 0)
    poly1.append(-4, 1)
    poly1.append(5, 2)

    poly2 = Polynomial()
    poly2.append(1, 0)
    poly2.append(2, 1)
    poly2.append(-3, 3)

    print("Polynomial 1: ", end="")
    poly1.display()

    print("Polynomial 2: ", end="")
    poly2.display()

  
    result_poly = add_polynomials(poly1, poly2)

    print("\nResultant Polynomial: ", end="")
    result_poly.display()
