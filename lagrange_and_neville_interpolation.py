def lagrange_interpolation(x_vals, y_vals, x_interp):
    """
    Polynomial interpolation using Lagrange method
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y lists must be of the same length")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required")

    n = len(x_vals)
    result = 0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                denominator = x_vals[i] - x_vals[j]
                if denominator == 0:
                    raise ZeroDivisionError("Duplicate X values detected")
                term *= (x_interp - x_vals[j]) / denominator
        result += term
    return result


def neville_interpolation(x_vals, y_vals, x_interp):
    """
    Polynomial interpolation using Neville's method
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y lists must be of the same length")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required")

    n = len(x_vals)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        Q[i][0] = y_vals[i]

    for j in range(1, n):
        for i in range(n - j):
            denominator = x_vals[i] - x_vals[i + j]
            if denominator == 0:
                raise ZeroDivisionError("Duplicate X values detected in Neville's method")
            Q[i][j] = ((x_interp - x_vals[i + j]) * Q[i][j - 1] +
                       (x_vals[i] - x_interp) * Q[i + 1][j - 1]) / denominator

    return Q[0][n - 1]


def main():
    try:
        # Define table of values
        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]

        # Point to interpolate
        x_interp = 2.5

        # Lagrange interpolation
        y_lagrange = lagrange_interpolation(x, y, x_interp)
        print(f'Lagrange interpolation at x = {x_interp}: y ≈ {y_lagrange:.4f}')

        # Neville interpolation
        y_neville = neville_interpolation(x, y, x_interp)
        print(f'Neville interpolation at x = {x_interp}: y ≈ {y_neville:.4f}')

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
