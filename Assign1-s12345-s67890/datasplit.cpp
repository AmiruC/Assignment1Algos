#include <sstream>
#include <memory>
#include <iostream> 
#include <fstream>
#include <algorithm>    // std::random_shuffle
#include <vector>       // std::vector
#include <ctime>        // std::time
#include <cstdlib>  
#include <stdio.h>
#include <ctype.h>
#include <random>    // std::rand, std::srand
#include <string> 

int main(){
    std::string line_;
    std::string let;
    std::string offWord;
    std::string next;
    std::string dirtyData;
    std::vector<std::string> wordArr;  
    std::ifstream file_("sampleData200k.txt");
    
    wordArr.clear();

//reads in the file of dirty data
    if(file_.is_open())
    {
        std::cout<<"Opening File"<<std::endl;
        std::string line;
        while(getline(file_, line_)) {
            //Files the vector with the letters 
            //Clears the vector 
            //Adds the input as string to vector one at a time
            wordArr.push_back(line_);
        }
    

   
    //closes file after reading   
    std::cout<<"File Close"<<std::endl;
    file_.close();
    }else{
        std::cout<<"File not open"<<std::endl;
    }

    std::cout<<"Randomising vector"<<std::endl;
     
    //Randomised function   
    std::srand (unsigned (std::time(0)));
    std::random_device rd;
    std::mt19937 g(rd());

 
    std::shuffle(wordArr.begin(), wordArr.end(), g);
    std::cout<<wordArr.size()<<std::endl;



    int length = wordArr.size();
    
    std::cout<<length<<std::endl;
    srand((unsigned) time(0));
    
    for(int i = 0; i < length; ++i){
        if(i < 500){//small 500 data set 
            std::ofstream output_file("500.txt",std::ios_base::app);
            output_file << wordArr[i];
        }else if(i>500 && i < 1501){//1k words
            std::ofstream output_file("1k.txt",std::ios_base::app);
           output_file << wordArr[i];
        }else if(i>1500 && i < 6501){//5k words
            std::ofstream output_file("5k.txt",std::ios_base::app);
            output_file << wordArr[i];
        }else if(i>6500 && i < 16501){//10k words
            std::ofstream output_file("10k.txt",std::ios_base::app);
            output_file << wordArr[i];
        }else if(i>16500 && i < 36501){//20k words
            std::ofstream output_file("20k.txt",std::ios_base::app);
            output_file << wordArr[i];
        }else if(i>36500 && i < 86501){ //50k words
            std::ofstream output_file("50k.txt",std::ios_base::app);
            output_file << wordArr[i];
        }
        else if(i>86500 && i < 186501){ //100k words
            std::ofstream output_file("100k.txt",std::ios_base::app);
            output_file << wordArr[i];
        }
        
     
    }

    

    
}


    
    
