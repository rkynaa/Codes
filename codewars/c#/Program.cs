using System;
using System.Collections.Generic;

namespace c_
{
    class Program
    {
        // 6th Kyu : Stop spinning the words!
        public static string SpinWords(string sentence){
            string[] words = sentence.Split(' ');
            for (int i = 0; i < words.Length; i++){
                if (words[i].Length > 4){
                    char[] split_word = words[i].ToCharArray();
                    Array.Reverse(split_word);
                    string new_word = new string(split_word);

                    words[i] = new_word;
                }
            }
            string result = string.Join(' ', words);
            return result;
        }

        // 6th Kyu: Sum of digits / digital root (X)
        public static int DigitalRoot(long n){
            long temp = n;
            int result = 0;
            while (temp.ToString().Length != 1) {
                while(temp != 0){
                    result += (int) temp % 10;
                    temp /= 10;
                }
                if (result.ToString().Length != 1) {
                    temp = (long) result;
                    result = 0;
                }
                Console.WriteLine("Result: " + result + ", temp = " + temp);
            }
            return result;
        }

        // 6th Kyu: Find the odd int
        public static int find_it(int[] seq){
            int result = -1;
            for (int i = 0; i < seq.Length-1; i++){
                int counter = 0;
                for (int j = 0; j < seq.Length; j++){
                    if (seq[j] == seq[i]) {
                        counter++;
                    }
                }
                if (counter % 2 == 1) {
                    result = seq[i];
                }
            }
            return result;
        }

        
        // 7th Kyu: Complementary DNA
        public static string MakeComplement(string dna){
            string result = "";
            foreach(char i in dna){
                result += (i.Equals('A')) ? "T" : (i.Equals('T')) ? "A" : "";
                result += (i.Equals('C')) ? "G" : (i.Equals('G')) ? "C" : "";
            }
            return result;
        }

        // 6th Kyu: Duplicate Encoder
        public static string DuplicateEncode(string word){
            string word_temp = word.ToLower();
            string result = "";
            Dictionary<char, int> charMap = new Dictionary<char, int>();
            foreach (char i in word_temp){
                if (charMap.ContainsKey(i)){
                    charMap[i] += 1;
                } else {
                    charMap.Add(i, 1);
                }
            }
            foreach (char i in word_temp){
                if (charMap[i] == 1){
                    result += "(";
                } else {
                    result += ")";
                }
            }
            return result;
        }

        // 6th Kyu: Find The Parity Outlier
        public static int Find(int[] integers) {
            int[] int_mod2 = new int[integers.Length];
            for (int i = 0; i < integers.Length; i++){
                int_mod2[i] = (integers[i] % 2 == 0) ? 0 : 1;
            }
            for (int i = 0; i < int_mod2.Length; i++){
                int j;
                for (int j = 0; j < int_mod2.Length; j++){
                    
                }
            }
            return -1;
        }

        static void Main(string[] args)
        {
            // 6th Kyu: Stop spinning the words!
            // string test = SpinWords("Hello World");
            // Console.WriteLine(test);

            // 6th Kyu: Sum of digits / digital root (X)
            // int test = 0;
            // long number = (long) 12345678989;
            // test = DigitalRoot(number);
            // Console.WriteLine(test);
            
            // 6th Kyu: Find the odd int
            // int[] test_arr = {1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6};
            // int test = find_it(test_arr);
            // Console.WriteLine(test);

            // 7th Kyu: Complementary DNA
            // string test = MakeComplement("ATCG");
            // Console.WriteLine(test);

            // 6th Kyu: Duplicate Encoder
            // string test = DuplicateEncode("Test");
            // Console.WriteLine(test);
            
            // 6th Kyu: Find The Parity Outlier

        }
    }
}
