package assignment1;


import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Hashtable;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class DictionaryServer {

	private static final String ADD = "ADD";
	private static final String DELETE = "DELETE";
	static int port = 0;
	private static Map<String, String> mapData = new Hashtable<String, String>();
	
	public static void main(String[] args) {
		port = Integer.parseInt(args[0]);
		DictionaryServer server = new DictionaryServer();
		try {
			@SuppressWarnings("resource")
			ServerSocket serverSocket = new ServerSocket(port);
			while (true) {
				Socket socket = serverSocket.accept();
				ChatThread thread = server.new ChatThread(socket);
				thread.start();
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	class ChatThread extends Thread {

		private Socket socket = null;
		private byte[] data;

		public ChatThread(Socket socket) {
			this.socket = socket;
		}

		@Override
		public void run() {
			try {
				// store the dictionary
				mapData.put("China", "Country");
				// Get message from Client port
				InputStream is = socket.getInputStream();
				data = new byte[1024];
				int length = -1;
				OutputStream os;
				String secondData = null;
				if ((length = is.read(data)) != -1) {
					data = new String(data, 0, length).getBytes();
					String clientData = new String(data, 0, length);
					if (clientData.indexOf("#") != -1) {
						String firstData = clientData.substring(0, clientData.indexOf("#"));
						synchronized (mapData) {
						// Get the symbol of "ADD"
						if (ADD.equals(firstData)) {
							// Get the meaning of the word
							secondData=clientData.substring(clientData.indexOf("#") + 1,clientData.lastIndexOf("#"));
							System.out.println(Thread.currentThread().getName());
							String thirdData = clientData.substring(clientData.lastIndexOf("#") + 1);
							if(mapData.containsKey(secondData)) {
								os = socket.getOutputStream();
								os.write("The word has been added".getBytes());
							}else{
								mapData.put(secondData, thirdData);
								os = socket.getOutputStream();
								os.write("Added Successfully".getBytes());
							}
						} else if (DELETE.equals(firstData)) {
							System.out.println(Thread.currentThread().getName());
							// Get the added word
							secondData = clientData.substring(firstData.length() + 1);
							mapData.remove(secondData);
							os = socket.getOutputStream();
							os.write("Delete Sucessfully".getBytes());
						} else {
						
							System.out.println(Thread.currentThread().getName());
							// Get the word required to search
							secondData = clientData.substring(firstData.length() + 1);
							String value = mapData.get(secondData);
							os = socket.getOutputStream();
							if (value == null) {
								os.write("No meaning finded".getBytes());
							}else {
								os.write(value.getBytes());
							}
							}
						}
					
				  }
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

	}

}