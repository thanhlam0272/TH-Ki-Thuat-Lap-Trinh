Bắt đầu hàm bubbleSort( list : mảng các phần tử )
 loop = list.count;
 
 for i = 0 tới loop-1 thực hiện:
 swapped = false
 for j = 0 tới loop-1 thực hiện:
 
 /* so sánh các phần tử cạnh nhau */ 
 if list[j] > list[j+1] then
 /* tráo đổi chúng */
 swap( list[j], list[j+1] )
 swapped = true
 kết thúc if
 
 kết thúc for
 
 /*Nếu không cần tráo đổi phần tử nào nữa thì 
 tức là mảng đã được sắp xếp. Thoát khỏi vòng lặp.*/
 
 if(not swapped) then
 break
 kết thúc if
 
 kết thúc for
 
Kết thúc hàm return list

