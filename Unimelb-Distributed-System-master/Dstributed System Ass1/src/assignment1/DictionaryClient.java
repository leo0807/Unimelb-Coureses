package assignment1;



import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class DictionaryClient extends JFrame implements ActionListener {

	private static final long serialVersionUID = 1L;
	private String inputContent;
	private String resultContent;
	JTextField inputText = null;
	JButton selectButton = null;
	JButton addButton = null;
	JButton deleteButton = null;
	JScrollPane jsp = null;
	JTextArea resultArea = null;
	private static final String SELECT = "SELECT";
	private static final String ADD = "ADD";
	private static final String DELETE = "DELETE";
	static int port = 0;
	
	public DictionaryClient() {
		setTitle("Dictionary");
		setSize(630, 500);
		setLocation(400, 100);
		setLayout(null);

		JLabel inputLabel = new JLabel("Please input a word：");
		inputLabel.setLayout(new BorderLayout());
		add(inputLabel);
		inputLabel.setBounds(50, 70, 250, 20);

		inputText = new JTextField(15);
		inputText.setLayout(new BorderLayout());
		add(inputText);
		inputText.setBounds(50, 100, 250, 30);

		selectButton = new JButton("Search");
		selectButton.setLayout(new BorderLayout());
		add(selectButton);
		selectButton.setBounds(330, 100, 70, 28);

		addButton = new JButton("Add");
		addButton.setLayout(new BorderLayout());
		add(addButton);
		addButton.setBounds(430, 100, 70, 28);

		deleteButton = new JButton("Delete");
		deleteButton.setLayout(new BorderLayout());
		add(deleteButton);
		deleteButton.setBounds(530, 100, 70, 28);

		JLabel resultLabel = new JLabel("Result：");
		resultLabel.setLayout(new BorderLayout());
		add(resultLabel);
		resultLabel.setBounds(50, 170, 200, 20);

		resultArea = new JTextArea();
		resultArea.setLayout(new BorderLayout());
		// JScrollPane
		jsp = new JScrollPane(resultArea);
		add(jsp);
		jsp.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
		jsp.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
		jsp.setBounds(50, 200, 250, 150);

		selectButton.addActionListener(this);
		addButton.addActionListener(this);
		deleteButton.addActionListener(this);
	};

	@Override
	public void actionPerformed(ActionEvent e) {

		inputContent = inputText.getText();
		resultContent = resultArea.getText();
		String InputData = null;
		
		if(inputContent!=null||inputContent!="") {
		
			if ("Add".equals(e.getActionCommand())) {
				InputData = ADD + "#" + inputContent + "#" + resultContent;
				
			} else if ("Delete".equals(e.getActionCommand())) {
				resultArea.setText("");
				inputText.setText("");
				InputData = DELETE + "#" + inputContent;
			} else {
				InputData = SELECT + "#" + inputContent;
			}
			sentMessage(InputData);
		}else {
			resultArea.setText("Cannot be null");
			return;
		}
		
	}

	private void sentMessage(String InputData) {
		try {
			@SuppressWarnings("resource")
			Socket socket = new Socket("127.0.0.1", port);
			
			new Thread() {
				@Override
				public void run() {
					try {
						InputStream is = socket.getInputStream();
						byte[] returnData = new byte[1024];
						int length = -1;
						while ((length = is.read(returnData)) != -1) {
							resultArea.setText(new String(returnData, 0, length));
						}
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}.start();

			// Send messages to the Server
			new Thread() {
				@Override
				public void run() {
					try {
						OutputStream os = socket.getOutputStream();
						os.write(InputData.getBytes());
					} catch (IOException e) {
						e.printStackTrace();
					}

				}
			}.start();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		port = Integer.parseInt(args[0]);
		DictionaryClient client = new DictionaryClient();
		client.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		client.setVisible(true);
	}
}
