package com.swagmen.wing;

import java.awt.Color;
import java.awt.Container;

import javax.swing.JFrame;

public class Wing extends JFrame {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	static final int HEIGHT = 900;
	static final int WIDTH = 900;

	WingPanel panel;

	public Wing(String title) {
		super(title);
		// Setting the title of the JFrame

		Container container;

		panel = new WingPanel();
		panel.setBackground(Color.BLACK);
		container = getContentPane();

		// container.setLayout(null);
		setLocationByPlatform(true);
		container.add(panel);
		container.validate();
	}

	public static void main(String[] args) {
		// Game engine loop

		// Instantiate and add the SimplePanel to the frame
	}

}
