import math

def volume(radius):
    return (4.0 / 3.0) * math.pi * (radius ** 3)

if __name__ == "__main__":
    print("INET4031 Sphere Volume Calculator")
    r = float(input("Enter the radius of the sphere: "))
    v = volume(r)
    print(f"The volume of the sphere is: {v}")
