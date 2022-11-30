// See https://aka.ms/new-console-template for more information
int[] arr = new int[] {1, 3, 3, 7};
int sum = 0;
for (int i = 0; i < arr.Length; i++)
{
    if (i % 2 != 0) sum += arr[i];
    
}
Console.Write(sum);