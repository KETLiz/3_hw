// See https://aka.ms/new-console-template for more information

int[] arr2 = new int[] {1, 3, 3, 7};
int[] arrres = new int[2];
int res = 0;
for (int i = 0; i < arr2.Length/2; i++)
{
    res = arr2[i]*arr2[arr2.Length - 1 - i];
    Console.Write($"{res}, ");   
}
