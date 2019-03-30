/**
 * 
 */
package udp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

/**
 * @author Scott
 *
 */
public class UdpServer {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		DatagramSocket datagramSocket= new DatagramSocket(6789);
		byte[] buffer = new byte[1024];
		while(true) {
			DatagramPacket request = new DatagramPacket(buffer,buffer.length);
			datagramSocket.receive(request);
			DatagramPacket reply = new DatagramPacket(request.getData(),request.getLength(),request.getAddress(),request.getPort());
			datagramSocket.send(reply);
	
			if (datagramSocket!=null) {
				datagramSocket.close();
			}
		}
	}

}
