package assignment1;



public class GED {


	// [m,d,i,r]=[1,-1,-1,-1]
	public int global(String A, String B) {
		int[][] dp = new int[A.length() + 1][B.length() + 1];
		
		dp[0][0] = 0;
		for (int i = 1; i <= A.length(); i++)
			dp[i][0] = i * (-1);
		for (int j = 1; j <= B.length(); j++)
			dp[0][j] = j * (-1);
		for (int i = 1; i <= A.length(); i++) {
			for (int j = 1; j <= B.length(); j++) {
				dp[i][j] = Math.max(dp[i - 1][j] - 1, Math.max(dp[i][j - 1] - 1, dp[i - 1][j - 1] +equal(A.charAt(i-1),B.charAt(j-1))));
				//System.out.print(dp[i][j]+" ");
			}
			//System.out.println();
		}
		return dp[A.length()][B.length()];
	}

	public int equal(char a,char b){
		if(a==b){
			return 1;
		}else 
			return -1;
	}
}