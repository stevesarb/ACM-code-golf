fun main()=readLine()!!.split("-").map(String::toInt).let{(y,m,d)->val (Y,M)=if(m<3)(y-1) to (m+12)else y to m;println(arrayOf("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")[(d+13*(M+1)/5+Y+Y/4-Y/100+Y/400)%7])}
